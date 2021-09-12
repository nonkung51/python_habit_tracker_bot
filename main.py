from flask import Flask, request
import csv
import time

# LINE
from line import reply, push

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def hook():
    data = request.json
    event = data['events'][0]
    with open('time_table.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([int(time.time()), event['message']['text']])
    return reply(event['replyToken'], { 'type': 'text', 'text': f"บันทึก {event['message']['text']} ลงในฐานข้อมูลแล้วน้า ~"})

@app.route("/push", methods=['POST'])
def cronHandler():
    data = request.json
    return push(data['to'], data['message'])

@app.route("/data", methods=['GET'])
def readData():
    data = []
    with open('time_table.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        for row in reader:
            data.append(row)
    return { 'success': True, 'data': data }

app.run(debug=False, port=5000)