from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

from .models import Post

# Create your views here.

class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'
    paginate_by = 3

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
            status='published',
            published__year=year,
            published__month=month,
            published__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
