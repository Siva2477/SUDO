Hii This python coad for login 
import os
from datetime import datetime
from flask import Flask, render_template, make_response

app = Flask(__name__)


def get_app_debug_info():
    cfg_items = {s: v for s, v in os.environ.items()}
    cfg_items['datetime'] = datetime.now().isoformat()
    return cfg_items


@app.route('/')
def welcome():
    return {
        'msg': 'Hello World! This is a simple Python app using Flask! But wait there is more!',
        'endpoints': ['/', '/ping', '/debug', '/debug/ui']
    }

