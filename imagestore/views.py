from django.shortcuts import render
from .models import Imagestore
# Create your views here.



def imagestore(request):
    image_store = Imagestore.objects.all()


    context = {
            'image_store' : image_store,
        }
    return render(request, 'imagestore/imagestore.html', context)