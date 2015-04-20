from django.db import models
from django.forms import ModelForm


class JsUserManager(models.Manager):
    def create_user(self, name, password):
        user = self.create_user(name=name, password=password)
        return user


class JsUser(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created = models.DateTimeField()

    objects = JsUserManager()


class JsUserForm(ModelForm):
    class Meta:
        model = JsUser
        fields = ['name', 'password']