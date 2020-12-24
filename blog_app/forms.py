from django import forms
from django.db.models import fields
from django.forms import widgets
# from .models import test

# Using model.py

from django.db.models.fields import TextField
from django.forms.widgets import PasswordInput
from .models import Post

# ModelForm allows us to create form fields
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = { 
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }



# creating a form without model.py
# class InputForm(forms.Form):

#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     roll_number = forms.IntegerField(help_text="enter 6 digit roll number")
#     # password = forms.CharField(widget = forms.PasswordInput())
#     password = forms.CharField(widget=forms.PasswordInput())


# Creating a form with models.py

# class InputForm(forms.ModelForm):
#     class Meta:
#         templates = "test.html"
#         model = test

#         # fields = ('first_name', 'last_name', 'roll_numnber', 'password')
#         fields = "__all__"

#         widgets = {
#             # 'first_name' : ,
#             # 'last_name' : ,
#             # 'roll_numnber' : ,
#             'password' : forms.PasswordInput(),
#         }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
