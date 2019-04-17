from django.shortcuts import render, HttpResponse

# Create your views here.

def company_list(request):
    return render(request, 'lesson1/company_list.html', {})
