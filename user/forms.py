from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user
    
class VendorRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.save()
        return user
    
class AdminRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        return user
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        return user
    
class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email', max_length=100)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)