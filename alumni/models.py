from django.db import models
from django.contrib.auth.models import User
from django_markdown.models import MarkdownField
# Create your models here.


class Alumni(models.Model):

    CHOICES = (('YES', True),
              ('No', False)
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollno = models.CharField(max_length = 9)
    batch = models.CharField(max_length = 4)

    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profile_pic', blank=True)
    cover_pic = models.ImageField(upload_to='cover_pic', blank=True)

    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    clubs = models.CharField(max_length = 300, blank=True)
