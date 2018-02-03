from datetime import datetime

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
@hug.get(examples='name=tolgahanuzun')
def user_details(name: hug.types.text, hug_timer=3):
    """User Details"""

    user = session_factory.query(Model).filter_by(name=name).all()
    if user:
        last_update = datetime.now() - user[0].date
        
        if last_update.seconds / 60 > 10:
            text = ''
            result = hook.hook(name)
            for hooks in result:
                text = text + ':::::' + hooks
            user[0].body = text
            user[0].date = datetime.now()
            session_factory.add(user[0])
            session_factory.commit()
        else:
            result = user[0].body.split(':::::')[1:]

    else:
        text = ''
        result = hook.hook(name)
        for hooks in result:
            text = text + ':::::' + hooks

        user = Model()
        user.name = name
        user.body = text
        user.date = datetime.now()
        session_factory.add(user)
        session_factory.commit()

    return {'result': result,
            'took': float(hug_timer)}

if __name__ == '__main__':
    user_details.interface.cli()