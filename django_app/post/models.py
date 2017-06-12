from django.db import models
from django.contrib.auth.models import User

"""
member application 생성
    User모델 구현
        username,nickname
이후 해당 user모델을 Post나 Comment에서 author나 user항목으로 참조
"""


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(  # 작성자 User참조
        User,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(null=True, blank=True)  # Post image
    content = models.TextField(null=True, blank=True)  # Post content(내용)
    created_date = models.DateTimeField(auto_now_add=True)  # Post 생성날짜
    modified_date = models.DateTimeField(auto_now=True)  # Post 수정날짜
    tags = models.ManyToManyField('Tag')
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts',
        # through='PostLike',

    )

    def __str__(self):
        return '{}의 포스트 : {}\n' \
               '게시일 : {}'.foramt(self.author,
                                 self.content,
                                 self.created_date
                                 )


class Comment(models.Model):
    post = models.ForeignKey('Post')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )  # 댓글 단 사람
    content = models.TextField()  # 댓글 내용
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}의 포스트 {}에 달린 댓글 {} :'.format(self.post.author,
                                               self.post.content,
                                               self.comment_content
                                               )


class PostLike(models.Model):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
