from django.forms import ModelForm
from django import forms
from .models import *

class ChatMessagesCreateForm(ModelForm):
    class Meta:
        model=GroupMessage
        fields=['body']
        widgets={
            'body': forms.TextInput(attrs={'placeholder':'Add messages ...','class':'p-4 text black', 'maxlength':'300', 'autofocus':True})
        }