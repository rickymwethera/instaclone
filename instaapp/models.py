from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse

class Image(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, null='True', blank=True)
    image = models.ImageField(upload_to = 'pics/')
    name = models.CharField(max_length=50,blank=True)	   
    caption = models.CharField(max_length=250, blank=True)	
    likes =  models.ManyToManyField(User, related_name='likes', blank=True, )
    date_posted = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    def total_likes(self):
        self.likes.count()

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


    def __str__(self):
        return self.caption

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    @classmethod
    def profile_posts(self):
        return self.image_set.all()

    def total_follows(self):
        return self.followers.count()

    def __str__(self):
        return f'{self.name.username} Profile'


class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey('Image', on_delete=models.CASCADE,related_name='comments',null='True', blank=True )
    name = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments',null='True', blank=True )
    created = models.DateTimeField(auto_now_add=True, null=True)  

    def __str__(self):
        return self.profile





