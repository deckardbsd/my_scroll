from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
    )
    title = models.CharField(_('Title'), max_length=250)
    slug = models.SlugField(_('Slug'), max_length=250, unique_for_date='published')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-published', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('blog:post_detail', args=[self.pk])
        return reverse('blog:post_detail', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', )

        def __str__(self):
            return 'Comment by {} on {}'.format(self.name, self.post)
