from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('menu/', views.MenuPage, name='menu'),
        path('blog/', views.BlogPage, name='blog'),
        path('events/', views.EventsPage, name='events'),
        path('about/', views.AboutPage, name='about'),
        path('contact/', views.ContactPage, name='contact'),
    ]