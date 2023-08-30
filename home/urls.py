from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index ,name='home'),
    path('home', views.index ,name='home'),
    path('about', views.about ,name='about'),
    path('contact',views.contact ,name='contact'),
    path('docs',views.docs ,name='docs'),     
    path('services',views.services ,name='services'),
    path('videos',views.display_videos ,name='videos'),
]