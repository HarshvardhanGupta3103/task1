from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('contact-submit/', views.contact_submit, name="contact-submit"),
   path("subscribe-newsletter/", views.subscribe_newsletter, name="subscribe_newsletter"),

]
