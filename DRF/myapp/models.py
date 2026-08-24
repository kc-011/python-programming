from django.db import models

class Student(models.Model):
    rolno = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=250)
    stream = models.CharField(max_length=250)
    desc = models.TextField(max_length=1000)

    