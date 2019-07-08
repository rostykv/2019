from django.contrib import admin
from .models import PaymentMethod, Company, Job, Invoice, PrimeNumber, UnorderedPrimeNumber

admin.site.register(Company)
admin.site.register(PrimeNumber)
admin.site.register(UnorderedPrimeNumber)
admin.site.register(Job)
admin.site.register(Invoice)
admin.site.register(PaymentMethod)
