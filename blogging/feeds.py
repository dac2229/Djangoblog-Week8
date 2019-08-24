from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.shortcuts import render
from django.contrib.syndication.views import Feed
from django.urls import reverse

class LatestEntriesFeed(Feed):
    title = "My Blog RSS"
    link = "/latest/feeds"
    description = "Latest update on Blogs."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])