from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name='AdminSide'

urlpatterns = [
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('order-list/',views.OrderList, name='order-list'),
    path('new-order/',views.NewOrder, name='new-order'),
    path('update-order/<str:pk>/',views.updateOrder, name='update-order'),
    path('details/<str:pk>/', views.details, name = 'details'),
    path('delete/<str:pk>/', views.deleteorder, name='delete-order'),
    path('', views.loginUser, name='login'),
     path('alllmessages/',views.Allmessages, name='all-messages'),
     path('message-details/<str:pk>/', views.messageDetails, name = 'message-details'),



  
    
]
urlpatterns += staticfiles_urlpatterns()