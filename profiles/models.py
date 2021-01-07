from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def user_directory_path(instance,filename):
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    
    return profile_pic_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(blank=True,null=True)
    web = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to=user_directory_path,blank=True,null=True,verbose_name='pictures')

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE,Image.LANCZOS)
            pic.save(self.picture.path)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()