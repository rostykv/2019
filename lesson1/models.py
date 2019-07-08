from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date

class Company(models.Model):
    company_name = models.CharField(max_length=200, unique = True, verbose_name = "Corporate name")
    company_address = models.TextField(verbose_name = 'Corporate address', blank = True)

    def __str__(self):
        return self.company_name

class Invoice(models.Model):
    invoice_no = models.CharField(max_length = 50, unique = True, verbose_name = 'Invoice No.')
    invoice_date = models.DateField(default = date.today, verbose_name = 'Invoice date')
    def __str__(self):
        return self.invoice_no


class Job(models.Model):
    job_ref = models.CharField(max_length = 50, unique = True, blank = True, null = True, verbose_name = 'My reference')
    job_PO = models.CharField(max_length = 50, verbose_name = "Client's reference")
    job_company = models.ForeignKey(Company, on_delete = models.CASCADE, verbose_name = 'Client')
    job_startdate = models.DateField(default = date.today, verbose_name = 'Start date')
    job_invoice = models.ForeignKey(Invoice, on_delete = models.CASCADE, blank = True, null = True)
    def __str__(self):
        return self.job_ref +' ('+ ('PO '+self.job_PO if self.job_PO else 'No PO specified')  +')'


class PaymentMethod(models.Model):
    method_short_name = models.CharField(max_length = 50, unique = True, verbose_name = 'Payment method')
    method_info = models.TextField(verbose_name = "Payment information")
    def __str__(self):
        return self.method_short_name



class PrimeNumber(models.Model):
    value  = models.IntegerField()

    def __str__(self):
        return self.value

class UnorderedPrimeNumber(models.Model):
    value  = models.IntegerField()

    def __str__(self):
        return self.value
