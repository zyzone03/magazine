from django.db import models
from django import forms
import re

# Create your models here.


def phone_validator(value):
	number = ''.join(re.findall(r'\d+', value))
	if not re.match(r'^01[01678]\d{7,8}$', number):
		raise forms.ValidationError('휴대폰 번호를 입력해주세요')

class PhoneField(models.CharField):
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('max_length', 11)
		super(PhoneField, self).__init__(*args, **kwargs)
		self.validators.append(phone_validator)


class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	photo = models.ImageField(blank=True)
	phone = PhoneField(max_length=20, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	article = models.ForeignKey(Article)
	message = models.CharField(max_length=100)

	def __str__(self):
		return self.message
