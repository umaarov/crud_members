from django.db import models


class Member(models.Model):
    image = models.ImageField(upload_to="images/", default="about.jpg")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
