
from flask import Flask, request

# LINE
from line import reply


app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def hook():
    data = request.json
    event = data['events'][0]
    return reply(event['replyToken'], event['message'])


app.run(debug=True, port=5000)