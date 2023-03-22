from django import forms
from .models import Product
from user.models import User

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'