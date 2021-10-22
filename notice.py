import requests


def notice(message):
    token = 'XXXXXXXXXX'
    endpoint = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': "Bearer " + token}
    params = {'message': message}
    requests.post(endpoint, headers=headers, data=params)
