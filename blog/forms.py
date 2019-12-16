from django import forms


class CategoryForm(forms.Form):
    title = forms.CharField(label='Kategori Ismi',max_length=20)

