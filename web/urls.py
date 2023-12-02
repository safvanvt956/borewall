from django.contrib import admin
from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/',views.about,name='about-us'),
    path('services/',views.service,name='services-1'),
    path('projects/',views.port,name='portfolio-style'),
    path('style_2/<int:id>',views.style_2,name='single-style-02'),
    path('style_3/',views.style,name='single-style-03'),
    path('update/',views.blog,name='blog-grid-view'),
    path('blog_view/<int:id>',views.blog_view,name='blog_view'),
    path('contact/',views.contact,name='contact'),
    path('road_fright/',views.fright,name='road-fright-services'),
    path('Warehousing/',views.wares,name='warehousing-services'),
    path('air/',views.air,name='air-freight-services'),
    path('delivery/',views.drone,name='drone-delivery-services'),
    path('customize/',views.customize,name='customize-brokerage'),
    path('consulting-storage/',views.storage,name='consulting-storage'),
    path('commercial/',views.commercial,name='commercial-movers'),


]