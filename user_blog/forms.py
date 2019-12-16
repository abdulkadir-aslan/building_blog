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



 # tcno = forms.IntegerField(  --->>>Tc kimlik numarasi gibi belli bir rakamin altindaki ve ustundeki degerlerin girilmesi icin olusturulan fonksiyon
    #     label="Tc No Gir",
    #     min_value=10000000000,
    #     max_value=99999999999
    # )