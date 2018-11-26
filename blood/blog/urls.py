from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views
urlpatterns = [
    path('', views.home , name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
    path('donors/', views.donors, name='blog-donors'),
    path('list/', views.ListEnrolled, name = 'doner-list')
]