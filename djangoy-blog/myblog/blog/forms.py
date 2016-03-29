#_*_coding:utf-8_*_

from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='标题', max_length=30)
    post = forms.CharField(label='内容', widget=forms.Textarea)

class CommentForm(forms.form):
    body = forms.CharField(max_length=20)


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=10)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
