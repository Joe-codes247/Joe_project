from django.db import models

class student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=False, blank=False)














