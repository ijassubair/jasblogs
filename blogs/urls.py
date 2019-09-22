from django.urls import path

from blogs import views

urlpatterns = [
    path('', views.home, name='blogs'),
    path('<slug:title>/', views.blog, name='blog'),
]