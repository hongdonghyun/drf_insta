from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)

