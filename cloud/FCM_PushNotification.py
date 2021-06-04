import requests
import json

def notify():
    serverToken = <SERVERTOKEN>
    deviceToken = <DEVICETOKEN> 

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
    }

    body = {
        'notification': {'title': 'A Milestone Achieved',
                         'body': 'You have walked for 1 min'
                         },
        'to':
            deviceToken,
        'priority': 'high',
        #   'data': dataPayLoad,
    }
    response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response.status_code)
    print(response.json())
