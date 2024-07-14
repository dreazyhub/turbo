from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name='clientside'

urlpatterns = [
    path('', views.Home, name = 'homepage'),
    path('about/', views.About, name = 'about'),
    path('services/', views.Services, name = 'services'),
    path('track/', views.Track, name = 'track'),
    path('contact/', views.Contact, name = 'contact'),  
    path('get-a-quote/', views.Quote, name = 'get-a-quote'),  

    
]
urlpatterns += staticfiles_urlpatterns()