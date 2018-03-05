from datetime import datetime
import json

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import hug

import hook

engine = create_engine("sqlite:///steemit.sqlite")
session_factory = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    body = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return '<Steemit_User %r>' % (self.name)

Base.metadata.create_all(bind=engine)


@hug.cli()
@hug.get(examples='name=tolgahanuzun&vote=True&follow=True&post=True&transfer=True')
def user_details(name: hug.types.text,
                vote: hug.types.text,
                follow: hug.types.text,
                post: hug.types.text,
                transfer: hug.types.text,
                hug_timer=3):
    
    # Control

    status = {
        'vote' : vote,
        'custom_json' : follow,
        'comment' : post,
        'transfer' : transfer,
        'curation_reward' : True,
        'claim_reward_balance' : True,
        'author_reward' : True,
        'account_update' : False,
        'comment_benefactor_reward': False,
        'transfer_to_vesting': False,
        'account_witness_vote': False,
        'limit_order_create': False,
        'fill_order': False,
        'limit_order_cancel': False,
        'comment_options': False
    }

    #cleaning
    feed_lists = hook.feed_list(name)
    new_lists = []
    for feed in feed_lists:
        if status[feed[1]['op'][0]] == 'True':
            new_lists.append(feed[1]['op'])
    

    posting = []
    #posting
    for nw in new_lists:
        if nw[0] == 'vote':
            post_link = "/@{}/{} ".format(nw[1]['author'], nw[1]['permlink'])
            text_link =  "<a href='https://www.steemit.com{}'>{}</a>".format(post_link, nw[1]['permlink'])
            text = "{} voteup it {}(%{})".format(nw[1]['voter'], text_link, float(nw[1]['weight']/100) )
            posting.append(text)
        if nw[0] == 'custom_json':
            data = json.loads(nw[1]['json'])
            text = '{1} following {0}'.format(data[1]['following'], data[1]['follower'])
            posting.append(text)
    return {'result': posting,
            'took': float(hug_timer)}

if __name__ == '__main__':
    user_details.interface.cli()
