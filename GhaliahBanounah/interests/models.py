from django.db import models

class Interest(models.Model):

    title = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)