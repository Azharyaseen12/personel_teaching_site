from django.shortcuts import render,HttpResponse
from .models import Video
from datetime import  datetime 
from home.models import Contact
from home.models import Docs
from django.contrib import messages


def index(request):
         videos = Video.objects.all()
         print(videos)
         return render(request, 'index.html', {'videos': videos})
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html',)

def display_videos(request):
     videos = Video.objects.all()
     return render(request, 'videos.html', {'videos': videos})

def about(request):
    return render(request, 'about.html',)

def services(request):
    return render(request, 'videos.html',)  

def docs(request):
    docs = Docs.objects.all()
    return render(request, 'docs.html', {'docs': docs})           
               
# Create your views here.
