import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), 
    label=_  ("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and          underscores.") })
    phonenumber = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30,      render_value=False)),      label=_("phonenumber"))
     
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30,      render_value=False)),      label=_("password"))
     
    
