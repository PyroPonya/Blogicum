from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Category


def get_filtered_post_queryset(**kwargs):
    """Возвращает queryset с указанными аргументами фильтрации"""
    return Post.objects.select_related(
        'category',
        'author',
        'location'
    ).filter(**kwargs)


POSTS_ON_MAIN_PAGE = 5


def index(request):
    post_list = get_filtered_post_queryset(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )[:POSTS_ON_MAIN_PAGE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_filtered_post_queryset(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__slug=category_slug
    )
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(
        get_filtered_post_queryset(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        ),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {
        'post': post,
    })
