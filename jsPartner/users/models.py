from django.db import models
from datetime import datetime

# User model

class UserManager(models.Manager):
    def create_user(self, nick, password):
        user = self.create(nick=nick, password=password, created_date=datetime.now())
        return user

class User(models.Model):
    nick = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField('user created time')
    objects = UserManager()
