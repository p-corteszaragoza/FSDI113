from django.views.generic import ListView, DetailView
from .models import Article
from django.views.generic.edit import (
    CreateView, 
    UpdateView, 
    DeleteView,
) 
from django.urls import reverse_lazy

    # 1. Create our migrations
    # 2. execute those migrations
    # 3. register our model in the admin panel
    # 3.1 Create Super User account.
    # 4. Create 3 articles throught the admin panel

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailListView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleNewListView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ['title', 'body', 'author']

class ArticleUpdateListView(UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = ['title', 'body']

class ArticleDeleteListView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('articles')

