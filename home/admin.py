from django.contrib import admin
from .models import Video
from home.models import Contact
from home.models import Docs

# Register your models here.
admin.site.register(Video)
admin.site.register(Contact)
admin.site.register(Docs)
