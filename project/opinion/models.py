from django.db import models

from django.utils.text import slugify
from django.core.urlresolvers import reverse
# Create your models here.

class Language(models.Model):
	lang = models.CharField(max_length=20)

	def __str__(self):
		return self.lang

class Article(models.Model):
	title = models.CharField(max_length=200,unique=True)
	image = models.FileField(null=True,blank=True)
	country = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	article_lang  = models.ForeignKey(Language, on_delete=models.CASCADE)
	opinions = models.IntegerField(null=True,default=0)
	slug = models.CharField(max_length=200,unique=True,null=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)

	def __str__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse("news_page", kwargs={"slug": self.slug})
	

class User(models.Model):
	loghin = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	name = models.CharField(max_length=100)
	lang = models.ForeignKey(Language, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/user/%s/" %(self.id)
	


class Author(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	about = models.TextField()
	email = models.EmailField(max_length=100)
	slug = models.CharField(max_length=200,unique=True,null=True)
	image = models.FileField(null=True,blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Author, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return "/author/%s/" %(self.slug)

	def __str__(self):
		return  self.slug
		
class Subscribe(models.Model):
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	subscribe = models.ForeignKey(Author, on_delete=models.CASCADE)
	
	
class Opinion(models.Model):
	id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
	opinion = models.TextField()
	id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
	upvote = models.IntegerField(null=True,default=0)
	downvote = models.IntegerField(null=True,default=0)


	def get_absolute_url(self):
		return "/opinion/%s/" %(self.id)

	class Meta:
		ordering = ["-upvote","downvote"]

class Tag(models.Model):
	tag_name =  models.CharField(max_length=50)

	def __str__(self):
		return self.tag_name


class Tag_article(models.Model):
	article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
	tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

	def __str__(self):
		return self.article_id.slug


class Setting(models.Model):
	obj = models.CharField(max_length=100)
	attribute = models.CharField(max_length=100)

	def __str__(self):
		return self.obj

class Element(models.Model):
	element = models.CharField(max_length=200)
	lang = models.ForeignKey(Language, on_delete=models.CASCADE)
	content = models.CharField(max_length=200)

	def __str__(self):
		return self.element

