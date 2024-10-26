from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from datetime import datetime

from blog.models import Post, Category


def index(request):
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=datetime.now(),
        category__is_published=True
    ).order_by('-pub_date')[0:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.all().filter(
        slug=category_slug,
    ), is_published=True)
    posts = Post.objects.select_related(
        'category').filter(
            is_published=True,
            pub_date__lte=datetime.now(),
            category__slug=category_slug
    )
    print('CATEGORIES: ', category)
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related('category').filter(pk=post_id),
        pub_date__lte=datetime.now(),
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {
        'post': post,
    })
