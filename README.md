
# VGS SIMPLE FLASK TEST APP

This is a simple Flask application which allows you to collect > encrypt > send payment card information without storing sensitive data on your server. That information is entered in a form but is sent directly to VGS vault, which encrypts it and returns aliased information that can be used to decrypt it (retrieve initial input).The following [video](https://www.loom.com/share/c917ef240bb54ffba4b5accec30c352d) demonstrates how VGS redacts and reveals data.

## Initial requirements

* [python](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [ngrok](https://ngrok.com/download)
* [VGS](https://www.verygoodsecurity.com/)

## Installation

* Clone/download this project
* Navigate to the project directory and create a virtual environment folder:
```
$ cd test_vgs
$ python3 -m venv venv
```
* Activate virtual environment:
```
$ source .venv/bin/activate
```
* Install requirements::
```
$ pip install -r requirements.txt
```

## VGS + Flask application usage
* Set configurations for the inbound and outbound rules in the [VGS Dashboard](https://dashboard.verygoodsecurity.com/dashboard/) (use ngrok forwarding URL)
* Save VGS tenant ID of your sandbox (`{tenant_id}.sandbox.verygoodproxy.com`)
* Save VGS Sandbox certificate
* Save VGS credentials file
* Run the Flask application:
```
$ flask run
```
* Run ngrok:
```
$ ngrok http 5000
```
* Set configurations for the inbound and outbound rules in the VGS Dashboard and directly in the code
* Navigate to the ngrok forwarding URL (or `127.0.0.1:5000`) and fill out the form to encrypt the data. Fill in the next form with the decrypt data.