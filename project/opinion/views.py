from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import *
from .forms import *
# Create your views here.
# p/u setari
#from django.conf import settings



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


def welcome(request):
	return render(request,"welcome.html")


def home(request):
	queryset = Article.objects.all()

	context = {
		"article_list" : queryset,
		"title" : "Welcome to UTM",
	}
	return render(request,"home.html", context)

def news(request,slug):
	instance = get_object_or_404(Article,slug=slug)
	context = {
		"article_list" : instance.title,
		"instance" : instance,
	}
	return render(request,"news.html",context)


def user(request,id):
	instance = get_object_or_404(User,id=id)
	context = {
		"instance" : instance,
	}
	return render(request,"user.html",context)

def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Welcome to UTM",
		"form" : form
	}
	return render(request,"register.html", context)

def user_edit(request,id):
	instance = get_object_or_404(User,id=id)

	form = UserChangeForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfuly edited")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"article_list" : instance.name,
		"instance" : instance,
		"form" : form, 
	}
	return render(request,"user_edit.html",context)