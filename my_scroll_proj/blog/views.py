from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse, reverse_lazy

from .models import Post
from .forms import PostForm, CommentForm

# Create your views here.

class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'
    paginate_by = 3



class PostDetailView(FormMixin, generic.DetailView):
    template_name = 'blog/post/detail.html'
    form_class = CommentForm
    model = Post
    queryset = Post.objects.filter(status='published')

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self,).get_context_data(**kwargs)
        # It is this
        # post = get_object_or_404(Post, slug=self.kwargs['slug'])
        # OR this 
        post = self.get_object()
        context['comments'] =  post.comments.filter(active=True)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        # you must provide this attribute
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # get the new_comment contents from the user
        new_comment = form.save(commit=False)
        # attach the new_comment to a post
        new_comment.post = self.object
        new_comment.save()

        return super(PostDetailView, self).form_valid(form)


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(generic.UpdateView):
    template_name = 'blog/post/update.html'
    model = Post
    form_class = PostForm


## When you want to have a Form in a DetailView
## We can have two separate Views, one DetailView and one FormView
## and then combine them in a single view.
# class PostDetailView(generic.DetailView):
#     template_name = 'blog/post/detail.html'
#     model = Post
#     queryset = Post.objects.filter(status='published')
#
#     def get_context_data(self, **kwargs):
#         context = super(PostDetailView, self).get_context_data(**kwargs)
#         context['form'] = CommentForm()
#         return context
#
#
# class PostCommentView(SingleObjectMixin, generic.FormView):
#     template_name = 'blog/post/detail.html'
#     form_class = CommentForm
#     model = Post
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super(PostCommentView, self).post(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return reverse('blog:post_detail', kwargs={'slug': self.object.slug})
#
#
# class PostView(generic.View):
#
#     def get(self, request, *args, **kwargs):
#         view = PostDetailView.as_view()
#         return view(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         view = PostCommentView.as_view()
#         return view(request, *args, **kwargs)
#
