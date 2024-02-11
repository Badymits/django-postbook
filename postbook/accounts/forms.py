from django import forms

from .models import Account

class LoginModelForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ['email', 'password']
        
        widgets ={
            "email": forms.TextInput(
                attrs={
                    "class": "border border-solid w-full h-[40px] rounded-lg",
                    "placeholder": "Enter email",
                    
                }
            
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "border border-solid w-full h-[40px] rounded-lg ",
                    "placeholder": "Enter password",
                }
            )
        }

class RegisterModelForm(forms.ModelForm):
    
    password2           = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "border border-solid w-full h-[40px] rounded-lg",
            "placeholder": "Confirm Password",
        }),
        label="Confirm Password",
        required=True
    )
    
    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'password2']
        
        widgets ={
            "email": forms.TextInput(
                attrs={
                    "class": "border border-solid w-full h-[40px] rounded-lg",
                    "placeholder": "Enter email",
                    
                }
            
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "border border-solid w-full h-[40px] rounded-lg ",
                    "placeholder": "Enter First Name",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "border border-solid w-full h-[40px] rounded-lg",
                    "placeholder": "Enter Username",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "border border-solid w-full h-[40px] rounded-lg",
                    "placeholder": "Enter Last Name",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "border border-solid w-full h-[40px] rounded-lg",
                    "placeholder": "Enter Password",
                }
            ),
                
        }