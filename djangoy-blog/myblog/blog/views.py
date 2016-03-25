#_*_ coding:utf-8 _*_

from django.shortcuts import render, redirect

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import PostForm, LoginForm
from .models import Post

#查询所有blog并分页
def index(request, page_id=1):
    posts = Post.objects.order_by('-date')
    paginator = Paginator(posts, 2)  #实例化一个分页对象
    print page_id
    try:
        posts = paginator.page(page_id)  #获取对应页记录
    except PageNotAnInteger:  #如果页码不是整数
        posts = paginator.page(1)  #取第一页的记录
    except EmptyPage:  #如果页码太大，没有相应记录
        posts = paginator.page(page.num_pages)  #取最后一条记录
    return render(request, 'blog/index.html', {'posts': posts})


@login_required()
def edit(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['post']
            user = request.user
            date = datetime.now()
            p = Post(title=title, content=content, user=user,date=date)
            p.save()
            return redirect('index', 1)
    else:
        form = PostForm()
        print request.user
    return render(request, 'blog/edit.html', {'form': form})


def loginto(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print password
        print username
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('edit')
        else:
            return HttpResponse('Invalid user')
    else:
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
    return render(request, 'blog/login.html', 
                 {'username': username, 'password': password})
              
def logout(request):
    pass

def register(request):
    pass

