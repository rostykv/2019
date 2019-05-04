from django.shortcuts import render, HttpResponse
from .models import Company

# Create your views here.

def company_list(request):
    company_list_qs = Company.objects.all()
    context = {'company_list_qs': company_list_qs}
    return render(request, 'lesson1/company_list.html', context)
