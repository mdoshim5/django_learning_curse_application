from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    publish_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    body = models.TextField()
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    hunter = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    
    def body_summery(self):
        return self.body[:220]
    
    def publish_date_pretty(self):
        return self.publish_date.strftime('%b %e %Y')