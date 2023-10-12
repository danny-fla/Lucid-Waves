from . import views
from django.urls import path
from .views import AddPostView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('gallery/', views.gallery, name='gallery'),
    path('upload/', views.upload_image, name='upload_image'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('like-comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('like-post/<int:post_id>/', views.like_post, name='like_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]