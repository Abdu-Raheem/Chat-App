from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ServiceRequest, ChatMessage

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_customer = forms.BooleanField(required=False)
    is_agent = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_customer', 'is_agent']


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['subject', 'description']


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']