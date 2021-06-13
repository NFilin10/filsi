from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_pg, name='home'),
    path('about', views.about, name='kontakt'),
    path('feedback', views.feedback, name='feedback')
]