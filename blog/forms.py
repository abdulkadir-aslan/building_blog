from django import forms
from .models import Category


class CategoryForm(forms.Form):
    title = forms.CharField(label='Kategori Ismi',max_length=20)


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','slug']