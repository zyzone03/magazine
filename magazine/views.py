from django.shortcuts import render
from magazine.models import Article

# Create your views here.
def index(request):
	return render(request, 'magazine/index.html', {})

def article_list(request):
	article_list = Article.objects.all()
	return render(request, 'magazine/article_list.html', {
			'article_list': article_list
		})

def article_detail(request, pk):
	article = Article.objects.get(pk=pk)
	return render(request, 'magazine/article_detail.html',{
			'article': article
		})