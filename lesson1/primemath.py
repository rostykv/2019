from .models import Company, PrimeNumber, UnorderedPrimeNumber
import pdb

messages = {
1: "The database contains prime numbers up to ",
2: "The database contains no prime numbers so far."
                                                    }

newly_found_primes = []

def unordered_primes():
    for p in UnorderedPrimeNumber.objects.all(): yield p.value

def new_primes():
    for p in newly_found_primes: yield p

def known_primes():
    for p in PrimeNumber.objects.all(): yield p.value

def db_content_message():
    try:
        return messages[1] + str(PrimeNumber.objects.last().value)
    except:
        return messages[2]

def eratosthenes():
    sieve = [ [n] for n in known_primes()  ]
    unordered = [ n for n in unordered_primes()]

    try: d = sieve[-1][0] # If the db of prime numbers is empty,
    except: d = 1           # the first prime number will be manually set to 2

    for n in sieve:
        n.append(n[0] - d % n[0])

    while True:
        d += 1
        try:
            unordered.remove(d)
            x = UnorderedPrimeNumber.objects.get(value = d)
            x.delete()
            sieve.append([d,d])
            add_new_prime_to_db(d)
            d += 1
            step = 2
        except:
            step = 1

        prime = True
        for a in sieve:
            a[1] -= step
            if a[1] == 0:
                a[1] = a[0]
                prime = False
        if prime:
            sieve.append([d,d])
            add_new_prime_to_db(d)
            newly_found_primes.append(d)
            yield d

def add_new_prime_to_db(p):
    new_prime = PrimeNumber(value = p)
    new_prime.save()


def add_new_unorderd_prime(p):
    new_prime = UnorderedPrimeNumber(value = p)
    new_prime.save()
    newly_found_primes.append(p)


def divide(divisible, divider):
    power = 0
    remainder = divisible
    while remainder % divider == 0:
        remainder //= divider
        power += 1
    return  (power, remainder)


def factorization(x, dividers, ordered = True):
    #This generator divides x by each of dividers and
    #yields tuples of (factor, power, remainder)
    remainder = x
    for factor in dividers:
        power, remainder = divide(remainder, factor)

        if power: #Division by a factor just completed (check factor, power, remainder)
            yield (factor, power, remainder) #Yielding factor and power and remainder
            if remainder == 1: return #This means that we have successfully factorized the input

        if ordered and (factor ** 2 > remainder):
            add_new_unorderd_prime(remainder)
            yield (remainder, 1, 1) #This means that the current remainder is the last prime factor in factorization
            return
    yield (0, 0, remainder) #This means that we have tried all the factors in dividers, but non-prime remainder still remains


def full_factorization(x):
    #This generator yields tuples (factor, power)
    #First it divides x by each of the known Primes
    #Then seeks new primes
    newly_found_primes.clear()
    for factor, power, remainder in factorization(x, known_primes() ):
        if factor:
            yield (factor, power)

    if remainder > 1: #After dividing x by all the ordered known primes, the remainder is still >1
        for factor, power, remainder in factorization(remainder, unordered_primes(), ordered = False ):
            if factor:
                yield (factor, power)

    if remainder > 1: #After dividing x by all the unordered known primes, the remainder is still >1
        for factor, power, remainder in factorization(remainder, eratosthenes()):
            yield (factor, power)#Searching for new primes
