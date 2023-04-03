from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

# Create your views here.

class PostList(ListView):
    model=Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model=Post


def index(request):

    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )


def categories_page(request,slug):
    category = Category.objects.get(slug=slug)
    context={
            'categories' : Category.objects.all(),
            'categories_less_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
            'post_list' : Post.objects.filter(category=category)
     }
    return render(request,'blog/post_list.html',context)