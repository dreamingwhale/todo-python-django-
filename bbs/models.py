from django.db import models

# Create your models here.
class Article(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.content
    
class User(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length = 200, null = False)

    def __str__(self):
        return self.user_name