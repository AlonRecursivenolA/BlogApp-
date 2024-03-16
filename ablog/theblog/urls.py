
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',HomeListView.as_view(),name="ListView"),
    path('Article/<int:pk>',HomeDetailView.as_view(),name="article-details"),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category',AddCategoryView.as_view(),name='add-category'),
    path('Article/edit/<int:pk>/',UpdateTheView.as_view(),name='edit-post'),
    path('Article/delete/<int:pk>',DeleteTheView.as_view(),name='delete-post'),
    path('category/<str:cats>',CategoryView,name='categories'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('Article/<int:pk>/comment/', CreateCommentView.as_view(),name='add_a_comment'),
    # path('test',views.home,name="home"),

]
