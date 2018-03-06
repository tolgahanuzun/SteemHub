from datetime import datetime
import json

import hug
import hook

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
        'comment_options': False,
        'account_create_with_delegation' : False,
        'delegate_vesting_shares':False
    }

    #cleaning
    feed_lists = hook.feed_list(name)
    new_lists = []
    for feed in feed_lists:
        if status[feed[1]['op'][0]] == 'true':
            new_lists.append(feed[1]['op'])


    posting = []
    #posting
    for nw in new_lists:
        if nw[0] == 'vote':
            post_link = "/@{}/{} ".format(nw[1]['author'], nw[1]['permlink'])
            text_link =  "<a href='https://www.steemit.com{}'>{}</a>".format(post_link, nw[1]['permlink'][:30])
            text = "{} voteup it {}(%{})".format(nw[1]['voter'], text_link, float(nw[1]['weight']/100) )
            posting.append(text)

        if nw[0] == 'custom_json':
            data = json.loads(nw[1]['json'])
            text = '{1} following {0}'.format(data[1].get('following'), data[1].get('follower'))
            posting.append(text)

        if nw[0] == 'comment':
            if nw[1].get('parent_author'):
                post_link = "/@{}/{} ".format(nw[1]['author'], nw[1]['permlink'])
                text_link =  "<a href='https://www.steemit.com{}'>{}</a>".format(post_link, nw[1]['permlink'][:30])            
                text = '{} comment to post {}'.format(nw[1]['author'], text_link)
                posting.append(text)

        if nw[0] == 'transfer':
            text = '{} to transfer {} - {}'.format(nw[1]['from'], nw[1]['to'], nw[1]['amount'])
            posting.append(text)
    posting.reverse()
    return {'result': posting,
            'took': float(hug_timer)}

if __name__ == '__main__':
    user_details.interface.cli()
