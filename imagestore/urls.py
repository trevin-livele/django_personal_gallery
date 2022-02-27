from django.urls import path
from .import views
urlpatterns = [
    path('',views.imagestore, name='imagestore'),
    path('<slug:category_slug>/',views.imagestore, name='imagestores_by_category'),



]