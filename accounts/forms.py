from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserBankAccount,Deposite
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistreationForm(UserCreationForm):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'required'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

    def save(self,commit=True):
        user=super().save(commit=False)
        if commit:
            user.save()
            account_no=10000+user.id
            UserBankAccount.objects.create(user=user,account_no=account_no)
        return user
    
class DepositeForm(forms.ModelForm):
    class Meta:
        model=Deposite
        fields=['amount']

    def __init__(self,*args,**kwargs):
        self.account=kwargs.pop('account')
        super().__init__(*args,**kwargs)

    def save(self,commit=True):
        self.instance.account=self.account
        return super().save()
    def clean_amount(self):
        min_diposite_amount=100
        amount=self.cleaned_data.get('amount')
        if amount < min_diposite_amount:
            raise forms.ValidationError(
                f'you need to deposite minimum {min_diposite_amount} $'
            )
        return amount




        