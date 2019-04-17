from django.conf import settings
from django.db import models
from django.utils import timezone


class Company(models.Model):
    company_name = models.CharField(max_length=200)

    def rvsave(self):
        self.save()

    def __str__(self):
        return self.company_name
