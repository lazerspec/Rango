from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique =True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category) #Allows creation of one to many relationship
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):  #string method - printing the objects created
        return self.title