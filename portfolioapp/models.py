from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class AboutMe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    fullname = models.CharField(max_length = 50)
    nickname = models.CharField(max_length = 25)
    profile = models.CharField(max_length = 100)
    specialist = models.CharField(max_length = 100)
    age = models.IntegerField()
    number=models.IntegerField()
    education = models.CharField(max_length = 100)
    mail = models.EmailField()
    linkedin = models.CharField(max_length = 500)
    twitter = models.CharField(max_length = 500)
    github = models.CharField(max_length = 500)
    facebook = models.CharField(max_length = 500)
    whatsapp = models.IntegerField()
    telegram = models.IntegerField()
    address = models.CharField(max_length = 500)
    aboutme = models.TextField(max_length = 2000)

    def __str__(self):
        return self.user.username
