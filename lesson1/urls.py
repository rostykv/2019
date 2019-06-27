from django.urls import path, include

from . import views

factorization_patterns = [
path('' , views.prime_factorization)
]

urlpatterns = [
path('', views.home_page ),
path('factorization/', include(factorization_patterns) ),
]
