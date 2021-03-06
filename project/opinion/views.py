from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, render_to_response
from django.contrib import messages, auth
from django.core.context_processors import csrf

from .models import *
from .forms import *

#from django.conf import settings



def welcome(request):
	#if 'user' not  in request.session:
	#	request.session['guest'] = "yes"
	#	return render(request,"welcome.html")
	#else:
	#	return HttpResponseRedirect("/home")
	return render(request,"welcome.html")
	
def notfound(request):
	#if 'user' not  in request.session:
	#	request.session['guest'] = "yes"
	#	return render(request,"welcome.html")
	#else:
	#	return HttpResponseRedirect("/home")
	return render(request,"404.html")

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
		

		if exist:
			ID = User.objects.filter(email=email, password=password).values('id')
			n_id = ID[0]	
		
			request.session['user'] = "yes"
			str1 = "/user/"
			str2 = str(n_id['id'])
			str3 = str1 + str2
			request.session['userid'] = str(n_id['id'])
			#return HttpResponseRedirect(str3)
			return HttpResponseRedirect("/home")

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
	#if 'user' not  in request.session:
	#	request.session['guest'] = "yes"
	#	return render(request,"welcome.html")
	

	queryset_list = Article.objects.all().order_by("-timestamp")
	top3 = Opinion.objects.all().order_by("-upvote")[:3]

	paginator = Paginator(queryset_list, 4) 
	
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	mytags =	get_list_or_404(Tag_article)

	#sidebar 
	tops = Article.objects.all().order_by("-opinions")[:5]
	tags = Tag.objects.all()
	authors = Opinion.objects.all().order_by("-upvote")[:1]
	obj = authors[0]
	author = get_object_or_404(Author,slug=obj.id_author)
	last = Opinion.objects.all().order_by("-upvote")[:1]


	context = {
		"article_list" : queryset,
		"top3" : top3,
		"title" : "Welcome to UTM",
		"mytags" : mytags,
		"tops" : tops,
		"tags" : tags,
		"author" : author,
		"last" : last,
	}
	return render(request,"pages.html", context)




def news(request,slug):

	instance = get_object_or_404(Article,slug=slug)
	obj_id = instance
	opinions = Opinion.objects.all().filter(id_article=obj_id.id).order_by("-upvote","downvote")
	tops = Article.objects.all().order_by("-opinions")[:5]
	tags = Tag.objects.all()
	authors = Opinion.objects.all().order_by("-upvote")[:1]
	obj = authors[0]
	author = get_object_or_404(Author,slug=obj.id_author)
	last = Opinion.objects.all().order_by("-upvote")[:1]

	
	context = {
		"instance" : instance,
		"opinions" : opinions,
		"tops" : tops,
		"tags" : tags,
		"author" : author,
		"last" : last,
	}
	return render(request,"news.html",context)

def country(request,country):

	obj_list = get_list_or_404(Article,country=country)
	context = {
		"list" : obj_list,
		"country": country,
	}
	return render(request,"country.html",context)

def author(request,slug):
	obj_list = get_object_or_404(Author,slug=slug)
	id_auth = obj_list.id
	opinions = get_list_or_404(Opinion,id_author=id_auth)
	context = {
		"auth" : obj_list,
		"opinions" : opinions,
	}
	return render(request,"author.html",context)

def tag(request,tag):
	
	obj = get_object_or_404(Tag,tag_name=tag)
	obj_list = get_list_or_404(Tag_article,tag_id=obj.id)
	
	context = {
		"list" : obj_list,
		"tag" : tag,
	}
	return render(request,"tag.html",context)

def lang(request,lang):
	
	obj = get_object_or_404(Language,lang=lang)
	obj_list = get_list_or_404(Article,article_lang=obj.id)
	
	context = {
		"list" : obj_list,
		"lang" : lang,
	}
	return render(request,"lang.html",context)


def search(request):
	
	form = LoginForm(request.POST or None)
	word = request.POST.get('word','')
	
	
	articles = Article.objects.all().filter(title__contains=word)
	number1 = Article.objects.all().filter(title__contains=word).count

	opinions = Opinion.objects.all().filter(opinion__contains=word)
	number2 = Opinion.objects.all().filter(opinion__contains=word).count()

	authors = Author.objects.all().filter(name__contains=word)
	number3 = Author.objects.all().filter(name__contains=word).count()

	
	context = {
		"list1" : articles,
		"number1" : number1,
		"list2" : opinions,
		"number2" : number2,
		"list3" : authors,
		"number3" : number3,
	}
	return render(request,"search.html",context)


def user(request,id):
	query = get_object_or_404(User,id=id)
	context = {
		"query" : query,
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