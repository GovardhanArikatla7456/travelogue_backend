from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListByLocation(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        location = self.kwargs['location']
        return Post.objects.filter(location__iexact=location)
