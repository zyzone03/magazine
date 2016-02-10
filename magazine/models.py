from django.db import models

# Create your models here.


class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	photo = models.ImageField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	article = models.ForeignKey(Article)
	message = models.CharField(max_length=100)

	def __str__(self):
		return self.message
