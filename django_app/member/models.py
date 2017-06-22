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
    relations = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,
    )  # 자기자신에게 MTM필드 설정

    # def follow(self, user):
    #     # 해당 user를 follow하는 Relation을 생성한다.
    #     # 이미 follow상태일 경우 행동x
    #
    #     if not isinstance(user, User):
    #         raise ValueError('"user" argument must <User> class')
    #
    #     # Relation모델의 매니저 사용
    #     Relation.objects.get_or_create(to_user=user, from_user=self)
    #
    #     # self로 주어진 User로부터 Relation의 from_user에 해당하는 RelatedManager를 사용
    #     # self.follow_relations.get_or_create(to_user=user)
    #
    #     # user로 주어진 User로부터 Relation의 to_user에 해당하는 RelatedManager를 사용
    #     # user.follower_relations.get_or_create(from_user=self)
    #
    # def unfollow(self, user):
    #     # 반대
    #     Relation.objects.filter(fromuser=self, to_user=user).delete()

    def is_follow(self, user):
        # 해당 user를 내가 follow하고 있는지 bool여부를 반환
        return self.follow_relations.filter(to_user=user).exists()

    def is_follower(self, user):
        # 해당 user가 나를 follow하고 있는지 bool여부를 반환
        return self.follow_reltations.filter(from_user=user).exists()

    def follow_toggle(self, user):
        relation, relation_created = self.follow_relations.get_or_create(to_user=user)

        if not relation_created:
            Relation.delete()

    @property
    def following(self):
        # 내가 follow중인 User QuerySet
        # return Relation.objects.filter(from_user=self)
        relations = self.follow_relations.all()
        return User.objects.filter(pk__in=relations.values('to_user'))

    @property
    def followers(self):
        # '나를 follow중인 User QuerySet'
        # return Relation.objects.filter(to_user=self)
        relations = self.follower_relations.all()
        return User.objects.filter(pk__in=relations.values('from_user'))

    def __str__(self):
        return self.nickname or self.username
        # return self.nickname if self.nickname else self.username


class Relation(models.Model):
    from_user = models.ForeignKey(User, related_name='follow_relations')
    # follow하는 사람 from_User
    to_user = models.ForeignKey(User, related_name='follower_relations')
    # follow 당하는사람 to_user
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Relation from({}) to ({})'.format(
            self.from_user,
            self.to_user
        )

    class Meta:
        unique_together = (
            ('from_user', 'to_user'),
        )  # 중복방지
