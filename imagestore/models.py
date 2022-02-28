from django.db import models
from category.models import Category



# Create your models here.
class Imagestore(models.Model):
    image_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    images          = models.ImageField(upload_to='photos/products')
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.image_name


# location model
class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # save location to database
    def save_location(self):
        self.save()

    # update location
    def update_location(self, name):
        self.name = name
        self.save()

     # delete location from database
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name
