from django.shortcuts import render
from django.http import  HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')



def about(request):

    return render(request, 'generator/about.html')

def password(request):

    letters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        letters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))


    elif request.GET.get('symbols'):
        letters.extend(list('!@#$%^&*()'))

    elif request.GET.get('numbers'):
        letters.extend(list('1234567890'))

    lenght = int(request.GET.get('lenght', 10))

    if lenght > 15:
        return HttpResponse("Больше 15 нельзя!")

    thepassword = ''

    for x in range(lenght):

        thepassword += random.choice(letters)

    return render(request, 'generator/password.html', {'password':thepassword})

