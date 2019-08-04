from django.urls import path, include

from . import views

factorization_patterns = [
path('' , views.prime_factorization),
path('factorize/', views.prime_factorization),
path('view/', views.view_primes_db),
path('pdf/',views.pdf)
]
accounting_patterns = [
path('', views.accounting),
path('companies/', views.view_companies),
path('jobs/', views.view_jobs),
path('invoices/', views.accounting),
path('newcompany/', views.new_company),
path('newjob/', views.new_job),
path('newinvoice/', views.new_invoice)
]


urlpatterns = [
path('', views.home_page ),
path('factorization/', include(factorization_patterns) ),
path('accounting/', include(accounting_patterns) )
]
