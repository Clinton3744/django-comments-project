from django.db import models

class Details(models.Model):

    title=models.CharField(max_length=20)
    commands=models.CharField(max_length=50)
    date=models.DateTimeField()
