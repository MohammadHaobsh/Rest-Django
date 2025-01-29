from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# عرض قائمة المقالات (GET) وإنشاء مقالة جديدة (POST)
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# عرض مقالة واحدة (GET)، تحديث مقالة (PUT)، حذف مقالة (DELETE)
class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
