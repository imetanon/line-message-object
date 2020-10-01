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


@app.route('/carousel-template')
def get_carousel_template():
    data = {
        "line_payload": [
            {
                "type": "template",
                "altText": "this is a carousel template",
                "template": {
                    "type": "carousel",
                    "columns": [
                        {
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
                        },
                        {
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
                    ]
                }
            }
        ]
    }

    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['reply-by-object'] = True
    return resp


@app.route('/image-carousel-template')
def get_image_carousel_template():
    data = {
        "line_payload": [
            {
                "type": "template",
                "altText": "this is an image carousel template",
                "template": {
                    "type": "image_carousel",
                    "columns": [
                        {
                            "imageUrl": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
                            "action": {
                                "type": "message",
                                "label": "Action 1",
                                "text": "Action 1"
                            }
                        },
                        {
                            "imageUrl": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg",
                            "action": {
                                "type": "message",
                                "label": "Action 2",
                                "text": "Action 2"
                            }
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


@app.route('/flex-message')
def get_image_carousel_template():
    data = {
        "line_payload": [
            {
                "type": "flex",
                "altText": "this is a flex message",
                "contents": {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "action": {
                            "type": "uri",
                            "label": "Line",
                            "uri": "https://linecorp.com/"
                        }
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Brown Cafe",
                                "weight": "bold",
                                "size": "xl",
                                "contents": []
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "margin": "md",
                                "contents": [
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "icon",
                                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": "4.0",
                                        "size": "sm",
                                        "color": "#999999",
                                        "flex": 0,
                                        "margin": "md",
                                        "contents": []
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "margin": "lg",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Place",
                                                "size": "sm",
                                                "color": "#AAAAAA",
                                                "flex": 1,
                                                "contents": []
                                            },
                                            {
                                                "type": "text",
                                                "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                                "size": "sm",
                                                "color": "#666666",
                                                "flex": 5,
                                                "wrap": true,
                                                "contents": []
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Time",
                                                "size": "sm",
                                                "color": "#AAAAAA",
                                                "flex": 1,
                                                "contents": []
                                            },
                                            {
                                                "type": "text",
                                                "text": "10:00 - 23:00",
                                                "size": "sm",
                                                "color": "#666666",
                                                "flex": 5,
                                                "wrap": true,
                                                "contents": []
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 0,
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "CALL",
                                    "uri": "https://linecorp.com"
                                },
                                "height": "sm",
                                "style": "link"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "WEBSITE",
                                    "uri": "https://linecorp.com"
                                },
                                "height": "sm",
                                "style": "link"
                            },
                            {
                                "type": "spacer",
                                "size": "sm"
                            }
                        ]
                    }
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
