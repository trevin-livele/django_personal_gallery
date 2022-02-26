from django.shortcuts import render

from imagestore.models import Imagestore

def home(request):
    image_store = Imagestore.objects.all()


    context = {
        'image_store' : image_store,
    }
    return render(request,'home.html',context)












def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')