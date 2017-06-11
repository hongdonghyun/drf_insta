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
    author = models.ForeignKey( #작성자 User참조
        User,
        on_delete=models.CASCADE
    )
    image = models.ImageField(null=True,blank=True) # Post image
    content = models.TextField(null=True,blank=True) # Post content(내용)
    comments = models.ManyToManyField(Comment)
    tags = models.ManyToManyField(Tag)
    post_like = models.ManyToManyField(
        User,
        through=PostLike,
        related_name='post_like_by_User'
    )

    def __str__(self):
        return '{}의 포스트 : {}'.foramt(self.author,self.content)



class Comment(models.Model):
    pass


class PostLike(models.Model):
    pass


class Tag(models.Model):
    pass
