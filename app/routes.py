from app import app
from flask import render_template, request
import requests
import os


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_cc_info', methods=['POST'])
def add_cc_info():

    cc_number = request.form['cc_number']
    exp_date = request.form['exp_date']
    cvv = request.form['cvv']

    return render_template('message.html',
                           cc_number=cc_number,
                           exp_date=exp_date,
                           cvv=cvv)


@app.route('/forward', methods=['POST'])
def forward():

    cc_number = request.form['cc_number']
    exp_date = request.form['exp_date']
    cvv = request.form['cvv']

    payload = {'cc_number': cc_number, 'exp_date': exp_date, 'cvv': cvv}
    os.environ['HTTPS_PROXY'] = 'https://USq3WZ9kJmpqHBkzaTaA24vo:be7b4139-fa3a-4392-adae-0832d491fc18@tntfjvtrllv.sandbox.verygoodproxy.com:8080'
    vgs_post = requests.post('https://echo.apps.verygood.systems/post',
                             json=payload,
                             verify='/Users/andrew.vazinsky/Desktop/VGS/test_vgs/app/static/cert/cert.pem')

    res = vgs_post.json()
    data = res['json']

    cc_number_revealed = data['cc_number']
    exp_date_revealed = data['exp_date']
    cvv_revealed = data['cvv']

    return render_template('forward.html',
                           cc_number=cc_number_revealed,
                           exp_date=exp_date_revealed,
                           cvv=cvv_revealed)
