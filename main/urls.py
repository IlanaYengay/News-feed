from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.get_article_by_category, name='get_article_by_category'),
    path('tag/<int:tag_id>/', views.get_article_by_tag, name='get_article_by_tag'),
    path('article/<int:pk>', views.detail_article, name= 'article_detail'),
    path('add_article/', views.add_article, name= 'add_article'),
    path('add_category/', views.add_category, name= 'add_category'),
    path('add_tags/', views.add_tags, name= 'add_tags'),
    path('article_edit/<int:pk>/', views.EditArticleVies.as_view(), name= 'edit_article'),
    path('add_comment/<int:pk>/', views.add_comment, name= 'add_comment'),
    path('delete_comment/<int:comment_id>/ <article_id>', views.delete_comment, name= 'delete_comment'),
    path('create_like/<int:pk>/', views.create_like, name= 'create_like'),
]