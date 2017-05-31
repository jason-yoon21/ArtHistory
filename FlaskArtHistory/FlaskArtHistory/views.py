"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskArtHistory import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        numbers = [1,2,3,4],
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Cathedral of Notre Dame'
    )

@app.route('/workscited')
def workscited():
    return render_template('workscited.html')