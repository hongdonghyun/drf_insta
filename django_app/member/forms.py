from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '아이디'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호'
            }
        )
    )
    #is_valid를 실행했을 때 Form내부의 모든 field들에 대한
    #유효성 검증을 실행하는 메서드

    def clean(self):
        # clean()메서드를 실행한 기본결과 dict를 가져옴
        cleaned_data = super().clean()
        # username,password를 가져와 로컬변수에 할당
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        #username ,password를 이용해 사용자 authenticate
        user = authenticate(
            username=username,
            password=password
        )
        #인증에 성공할 경우 form의 cleaned_date의 'user'
        #키에 인증된 User객체를 할당
        if user is not None:
            self.cleaned_data['user'] = user
        #인증에 실패할 경우, is_valid()를 통과하지 못하도록
        #VailiddationError를 발생시킴
        else:
            raise forms.ValidationError(
                'Login credentials not invalid'
            )
        return self.cleaned_data
