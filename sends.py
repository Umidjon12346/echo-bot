import requests
def send_message(url: str,chat_id: int, text, parse_mode=False):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    if parse_mode:
        payload['parse_mode'] = 'HTML'

    requests.get(url, params=payload)

def send_contact(url: str,chat_id: int, phone_number,first_name, parse_mode=False):
    endpoint = '/sendContact'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'first_name': first_name,
        "phone_number": phone_number
    }
    if parse_mode:
        payload['parse_mode'] = 'HTML'

    requests.get(url, params=payload)

def send_video(url,chat_id: int, video, parse_mode=False):
    endpoint = '/sendContact'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        "video" : video
    }
    if parse_mode:
        payload['parse_mode'] = 'HTML'

    requests.get(url, params=payload)
def send_Photo(url,chat_id, photo, parse_mode=False):
    endpoint = "/sendPhoto"
    url+=endpoint
    payload={
        "chat_id":chat_id,
        "photo":photo
    }
    if parse_mode:
        payload['parse_mode'] = 'HTML'
    requests.get(url,params = payload)