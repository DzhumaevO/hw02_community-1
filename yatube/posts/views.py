from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Group, Post, User


LAST_POSTS = 10
NUMBER_OF_POSTS = 10


def index(request):
    # posts = Post.objects.all()[:LAST_POSTS]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, NUMBER_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        # 'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug_name):
    group = get_object_or_404(Group, slug=slug_name)
    posts = group.posts.all()[:LAST_POSTS]
    template = 'posts/group_list.html'
    post_list = group.posts.all()
    paginator = Paginator(post_list, NUMBER_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post\
        .objects\
        .select_related('group')\
        .filter(author__username=username)
    paginator = Paginator(posts, NUMBER_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        "author": author,
        'posts': posts
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_id = Post.objects.filter(author__posts=post_id)
    context = {
        'post_id': post_id,
        'author': post.author,
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)
