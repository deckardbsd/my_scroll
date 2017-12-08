from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

# Create your views here.

def post_list(request):
    posts_list=Post.objects.all()
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an int, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If empty page, get the last one
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
            status='published',
            published__year=year,
            published__month=month,
            published__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
