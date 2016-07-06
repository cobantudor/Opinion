from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	country = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	article_lang = models.CharField(max_length=50)
	opinions = models.IntegerField()

	def __str__(self):
		return self.title

class User(models.Model):
	loghin = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Author(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	about = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)

	def __str__(self):
		return  self.name
		
class Subscribe(models.Model):
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	subscribe = models.ForeignKey(Author, on_delete=models.CASCADE)
	
	
class Opinion(models.Model):
	id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
	opinion = models.TextField()
	id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
	upvote = models.IntegerField()
	downvote = models.IntegerField()


class Tag(models.Model):
	tag_name =  models.CharField(max_length=50)

	def __str__(self):
		return self.tag_name


class Tag_article(models.Model):
	article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
	tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Setting(models.Model):
	obj = models.CharField(max_length=100)
	attribute = models.CharField(max_length=100)

	def __str__(self):
		return self.obj

class Element(models.Model):
	element = models.CharField(max_length=200)
	lang = models.CharField(max_length=50)
	content = models.CharField(max_length=200)

	def __str__(self):
		return self.element