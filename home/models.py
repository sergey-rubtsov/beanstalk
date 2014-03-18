from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    message = models.CharField(max_length=10000)
