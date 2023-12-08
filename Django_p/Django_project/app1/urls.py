from django.urls import path

from . import views

urlpatterns = [
    path('blogpost/', views.blogpost_list, name='blogpost'),

]
