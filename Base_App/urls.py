from django.contrib import admin
from django.urls import path,include
from Base_App.views import Home_view,About_view,Menu_view,Book_table_view,feedback, spin_wheel

urlpatterns = [
    path('', Home_view,name="Home_view"),
    path('about/', About_view,name="About_view"),
    path('menu/', Menu_view,name="Menu_view"),
    path('bookatable', Book_table_view,name="Book_table_view"),
    path('feedback', feedback,name="feedback"),
    path('spin/', spin_wheel, name='spin_wheel'),
    
]