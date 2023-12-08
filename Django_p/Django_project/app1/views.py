from django.http import HttpResponse
from django.shortcuts import render

from .models import Blog


def blogpost_list(request):
    blogposts = {'blogposts': Blog.objects.order_by('-date')}
    return render(request, 'blogpost.html', blogposts)
