from django.shortcuts import render, get_object_or_404
from .models import Post, Group

number_last_posts = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:number_last_posts]
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug_name):
    group = get_object_or_404(Group, slug=slug_name)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:number_last_posts]
    title = "Здесь будет информация о группах проекта Yatube"
    template = 'posts/group_list.html'
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
