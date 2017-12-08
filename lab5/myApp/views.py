import json

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from .models import *

# Create your views here.
with open("/home/catmen/Документы/lab2_repo/lab5/myApp/static/json/goods.json") as data_file:
    goods_list = json.load(data_file)


class IndexBaseClass(View):
    @staticmethod
    def get(request):
        context = {
            "page_name": 'Магазин электроники'
        }
        return render(request, "index.html", context=context)

def product(request, product_id):
    return render(request, "product.html", context={"product" : Products.objects.get(id=product_id)})


def get_goods(request):
    return render(request, "goods.html", context={"goods" : Products.objects.all()})

def set_product(request):
    pass


class SingUpForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите ввод')
    email = forms.EmailField(label='Почта')

    # def save(self, commit=True):
    #   user = super(RegistrationForm,self).save(commit=False)
    # f
    #  return user


# class RegistrationForm(UserCreationForm):
#   helper = FormHelper()


def registration(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        else:
            print("else vailed")
    else:
        form = SingUpForm()
    return render(request, 'registration.html', {'form': form})
