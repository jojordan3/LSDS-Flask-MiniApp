'''
Main application and routing logic for miniapp (application configuration
and routing logic)
'''
from flask import Flask, render_template, request
from .models import DB, User, Tweet
from decouple import config


def create_app():
    '''Create and configure an instance of the Flask application
    '''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config(DATABASE_URL)
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    app.config['ENV'] = config('ENV')
    DB.init_app(app)

    @app.route('/')
    def root():
        # auto searches templates folder
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Databse Reset', users=[])

    return app
