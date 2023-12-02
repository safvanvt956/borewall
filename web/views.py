from django.shortcuts import render,redirect,get_object_or_404
from . models import Blog, Project
from .forms import ContactForm

# Create your views here.

def index(request):
    context = {
        'is_Home' : True    
    }
    return render(request, 'web/index.html', context)


def blog(request):
    item = Blog.objects.all()
    
    context = {
        'blogs' : item,
        'is_Update' : True
    }
    return render(request,'web/blog-grid-view.html',context)


def blog_view(request,id):
    blog_post = get_object_or_404(Blog, id=id)
    
    context = {
        'item_blog' : blog_post
    }
    return render(request,'web/blog_view.html',context)


def about(request):
    context = {
        'is_About' : True
    }
    return render(request,'web/about-us.html',context)

def service(request):
    context = {
        'is_Service' : True
    }
    return render(request,'web/services-1.html',context)


def fright(request):
    context = {}
    return render(request,'web/road-fright-services.html',context)


def wares(request):
    return render(request,'web/warehousing-services.html')

def air(request):
    return render(request,'web/air-freight-services.html')

def drone(request):
    return render(request,'web/drone-delivery-services.html')

def customize(request):
    return render(request,'web/customize-brokerage.html')

def storage(request):
    return render(request,'web/consulting-storage.html')

def commercial(request):
    return render(request,'web/commercial-movers.html')

def port(request):
    pjs = Project.objects.all()
    context = {
        'project' :pjs,
        'is_Project' : True
    }
    return render(request,'web/portfolio-style.html',context)


def style_2(request,id):
    pjss = get_object_or_404(Project, id=id)
    context = {
        'pjs' : pjss
    }
    return render(request,'web/single-style-02.html',context)


def style(request):
    return render(request,'web/single-style-03.html',)


def contact(request):
    contact = ContactForm()
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect("web:contact")
                    
    context = {
        'contact': contact,
        'is_Contact' : True
    }
    return render(request,'web/contact.html',context)

    
                

