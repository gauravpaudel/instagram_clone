from django.db import models

class Post(models.Model):
    caption = models.CharField(max_length = 100)
    
