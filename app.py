from flask import Flask, request, jsonify, Response
import json


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Flask on heroku'


@app.route('/buttons-template')
def get_buttons_template():
    data = {
        "line_payload": [
            {
                "type": "template",
                "altText": "this is a buttons template",
                "template": {
                    "type": "buttons",
                    "title": "Title",
                    "text": "Text",
                    "actions": [
                        {
                            "type": "message",
                            "label": "Action 1",
                            "text": "Action 1"
                        },
                        {
                            "type": "message",
                            "label": "Action 2",
                            "text": "Action 2"
                        }
                    ]
                }
            }
        ]
    }

    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['reply-by-object'] = True
    return resp


@app.route('/confirm-template')
def get_confirm_template():
    data = {
        "line_payload": [
            {
                "type": "template",
                "altText": "this is a confirm template",
                "template": {
                    "type": "confirm",
                    "actions": [
                        {
                            "type": "message",
                            "label": "Yes",
                            "text": "Yes"
                        },
                        {
                            "type": "message",
                            "label": "No",
                            "text": "No"
                        }
                    ],
                    "text": "Continue?"
                }
            }
        ]
    }

    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['reply-by-object'] = True
    return resp


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
