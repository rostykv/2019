from django import forms
from .models import Company, Job, Invoice

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_address']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_ref', 'job_PO', 'job_company', 'job_startdate']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_no']
