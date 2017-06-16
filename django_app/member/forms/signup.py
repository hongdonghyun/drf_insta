from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    # SignupForm을 구성하고 해당 form을 view에서 사용하도록 설정
    username = forms.CharField(
        help_text='Signup help text test',
        widget=forms.TextInput
    )
    nickname = forms.CharField(
        help_text='Signup help text test',
        widget=forms.TextInput
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )

    # clean_<fieldname>메서드를 사용해서
    # username필드에 대한 유효성 검증을 실행
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exist'
            )
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if nickname and User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError(
                'nickname already exist'
            )
        return nickname

    # clean_<fieldname>메서드를 사용해서
    # password2필드에 대한 유효성 검증을 실행
    # 만약 password1이라고한다면 class에서 password1이 들어왔을때
    # 바로 clean메서드를 실행시키기 때문에 에러가 난다.
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Password and Password check are not equal'
            )
        return password2

    def create_user(self):
        username = self.cleaned_data['username']
        nickname = self.cleaned_data['nickname']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        return User.objects.create_user(
            username=username,
            nickname=nickname,
            password=password2
        )


