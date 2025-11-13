from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  . models import Category_items,Product
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category_items
        fields="__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','description','price','stock','category','image']


class StockForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['stock']

