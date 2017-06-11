from django.db import models
from member.models import User

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
    post_image = models.ImageField(null=True, blank=True)  # Post image
    post_content = models.TextField(null=True, blank=True)  # Post content(내용)
    post_created_date = models.DateTimeField(auto_now_add=True)  # Post 생성날짜
    post_modified_date = models.DateTimeField(auto_now=True)  # Post 수정날짜
    comments = models.ManyToManyField(Comment)
    tags = models.ManyToManyField(Tag)
    post_like = models.ManyToManyField(
        User,
        through=PostLike,
    )

    def __str__(self):
        return '{}의 포스트 : {}\n' \
               '게시일 : {}'.foramt(self.author, self.content, self.created_date)


class Comment(models.Model):
    comment_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )  # 댓글 단 사람
    comment_content = models.TextField()  # 댓글 내용
    tags = models.ManyToManyField(
        Tag
    )  # 태그

    def __str__(self):
        return '{}의 포스트 {}에 달린 댓글 {} :'.format(self.post.author,
                                               self.post.content,
                                               self.comment_content
                                               )


class PostLike(models.Model):
    postlike_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )  # 좋아요를 누른사람
    postlike_post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )  # 좋아요를 누른 게시글


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
