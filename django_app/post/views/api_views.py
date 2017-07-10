from rest_framework import generics
from rest_framework import permissions

from post.permissions import IsOwnerOrReadOnly
from ..models.post import Post
from ..serializers import PostSerializer


class Api_Post_List(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class Api_Post_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
