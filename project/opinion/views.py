from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
# p/u setari
#from django.conf import settings
from django.template.defaultfilters import slugify


def welcome(request):
	#return HttpResponse("<h1>WELCOME</h1>")
	queryset = Article.objects.all()

	context = {
		"article_list" : queryset,
		"title" : "Welcome to UTM"
	}
	return render(request,"welcome.html", context)


'''
Other ways to map URL

by id
def news(request,id):
	instance = get_object_or_404(Article,id=id)
	context = {
		"article_list" : instance.title,
		"instance" : instance,
	}
	return render(request,"news.html",context)

by name
def news(request,article_title):
	instance = get_object_or_404(Article,title=article_title)
	context = {
		"article_list" : instance.title,
		"instance" : instance,
	}
	return render(request,"news.html",context)
'''


def news(request,slug):
	instance = get_object_or_404(Article,slug=slug)
	context = {
		"article_list" : instance.title,
		"instance" : instance,
	}
	return render(request,"news.html",context)

def home(request):
	return HttpResponse("<h1>Home page</h1>")