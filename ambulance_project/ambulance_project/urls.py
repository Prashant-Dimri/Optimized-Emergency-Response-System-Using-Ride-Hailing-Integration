from django.contrib import admin
from django.urls import path
from emergency import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home'),
    path('emergency/', views.get_location, name='get_location'),  
    path('send-location/', views.send_location, name='send_location'),
]
