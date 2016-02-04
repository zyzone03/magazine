from django.shortcuts import render, redirect
from magazine.models import Article
from magazine.forms import ArticleForm

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

def article_new(request): 
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save()
			return redirect('magazine:article_detail', article.pk)
	else:
		form = ArticleForm()
	return render(request, 'magazine/article_new.html', {'form': form})

def article_edit(request, pk): 
	form = Article.objects.get(pk=pk)
	if request.method == 'POST':
		form = ArticleForm(request.POST, instance=form)
		if form.is_valid():
			article = form.save()
			return redirect('magazine:article_detail', article.pk)
	else:
		form = ArticleForm(instance=form)
	return render(request, 'magazine/article_new.html', {'form': form})

def article_delete(request, pk):
	form = Article.objects.get(pk=pk)
	form.delete()
	return redirect('magazine:article_list')

def comment_new(request, post_pk):
	article = Article.objects.get(post_pk=post_pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save()
			return redirect('magazine:article_detail', article.post_pk)
	else:
		form = CommentForm()
	return render(request, 'magazine/comment_new.html', {'form': form})


