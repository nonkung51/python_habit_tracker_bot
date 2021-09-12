import requests
import config

LINE_MESSAGING_API = "https://api.line.me/v2/bot"
LINE_HEADER = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {config.LINE_ACCESS_TOKEN}"
}

def reply(token, payload):
    req = requests.post(
        f"{LINE_MESSAGING_API}/message/reply", 
        headers=LINE_HEADER, 
        json={ "replyToken": token, "messages": [payload] }
    )
    return req.json()
