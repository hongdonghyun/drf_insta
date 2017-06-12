from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

# User모델을 AUTH_USER_MODEL로 사용하도록 settings.py에 설정
