from socket import MsgFlag
from flask import Flask, jsonify, request, render_template
import os
from botocore import endpoint
from flask import Flask, render_template, request
import boto3 
import json
import pulsar

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:4566")
table = dynamodb.Table('tracking_data')

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('pulsar-test', 'my-subscription')
print("Đã kết nối với pulsar server")
while True:
    print("Khởi động consume_app")
    #receive message from pulsar topic
    msg = consumer.receive()
    print("Đã nhận")
    if msg:
        print(msg)
    try:        
        # Acknowledge successful processing of the message
        consumer.acknowledge(msg)
        #this code is to convert the received message into the right format to add to dynamodb
        try:
            json_data = json.loads(msg.data().decode('utf8'))
            print(json_data)
            dict_data = json.loads(json.dumps(json_data))
            print(dict_data)
            new_data = json.loads(json.dumps(dict_data), parse_float=Decimal)
            print("Đã xử lí")
        except Exception as e:
            print(e)

        #add the data into dynamodb
        try:
            print("Start putting item into dynamodb data table...")
            table.put_item(Item=new_data)
            print("Done put item")
        except Exception as e: 
            print(e)
    
    except:
        # Message failed to be processed
        consumer.negative_acknowledge(msg)

client.close()



