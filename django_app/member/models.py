from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    동작
        follow : 내가 다른사람을 follow함
        unfollow : 내가 다른사람에게 한 follow를 취소함

    속성
        followers : 나를 follow하고 있는 사람들
        follower : 나를 follow하고 있는 사람
        following :내가 follow하고 있는 사람들
        friend : 나와 서로 follow하고 있는 사람들
        friends : 나와 서로 follow하고 있는 모든 관계
        없음 : 내가 follow하고 있는 사람 1명
            (나는 저 사람의 follower이다 or 나는 저사람을 follow하고 있다 라고 포함)

    ex) 내가 user1,user2을 follow하고 user2,user3는 나를 follow한다
        나의 follower는 user2,user3
        나의 following은 user1
        user3는 나의 follow이다
        나는 user1의 follower다
        나와 user2는 friend관계이다
        나의 friend는 user1 한명이다.

    """
    # 이 User모델을 AUTH_USER_MODEL로 사용하도록 settings.py에 설정
    nickname = models.CharField(max_length=24, null=True, unique=True)
    following = models.ManyToManyField(
        'self',
        # through='Relation',
    ) #자기자신에게 MTM필드 설정

    def __str__(self):
        return self.nickname or self.username
        # return self.nickname if self.nickname else self.username

# class Relation(models.Model):
#     from_user = models.ForeignKey(User)
#     to_user = models.ForeignKey(User)
#     created_date = models.DateTimeField(auto_now_add=True)