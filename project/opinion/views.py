from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages

from .models import *
from .forms import *
#from django.conf import settings



def welcome(request):
	return render(request,"welcome.html")

def about(request):
	return render(request,"about.html")

def home(request):
	if 'user' not in request.session:
		request.session['user'] = "yes"
		return HttpResponseRedirect("/welcome")
	else:
		queryset = Article.objects.all()
		context = {
			"article_list" : queryset,
			"title" : "Welcome to UTM",
		}
		return render(request,"home.html", context)


def pages(request):
	queryset_list = Article.objects.all().order_by("-timestamp")
	paginator = Paginator(queryset_list, 2) 
	
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"article_list" : queryset,
		"title" : "Welcome to UTM",
	}
	return render(request,"pages.html", context)


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
	# request.Files or None numai cind sunt fisiere
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

	form = UserChangeForm(request.POST or None, instance=instance ,)
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