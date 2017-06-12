from django.conf import settings
from django.db import models


"""
member application 생성
    User모델 구현
        username,nickname
이후 해당 user모델을 Post나 Comment에서 author나 user항목으로 참조
"""


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(  # 작성자 User참조
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(null=True, blank=True)  # Post image
    created_date = models.DateTimeField(auto_now_add=True)  # Post 생성날짜
    modified_date = models.DateTimeField(auto_now=True)  # Post 수정날짜
    tags = models.ManyToManyField('Tag')
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_posts',
        through='PostLike',



    )
    @property
    def like_count(self):
        return self.like_users.count()

    def add_comment(self, user, content):
        # 자신을 post로 갖고 전달받은 user를 author로 가지며
        # content를 content필드내용으로 넣는 Comment 객체 생성
        self.comment_set.create(author=user, content=content)

    def add_tag(self, tag_name):
        # tags에 tag매개변수로 전달된 값(str)을
        # name으로 갖는 Tag객체를 (존재한다면)가져오고 없으면 생성하여
        # 자신의 tags에 추가
        tag, tag_created = Tag.objects.get_or_create(name=tag_name)
        if self.tags.filter(name=tag_name).exitsts():#id=tag.id
            self.tags.add(tag)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )  # 댓글 단 사람
    content = models.TextField()  # 댓글 내용
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='CommentLike',
        related_name='like_comments'
    )


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    comment =models.ForeignKey(Comment)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)
