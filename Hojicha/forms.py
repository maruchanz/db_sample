from django import forms 
from .models import products
from django.contrib.auth.forms import (
    AuthenticationForm
)

class ProductsForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ('product_name', 'price','media_data','URL')

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            #なにこれ？
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
