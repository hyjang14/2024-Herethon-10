from django import forms
from accounts.models import User


# 커스텀 유저
class CustomUserForm(forms.ModelForm):
    profile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'hidden-file-input'}))
    class Meta:
        model = User
        fields = ['profile', 'username', 'password', 'email', 'name', 'phone', 'birthdate']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'userid-input',
                'placeholder': '아이디를 6자 이상 입력해주세요.',
            }),
            'email': forms.TextInput(attrs={
                'class': 'email-input',
                'placeholder': '예) rlfhvm@gmail.com',
            }),
            'password': forms.TextInput(attrs={
                'class': 'password-input',
                'placeholder': '비밀번호를 8자 이상 입력해주세요.',
            }),
            'name': forms.TextInput(attrs={
                'class': 'name-input',
                'placeholder': '예) 기로프',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'phone-input',
                'placeholder': '예) 01012345678',
            }),
            'birthdate': forms.TextInput(attrs={
                'class': 'birthdate-input',
                'placeholder': '예) 2000-01-01',
            }),
            'profile': forms.FileInput(attrs={
                'class': 'profile-input',
                'id': 'profile-input',
                'style': 'display:none;'
            }),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 비밀번호 해싱하기
        if commit:
            user.save()
        return user

# 커스텀 유저 업데이트    
class CustomUserUpdateForm(forms.ModelForm):
    profile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'hidden-file-input clearable-file-input'}))
    class Meta:
        model = User
        fields = ['profile', 'username', 'email', 'name', 'phone', 'birthdate']
    

