from django.shortcuts import render, HttpResponse
from .models import Company, PrimeNumber
import pdb;


newly_found_primes = []

def known_primes_list():
    l = []
    for p in PrimeNumber.objects.all():
        l.append(p.value)
    return l

def add_prime_to_db(p):
    new_prime = PrimeNumber(value = p)
    new_prime.save()
    newly_found_primes.append(p)

def eratosthenes(known_primes):
    counter = []
    d = known_primes[-1]
    for n in known_primes:
        counter.append([n, n - d % n])

    while True:
        d += 1
        prime = True
        for a in counter:
            a[1] -= 1
            if a[1] == 0:
                a[1] = a[0]
                prime = False
        if prime:
            add_prime_to_db(d)
            yield d
            counter.append([d,d])


def factorize(x):

    local_x = x
    local_known_primes = known_primes_list()

    for source in (local_known_primes, eratosthenes(local_known_primes)  ):

        for factor in source:
            power = 0
            while local_x % factor == 0:
                local_x //= factor
                power += 1
            if power: yield (factor, power)
            if local_x == 1: return
            if factor ** 2 > local_x:
                yield (local_x, 1)
                return

def company_list(request):

    try:
        argument = int(request.GET['argument'])
        context = { 'primes': factorize( argument ),
                    'argument': argument,
                    #'newly_found_primes': newly_found_primes
                    }
    except:
        context = {}
    return render(request, 'lesson1/company_list.html', context)
