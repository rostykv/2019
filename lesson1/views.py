from django.shortcuts import render, HttpResponse, redirect
from django.http import FileResponse
from .models import Company, PrimeNumber, Job, Invoice
from .primemath import *
from .forms import CompanyForm, JobForm, InvoiceForm
from django import forms
from django.views import View
from django.core.exceptions import ValidationError


def new_job(request):
    context = {}
    #import pdb; pdb.set_trace()
    if request.POST:

        if request.POST['action'] == 'delete':
            Job.objects.get(pk = request.POST['single_job']).delete()
            return redirect('accounting/jobs')

        elif request.POST['action'] == 'open_editing_form':
            f = JobForm(instance = Job.objects.get(pk = request.POST['single_job']))
            message = 'Please edit data'
            context['single_job'] = request.POST['single_job']

        elif request.POST['action'] == 'save_form':
            try:
                f = JobForm(request.POST, instance = Job.objects.get(pk=request.POST['single_job']))
                context['single_job'] = request.POST['single_job']
            except ValueError:
                import pdb; pdb.set_trace()
                f = JobForm(request.POST)
            try:
                f.save()
                f = JobForm()
                message = "Entry saved. Please enter another"
            except ValidationError:
                message = "Entry not saved. Please amend."

    else:
        f = JobForm()
        message = "Please enter data."
    context.update({'form': f, 'message': message})
    return render(request, 'lesson1/new_job.html', context)

def new_company(request):
    context = {}
    if request.POST:

        if request.POST['action'] == 'delete':
            Company.objects.get(pk = request.POST['pk']).delete()
            return redirect('/accounting/companies')

        elif request.POST['action'] == 'open_editing_form':
            f = CompanyForm(instance = Company.objects.get(pk = request.POST['pk']))
            message = "Please edit data."
            context['pk'] = request.POST['pk']

        elif request.POST['action'] == 'save_form':
            try:
                f = CompanyForm(request.POST, instance = Company.objects.get(pk = request.POST['pk']))
            except:
                f = CompanyForm(request.POST)
            if f.is_valid():
                f.save()
                f = CompanyForm()
                message = "Entry saved. You may enter another one."
            else:
                message = "Entry not saved. Please amend"

    else:
        message = "Please enter new data."
        f = CompanyForm()

    context.update({'form': f, 'message': message})
    return render(request, "lesson1/new_company.html", context)

def view_companies(request):

    context = {"companies":  Company.objects.all()   }
    return  render(request, "lesson1/view_companies.html", context)

def new_invoice(request):

    invoice_form = InvoiceForm(request.POST)
    criterion = request.POST.getlist('jobs_to_invoice')

    if invoice_form.is_valid():
        invoice_form.save()
        Job.objects.filter(id__in=criterion).update(job_invoice = invoice_form.instance.pk)
        invoice_form = InvoiceForm()

    jobs = Job.objects.all().order_by('job_company', 'job_invoice', '-job_startdate')
    context = {'jobs': jobs, 'invoice_form': invoice_form }

    return render(request, 'lesson1/view_jobs.html', context)

def view_jobs(request):

    invoice_form = InvoiceForm()
    jobs = Job.objects.all().order_by('job_company', 'job_invoice', '-job_startdate')

    context = {'jobs': jobs, 'invoice_form': invoice_form }
    return  render(request, "lesson1/view_jobs.html", context)

def home_page(request):
    return redirect('/factorization/')

def view_primes_db(request):

    if request.method == 'POST':
        if 'flushDB' in request.POST:
            PrimeNumber.objects.all().delete()
            UnorderedPrimeNumber.objects.all().delete()

        if 'downloadDB' in request.POST:
            import csv;
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="prime_numbers_list.csv"'
            writer = csv.writer(response)

            for v in consecutive_primes():
                writer.writerow([v])
            return response


    context = {'message': db_content_message()}
    return render(request, "lesson1/primes_db.html", context)

def pdf(request):
    import io
    from reportlab.pdfgen import canvas
    import pdb; pdb.set_trace()

    p = canvas.Canvas('invoice.pdf')
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()

    return FileResponse(open('invoice.pdf', 'rb'), as_attachment=True )
    
def prime_factorization(request):
    context = {}

    if request.method == 'POST':
        if 'flushDB' in request.POST:
            PrimeNumber.objects.all().delete()
            UnorderedPrimeNumber.objects.all().delete()
        if 'downloadDB' in request.POST:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
            writer = csv.writer(response)
            writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
            writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
            return response

    try:
        argument = int(request.GET['argument'])
        context['argument'] = argument
        context['factorization'] =  full_factorization(argument)
        context['newly_found_primes'] = new_primes()

    except:
        context['message1'] = db_content_message()

    return render(request, 'lesson1/factorize.html', context)

def accounting(request):

    try:
        f1 = CompanyForm(request.POST)
        f1.save()
    except:
        f1 = CompanyForm()

    context = {'form1': f1}

    return render(request, 'lesson1/accounting.html', context)
