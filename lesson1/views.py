from django.shortcuts import render, HttpResponse, redirect
from .models import Company, PrimeNumber
from .primemath import *

from sys import exc_info
from itertools import chain



def home_page(request):
    return redirect('/factorization/')

def prime_factorization(request):
    context = {}
    try:
        if request.POST['flushDB']:
            PrimeNumber.objects.all().delete()
            UnorderedPrimeNumber.objects.all().delete()
    except:
        pass

    try:
        argument = int(request.GET['argument'])
        context['argument'] = argument
        context['factorization'] =  full_factorization(argument)
        context['newly_found_primes'] = new_primes()

    except:
        context['message1'] = db_content_message()

    return render(request, 'lesson1/company_list.html', context)
