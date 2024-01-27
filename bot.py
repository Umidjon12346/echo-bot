import requests
from settings import URL
from sends import send_contact,send_message,send_Photo,send_video
from time import sleep


def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()["result"]

        if len(result) !=0:
            return result[-1]
        else:
            return 404 
    
    return response.status_code

def main(url):
    last_update_id = -1
    while True:
        curr_update = get_last_update(url)

        if curr_update['update_id'] != last_update_id:
            user = curr_update['message']['from']
            text = curr_update['message'].get('text')
            ph = curr_update['message'].get("photo")
            contact = curr_update['message'].get("contact")
            vidoe = curr_update['message'].get("contact") 

            if text:
                send_message(url,user["id"],text)
            elif contact:
                send_contact(url,user["id"],contact['phone_number'],contact['first_name'])
            elif ph:
                send_Photo(url,user['id'],ph[0]['file_id'])
            last_update_id = curr_update['update_id']
        sleep(0.5)
main(URL)

