from django.urls import path
from .views import PostListCreate, PostListByLocation

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/location/<str:location>/', PostListByLocation.as_view(), name='post-list-by-location'),
]
