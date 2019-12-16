from django import forms


class LoginForm(forms.Form):
    username = forms.EmailField(
        label='kullanici Adi'
        ,max_length=50,
    )
    password = forms.CharField(
        label='Parolanizi Giriniz',
        max_length=50,
        widget=forms.PasswordInput()
    )