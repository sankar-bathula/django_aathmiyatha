from django.urls import path
from aathmiyatha.views import *

urlpatterns = [
	path('', PostListView.as_view(), name='amf-home'),
	path('home/', index_home, name='amf-home-index'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='amf-about'),
]
