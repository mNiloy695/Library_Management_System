from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from  django.views.generic import CreateView
from .forms import RegistreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DepositeForm
from .models import Deposite
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

def send_mail(user,subject,type,book):
        mail_subject=subject
        message=render_to_string('mail.html',{
            'user':user,
            'type':type,
            'book':book
        })
        user_mail=user.email
        mail=EmailMultiAlternatives(mail_subject,'',to=[user_mail])
        mail.attach_alternative(message,'text/html')
        mail.send()
class RegistrationView(CreateView):
    model=User
    form_class=RegistreationForm
    template_name='signup.html'
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        messages.success(self.request,f'Your account Successfully Created')
        return super().form_valid(form)
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['type']='Registration'
        return context

class UserLoginView(LoginView):
    template_name='signup.html'
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self,form):
        messages.success(self.request,'your successfully login')
        return super().form_valid(form)
    def form_invalid(slef,form):
        messages.warning(slef.request,'Please Enter the correct information')
        return super().form_invalid(form)
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['type']='Login'
        return context 
    
class UserLogoutView(LoginRequiredMixin,LogoutView):
    model=User
    def get_success_url(self):
        return reverse_lazy('home')
    

class DeposteView(LoginRequiredMixin,CreateView):
    model=Deposite
    form_class=DepositeForm
    template_name='signup.html'
    success_url=reverse_lazy('home')
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update(
            {'account':self.request.user.account}
        )
        return kwargs
    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance+=amount
        account.save(
            update_fields=[
                'balance'
            ]
        )
        messages.success(self.request,f'you {amount}$ Deposite successflly')
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Deposite Money'
        return context

    