from django.db import models
from django.forms import ModelForm
from datetime import datetime


class JsUserManager(models.Manager):
    def create_user(self, name, password, email):
        created_time = datetime.utcnow()
        user = self.create(name=name, password=password, email=email, created=created_time)
        return user


class JsUser(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    created = models.DateTimeField()

    objects = JsUserManager()


class JsUserForm(ModelForm):
    class Meta:
        model = JsUser
        fields = ['name', 'password', 'email']