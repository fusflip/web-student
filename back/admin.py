from django.contrib import admin

# Register your models here.

from .models import Paper, Settings, Subject 

admin.site.register(Paper) 
admin.site.register(Settings) 
admin.site.register(Subject)