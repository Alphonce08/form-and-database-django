from django.db import models


class student(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    idnum = models.CharField(max_length=30, blank=False, null=False)

def __dir__(self):
    return self.name



