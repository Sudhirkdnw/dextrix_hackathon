from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/',views.about, name= "about"),
    path('contact/',views.contact, name="contact"),
    path('service/',views.service, name="service"),
    path('project/',views.project, name="project"),
    path('team/',views.team, name="team"),
    path('card/',views.card, name="card"),
    path('testimonial/',views.testimonial, name="testimonial"),
    path('register/',views.register, name="register"),
    path('eventpage/',views.eventpage, name="eventpage"),
    path('guclub/',views.guclub, name="guclub"),
    path('op/',views.op, name="op"),
    #path('register<int:plan_id>,views.register, name="register')
    


    
]

    

