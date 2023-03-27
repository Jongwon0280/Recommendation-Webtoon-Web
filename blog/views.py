from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model=Post
    ordering = '-pk'
class PostDetail(DetailView):
    model=Post


# def index(request):
#
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

def single_post_page(request, pnum):
    post = Post.objects.get(pk=pnum)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post' : post,
        }
    )

