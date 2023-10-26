from . import views
from django.urls import path
from .views import AddPostView, EditPostView


urlpatterns = [
    path('', views.landing_page, name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('gallery/', views.GalleryList.as_view(), name='gallery'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('like-comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    # path('blog/<int:pk>/edit_comment/', EditCommentView.as_view(), name='edit_comment'),
    path('like-post/<int:post_id>/', views.like_post, name='like_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]