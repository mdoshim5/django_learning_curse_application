from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summery(self):
        return self.body[:50]