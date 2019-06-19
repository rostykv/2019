from django.shortcuts import render, HttpResponse
from .models import Company, PrimeNumber
import pdb
from .primemath import *
from sys import exc_info
from itertools import chain


def company_list(request):
    context = {}
    try:
        if request.POST['cleardatabase'] == "cleardatabase":
            p = PrimeNumber.objects.all()
            p.delete()
            p = UnorderedPrimeNumber.objects.all()
            p.delete()
    except:
        pass;


    try:
        argument = int(request.GET['argument'])
        context['argument'] = argument
        context['factorization'] =  full_factorization(argument)
        context['newly_found_primes'] = new_primes()

    except:
        context['message1'] = db_content_message()

    return render(request, 'lesson1/company_list.html', context)
