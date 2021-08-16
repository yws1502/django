from django.contrib.auth.models import User
from django import forms

# 폼 : 폼태크 -> HTML의 태그 -> front에서 사용자의 입력을 받는 인터페이스
# 장고의 폼 : HTML의 폼 역할, 데이터베이스에 저장할 내용을 형식, 제약조건
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # 보통 뒤쪽에 필드명이 들어오면 해당 필드에 대한 validation은 어떻게 할것인지!
    def clean_password2(self):
        cd = self.cleaned_data # dictionary
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched')
        return cd['password2']