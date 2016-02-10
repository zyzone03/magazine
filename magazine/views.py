from django.shortcuts import render, redirect, get_object_or_404
from magazine.models import Article, Comment
from magazine.forms import ArticleForm, CommentForm
from django.contrib import messages

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
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.article = get_object_or_404(Article, pk=post_pk)
			comment.save()
			messages.success(request, '댓글이 등록되었습니다.')
			return redirect('magazine:article_detail', post_pk)
	else:
		form = CommentForm()
	return render(request, 'magazine/comment_new.html', {'form': form})

def comment_edit(request, post_pk, pk):
	comment = get_object_or_404(Comment, pk=pk)
	if request.method == 'POST':
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return redirect('magazine:article_detail', post_pk)
	else:
		form = CommentForm(instance=comment)
	return render(request, 'magazine/comment_new.html', {'form': form})

def comment_delete(request, post_pk, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.delete()
	return redirect('magazine:article_detail', post_pk)
