from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('view_All_Customer/', views.viewAllCustomer, name='viewallcustomer'),    
    path('transfer_money/', views.transaction, name='transfer'),  
    path('transfer_details/', views.transferDetails, name='transferdetails'),     
       
     
        
]
