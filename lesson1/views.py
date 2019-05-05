from django.shortcuts import render, HttpResponse
from .models import Company

# Create your views here.

def prime_numbers(max):
    yield 2
    list = [2,3]
    while list[-1] < max:
        for d in list:
            prime = True
            if (d**2>list[-1]):
                break
            if (list[-1] % d == 0):
                prime = False
                break
        if prime:
            yield list[-1]
            list.append(list[-1] + 2)
        else:
            list[-1]+=1
    return


def company_list(request):

    company_list_qs = Company.objects.all()
    context = {'company_list_qs': company_list_qs}
    context = {'company_list_qs': prime_numbers(100)}
    return render(request, 'lesson1/company_list.html', context)
