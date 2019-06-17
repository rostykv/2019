from django.shortcuts import render, HttpResponse
from .models import Company, PrimeNumber
import pdb
from .primemath import *
from sys import exc_info
from itertools import chain


def company_list(request):
    context = {}
    import pdb; pdb.set_trace()
    try:
        argument = int(request.GET['argument'])
        context['argument'] = argument
        context['factorization'] =  full_factorization(argument)
        context['newly_found_primes'] = new_primes()

    except:
        context['message1'] = db_content_message()

    return render(request, 'lesson1/company_list.html', context)
