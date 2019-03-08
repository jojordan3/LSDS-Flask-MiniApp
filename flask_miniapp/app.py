'''
Main application and routing logic for miniapp
'''
from flask import Flask, render_template, request
from .models import DB, User, Tweet


def create_app():
    '''Create and configure an instance of the Flask application
    '''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['ENV'] = 'debug'
    DB.init_app(app)

    @app.route('/')
    def root():
        # auto searches templates folder
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    return app
