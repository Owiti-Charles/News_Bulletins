from flask import render_template
from app import app

@app.route('/')
def HomePage():
    return render_template('sources.html')