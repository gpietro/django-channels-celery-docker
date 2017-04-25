import json
from channels import Channel, Group
from .actions import actions


def reducer(sender, **kwargs):
    action = kwargs['action']
    payload = kwargs['payload']
    reply_channel = kwargs['reply_channel']
    
    if action in actions:
        actions[action](payload)
        # Update all clients
        Group("todo_app").send({
            "text": json.dumps({
                "type": action,
                "done": True,
                "channelId": reply_channel,
                **payload
            })
        })
    else:
        print('Action has not been implemented yet...')
