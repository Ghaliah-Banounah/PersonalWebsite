from django.db import models

class Contact(models.Model):

    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()
    sentAt = models.DateTimeField(auto_now_add=True)