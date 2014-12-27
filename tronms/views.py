from flask import render_template
from tronms import tronms
from models import User



@tronms.route('/')
def index():
    return render_template('index.html')
