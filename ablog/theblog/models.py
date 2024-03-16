import objects
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):  # everytime we commit something this method is being called
        return reverse('ListView')

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete= models.CASCADE)
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField(blank=True,null=True,upload_to='images/')
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):  # everytime we commit something this method is being called
        return reverse('ListView')


class Post(models.Model):

    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    image_header = models.ImageField(null=True, blank=True, upload_to='images/')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):  # everytime we commit something this method is being called
        return reverse('ListView')


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment.title} and {self.name}"

