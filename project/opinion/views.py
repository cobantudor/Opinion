from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, render_to_response
from django.contrib import messages, auth
from django.core.context_processors import csrf

from .models import *
from .forms import *

#from django.conf import settings



def welcome(request):
	request.session['guest'] = "yes"
	return render(request,"welcome.html")

def login(request):
	if 'user' not in request.session:
		form = LoginForm(request.POST or None)

		email = request.POST.get('email','')
		password = request.POST.get('password','')
		exist = User.objects.filter(email=email, password=password).exists()
		
		if(email != ''):
			check = 1
		else:
			check = 0
		
		print(check)

		if exist:
			ID = User.objects.filter(email=email, password=password).values('id')
			n_id = ID[0]	
		
			request.session['user'] = "yes"
			str1 = "/user/"
			str2 = str(n_id['id'])
			str3 = str1 + str2
			request.session['userid'] = str(n_id['id'])
			return HttpResponseRedirect(str3)
			
		else:
			context = {
			"form" : form,
			"check" : check
			}
			return render(request,"login.html",context)

	else:
		return HttpResponseRedirect("/home")


def logout(request):
	if 'user' in request.session:
		del request.session['user']
		del request.session['userid']
	return  HttpResponseRedirect("/login")


def home(request):
	if 'guest' not in request.session:
		
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