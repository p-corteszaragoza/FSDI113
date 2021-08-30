from django.urls import path 
from .views import (
    ArticleListView, 
    ArticleDetailListView, 
    ArticleCreateListView,
    ArticleUpdateListView,
    ArticleDeleteListView,
)

# 1. Create an article detail view.
# 2. Create an article create view.
# 3. Create an article update view.
# 4. Create an article delete view.
# 5. Create urlpatterns to map to all of our views.
# To view an article's detail, we're going to: /articles/<int:pk>/
# To create an article we're going to go to: /articles/new/
# To update an article: /articles/<int:pk>/update/
# To delete an article: /articles/<int:pk>/delete/
urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('<int:pk>/', ArticleDetailListView.as_view(), name="article_detail"),
    path('new/', ArticleCreateListView.as_view(), name="article_new"),
    path('<int:pk>/update/', ArticleUpdateListView.as_view(), name="article_update"),
    path('<int:pk>/delete/', ArticleDeleteListView.as_view(), name="article_delete"),
]
