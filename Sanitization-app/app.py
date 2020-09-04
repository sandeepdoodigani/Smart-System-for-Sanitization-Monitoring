# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:12:47 2020

@author: Sandeep Doodigani
"""

from flask import Flask, render_template
import requests

import boto3

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello world"

@app.route('/world')
def world():
    return "Hello world"

@app.route('/world1')
def world1():
    return "Hello world"   

@app.route('/')
def index():
    names = ['nidhi','sandeep','pradeepthi','Prasad']
    date = []
    for i in names:
        url = "https://5gyg4nqqsb.execute-api.us-east-1.amazonaws.com/sanitizerappretrieve?name="+i
        resp = requests.get(url)
        data = resp.json()
        print(data)
        #[{'name': 'sandeep', 'date': '31-09-2020'}]
        date.append(data['datetime'])
    return render_template('stats.html', p1= names[0],d1=date[0], p2=names[1], d2=date[1],p3=names[2], d3=date[2],p4=names[3], d4=date[3])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)