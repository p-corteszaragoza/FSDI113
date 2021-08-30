from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.http import request
from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from .models import Article
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

    # 1. Create our migrations
    # 2. execute those migrations
    # 3. register our model in the admin panel
    # 3.1 Create Super User account.
    # 4. Create 3 articles throught the admin panel

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailListView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleCreateListView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ['title','body',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateListView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteListView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('articles')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user