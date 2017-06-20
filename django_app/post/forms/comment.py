from django import forms

from django.contrib.auth import get_user_model

from ..models import Comment, Post

User = get_user_model()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'input-comment',
                    'placeholder': '댓글 입력',

                }
            )
        }

    def save(self, **kwargs):
        commit = kwargs.get('commit', True)
        author = kwargs.pop('author', None)
        post = kwargs.pop('post', None)

        if author is None:
            author = self.instance.author
        else:
            self.instance.author = author

        if isinstance(post, Post):
            self.instance.post = post

        comment_string = self.cleaned_data['content']
        if commit and comment_string:
            instance = Comment.objects.create(
                post=self.instance.post,
                author=self.instance.author,
                content=comment_string
            )
        else:
            instance = Comment.objects.get(pk=post.pk)
            instance.content = comment_string
        instance.save()

        return instance