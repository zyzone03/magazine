from django import forms 
from magazine.models import Article, Comment

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = '__all__'

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['message']
		