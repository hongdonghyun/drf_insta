from rest_framework import serializers

from post.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ('pk', 'photo', 'video', 'author', 'created_date', 'modified_date', 'my_comment',)
