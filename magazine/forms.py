from django import forms
from magazine.models import Article, Comment


class ArticleForm(forms.ModelForm):
    is_agree = forms.BooleanField(label='약관동의',
        error_messages={'required': '동의하셔야 이용 가능합니다'})

    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
