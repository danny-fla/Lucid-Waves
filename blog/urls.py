from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('like-comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('like-post/<int:post_id>/', views.like_post, name='like_post'), 
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]