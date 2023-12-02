from django.contrib import admin
from . models import Blog, Contact, Project

# Register your models here.

admin.site.register(Project)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name' , 'title', 'image', 'contact')

@admin.register(Contact)
class ContactfmAdmin(admin.ModelAdmin):
    list_display = ('fullname','lastname','email','phone','message')
    

    
    

