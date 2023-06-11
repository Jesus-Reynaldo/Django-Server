from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name','avatar', 'date_born','password1', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'}))
    password1 = forms.CharField(label='Create password',widget=forms.PasswordInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'}))
    password2 = forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'}))
    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'}))
    date_born = forms.DateField(widget=forms.DateInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500'}))
