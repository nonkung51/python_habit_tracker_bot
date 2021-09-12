
from flask import Flask, request

# LINE
from line import reply, push


app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def hook():
    data = request.json
    event = data['events'][0]
    print(event)
    return reply(event['replyToken'], event['message'])

@app.route("/test", methods=['POST'])
def test():
    data = request.json
    return push(data['to'], data['message'])


app.run(debug=True, port=5000)