from re import I
from django.contrib import admin
from .models import Imagestore
# Register your models here.
class ImagestoreAdmin(admin.ModelAdmin):
    list_display = ('image_name','category', 'modified_date')
    prepopulated_fields = {'slug': ('image_name',)}



admin.site.register(Imagestore, ImagestoreAdmin)
