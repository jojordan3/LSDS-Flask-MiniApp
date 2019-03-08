'''
SQLalchemy models for the mini application
'''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    '''Twitter users that we pull and analyze tweets for
    '''
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Tweet(DB.Model):
    '''Tweets
    '''
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(500))
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'),
                        nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets'), lazy=True)

    def __repr__(self):
        return '<Tweet: {}>'.format(self.text)


'''
>>> from flask_miniapp.models import *
>>> u1 = User(name='austen')
>>> t1 = Tweet(text='Lambda rocks')
>>> u1.tweets
[]
>>> u1.tweets.append(t1)
>>> u1
<User austen>
>>> u1.tweets
[<Tweet: Lambda rocks>]
>>> DB.session.add(u1)
>>> DB.session.add(t1)
>>> DB.session.commit()
>>> User.query.filter(User.name=='austen').first()
<User austen>
>>> User.query.filter(User.name=='austen').first().tweets
[<Tweet: Lambda rocks>]
'''
