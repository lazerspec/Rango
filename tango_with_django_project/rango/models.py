from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category) #Allows creation of one to many relationship
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):  #string method - printing the objects created
        return self.title

class UserProfile(models.Model):
    #Line required. Links profile to user model
    user = models.OneToOneField(User) #default value of 0

    #Additional attributes we wish to include
    website = models.URLField(blank=True) #blank means user does not need to provide these
    picture = models.ImageField(upload_to='profile_images', blank=True)

    #Override the __unicode__() method to return something meaningful
    def __str__(self):
        return self.user.username