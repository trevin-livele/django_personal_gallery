from django.urls import path
from .import views
urlpatterns = [
    path('',views.imagestore, name='imagestore'),
    path('category/<slug:category_slug>/',views.imagestore, name='imagestores_by_category'),
    path('search/',views.search,name='search'),
    path('location/', views.location, name='location'),




]