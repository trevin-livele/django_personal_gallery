from ast import keyword
from unicodedata import category
from webbrowser import get
from django.forms import SlugField
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Imagestore,Category,Location
from django.db.models import Q
# Create your views here.



def imagestore(request,category_slug=None):
    location = Location.objects.all()
    categories = None
    image_store = None

    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        image_store = Imagestore.objects.filter(category=categories)

    else:
        image_store = Imagestore.objects.all()


    context = {
            'image_store' : image_store,
            'location'    : location,
        }
    return render(request, 'imagestore/imagestore.html', context)



def search(request):
    location = Location.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            image_store = Imagestore.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(image_name__icontains=keyword ))

    context = {
        'image_store': image_store,
        'location'    : location,
    }
    return render(request, 'imagestore/imagestore.html', context)



