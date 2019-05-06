from django.shortcuts import render, HttpResponse
from .models import Company

# Create your views here.

def prime_numbers(max):
    yield 1
    yield 2
    l = [2,3]
    while (l[-1] < max):
        for d in l:
            if (l[-1] % d == 0):
                l[-1]+=2
                break
            if (d**2 > l[-1]):
                yield l[-1]
                l.append(l[-1] + 2)
                break
    return


def company_list(request):

    company_list_qs = Company.objects.all()
    context = {'company_list_qs': company_list_qs}
    context = {'primes': prime_numbers(100)}
    return render(request, 'lesson1/company_list.html', context)
