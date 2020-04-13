from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker


app = Flask(__name__)
Bootstrap(app)
datepicker(app)


@app.route('/')
def datepicker():
    return render_template('index.html')
