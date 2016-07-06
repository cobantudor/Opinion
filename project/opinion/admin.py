from django.contrib import admin

# Register your models here.
from .models import *

class ArticleAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp'
	readonly_fields = ('opinions',)
	empty_value_display = '-empty-'
	list_display = ('title','country','article_lang','opinions')
	list_filter = ('country','article_lang',)
	search_fields = ['title']
admin.site.register(Article,ArticleAdmin)


class UserAdmin(admin.ModelAdmin):
	empty_value_display = '-empty-'
	list_display = ('name','email')
	search_fields = ['name','email']
admin.site.register(User,UserAdmin)


class AuthorAdmin(admin.ModelAdmin):
	empty_value_display = '-empty-'
	list_display = ('user','name','email','about')
	search_fields = ['name','email']
admin.site.register(Author,AuthorAdmin)


class SubscribeAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp'
	empty_value_display = '-empty-'
	list_display = ('user','timestamp','subscribe')
admin.site.register(Subscribe,SubscribeAdmin)


class OpinionAdmin(admin.ModelAdmin):
	mpty_value_display = '-empty-'
	readonly_fields = ('upvote','downvote')
	list_display = ('id_article','opinion','id_author','upvote','downvote')
	search_fields = ['opinion']

admin.site.register(Opinion,OpinionAdmin)


class TagAdmin(admin.ModelAdmin):
	empty_value_display = '-empty-'
	list_display = ('tag_name',)
	search_fields = ['tag_name']
admin.site.register(Tag,TagAdmin)


class Tag_ArticleAdmin(admin.ModelAdmin):
	empty_value_display = '-empty-'
	list_display = ('article_id','tag_id')
	list_filter = ('tag_id',)
admin.site.register(Tag_article,Tag_ArticleAdmin)


class SettingAdmin(admin.ModelAdmin):
	empty_value_display = '-empty-'
	list_display = ('obj','attribute')
	search_fields = ['obj']
	list_filter = ('attribute',)
admin.site.register(Setting,SettingAdmin)


class ElementAdmin(admin.ModelAdmin):
	empty_value_display = '-empty-'
	list_display = ('element','lang','content')
	search_fields = ['element','content']
	list_filter = ('lang','element',)
admin.site.register(Element,ElementAdmin)