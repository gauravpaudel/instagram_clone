import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

def user_directory_path(instance, filename):

    #this file will be uploaded to media_root/user_id/filename
    return 'user_{0}/{1}'.format(instance.author.id, filename)


class Tag(models.Model):
    tag = models.CharField(max_length = 100)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.tag
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        return super().save(*args,**kwargs)

class Post(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    caption = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = user_directory_path, verbose_name ='Picture', null = False )
    created_at = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(default = 0)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return '%s' % self.created_at
