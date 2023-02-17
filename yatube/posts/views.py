from django.shortcuts import render, get_object_or_404

from .models import Post, Group


LAST_POSTS = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:LAST_POSTS]
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug_name):
    group = get_object_or_404(Group, slug=slug_name)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:LAST_POSTS]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
