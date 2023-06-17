from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings

from webtoon.views import select_random_images
from.forms import CommentForm

from .models import Post, Category, Tag

import pandas as pd
import os
import numpy as np
import random

webtoon_df = pd.DataFrame()


class PostUpdate(LoginRequiredMixin, UpdateView):
    model=Post
    fields=['title','hook','content','head_image','file_upload','category','tag']

    template_name='blog/post_form_update.html'


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate,self).dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied




class PostCreate(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields=['title','hook','content','head_image','file_upload','category','tag']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self,form):
        current_user = self.request.user
        if current_user.is_authenticated: #and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')


class PostList(ListView):
    model = Post
    ordering = '-pk'
    global webtoon_df
    # 웹툰 데이터프레임 로드
    csv_file_path = os.path.join(settings.STATIC_ROOT, 'webtoon', 'webtoon0607.csv')
    webtoon_df = pd.read_csv(csv_file_path)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)





        # 군집별로 랜덤 이미지 선택
        random_images = select_random_images(webtoon_df, 5)

        context['random_images'] = random_images
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()
        context['comment_form']=CommentForm

        return context


def categories_page(request, slug):
    global webtoon_df

    category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=category)



    # 군집별로 랜덤 이미지 선택
    random_images = select_random_images(webtoon_df, 5)



    context = {
        'category' : category,
        'random_images' : random_images,
        'categories' : Category.objects.all(),
        'post_list' : post_list,
        'no_category_count' : Post.objects.filter(category=None).count(),
        #'category_count' : Post.objects.filter(category=category).count()
    }
    return render(request, 'blog/post_list.html', context)


def tag_page(request, slug):

    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context = {
        'tag' : tag,
        'categories' : Category.objects.all(),
        'post_list' : post_list,
        'no_category_count' : Post.objects.filter(category=None).count()
    }
    return render(request, 'blog/post_list.html', context)


def add_comment(request, pk):
    if not request.user.is_authenticated:
        raise PermissionError

    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        comment_temp = comment_form.save(commit=False)
        comment_temp.post = post
        comment_temp.author = request.user
        comment_temp.save()

        return redirect(comment_temp.get_absolute_url())

    else :
        raise PermissionError






