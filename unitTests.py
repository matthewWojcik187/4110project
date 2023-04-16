#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
import app
from app.models import User, Post
from app.main.forms import EditProfileForm
from config import Config
from wtforms import StringField
from flask import current_app
import graph





class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

    def test_follow(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        # create four users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body="post from john", author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from mary", author=u3,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from david", author=u4,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup the followers
        u1.follow(u2)  # john follows susan
        u1.follow(u4)  # john follows david
        u2.follow(u3)  # susan follows mary
        u3.follow(u4)  # mary follows david
        db.session.commit()

        # check the followed posts of each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])
    
    def test_archived_posts(self):
        #Creating users to test with
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body="post from john", author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="good post from john", author=u1,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="good post from susan", author=u2,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        #Archiving posts
        u1.archive(p2)
        u2.archive(p2)
        u1.archive(p4)

        db.session.commit()

        #Checking that only posts that have been selected have been archived
        self.assertTrue(u1.isArchived(p4.id))
        self.assertTrue(u1.isArchived(p2.id))
        self.assertTrue(u2.isArchived(p2.id))
        self.assertFalse(u2.isArchived(p4.id))
        self.assertFalse(u1.isArchived(p1.id))
        self.assertFalse(u2.isArchived(p1.id))
        self.assertFalse(u1.isArchived(p3.id))
        self.assertFalse(u2.isArchived(p3.id))

    def test_unarchived_posts(self):
        #Creating 2 users
        u1 = User(username='tyler', email='john@example.com')
        u2 = User(username='kyle', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body="Hi im tyler", author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="hi again im tyler", author=u1,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="Kyle says ayo", author=u2,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="I like energy drinks", author=u2,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        #Archiving all the posts
        u1.archive(p1)
        u1.archive(p2)
        u1.archive(p3)
        u1.archive(p4)

        u2.archive(p1)
        u2.archive(p2)
        u2.archive(p3)
        u2.archive(p4)

        db.session.commit()

        #asserting they are archived
        self.assertTrue(u1.isArchived(p1.id))
        self.assertTrue(u1.isArchived(p2.id))
        self.assertTrue(u1.isArchived(p3.id))
        self.assertTrue(u1.isArchived(p4.id))

        self.assertTrue(u2.isArchived(p1.id))
        self.assertTrue(u2.isArchived(p2.id))
        self.assertTrue(u2.isArchived(p3.id))
        self.assertTrue(u2.isArchived(p4.id))

        #Removing half
        u1.unarchive(p1)
        u1.unarchive(p2)
        u2.unarchive(p1)
        u2.unarchive(p2)

        db.session.commit()

        #Asserting only half have been removed
        self.assertFalse(u1.isArchived(p1.id))
        self.assertFalse(u1.isArchived(p2.id))
        self.assertTrue(u1.isArchived(p3.id))
        self.assertTrue(u1.isArchived(p4.id))

        self.assertFalse(u2.isArchived(p1.id))
        self.assertFalse(u2.isArchived(p2.id))
        self.assertTrue(u2.isArchived(p3.id))
        self.assertTrue(u2.isArchived(p4.id))

        #Removing the rest
        u1.unarchive(p3)
        u1.unarchive(p4)
        u2.unarchive(p3)
        u2.unarchive(p4)

        db.session.commit()

        #asserting that all the post are now unarchived
        self.assertFalse(u1.isArchived(p1.id))
        self.assertFalse(u1.isArchived(p2.id))
        self.assertFalse(u1.isArchived(p3.id))
        self.assertFalse(u1.isArchived(p4.id))

        self.assertFalse(u2.isArchived(p1.id))
        self.assertFalse(u2.isArchived(p2.id))
        self.assertFalse(u2.isArchived(p3.id))
        self.assertFalse(u2.isArchived(p4.id))

    def test_profilePic(self):
        #Creating a user
        u = User(username='john', email='john@example.com')
        #Setting the users profile picture to a dog
        u.profilePicture = 'dog.png'
        db.session.add(u)
        db.session.commit()
        #Asserting that the avatar is not overwritten
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))
        #Asserting the profile picture is now a dog
        self.assertEqual(u.profilePicture, 'dog.png')
        #Asserting the profile picture is not a cat
        self.assertNotEqual(u.profilePicture, 'cat.jpg')

    def test_2fa(self):
        #Creating a user
        u = User(username='john', email='john@g.g')

        #Generating a authenication token for the user
        tok = u.get_totp_uri()
        u.token = tok
        db.session.add(u)
        db.session.commit()
        #Asserting that the token generated matches the one expected for the user
        self.assertEqual(u.otp_secret, u.token[u.token.find('=')+1:u.token.find('&')])
        #Asserting other random tokens will not satisfy the condition
        self.assertNotEqual(u.otp_secret, '1234567890QWERTY')



if __name__ == '__main__':
    unittest.main(verbosity=2)
