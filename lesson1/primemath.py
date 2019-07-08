from .models import Company, PrimeNumber, UnorderedPrimeNumber
import pdb

messages = {
1: "The database contains {0} consecutive prime numbers up to {1}.",
2: "The database contains no prime numbers so far.",
3: "The database also contains the following non-consecutive prime numbers identified by the square root rule: "
                                                    }

newly_found_primes = []

def nonconsecutive_primes():
    return [p.value for p in UnorderedPrimeNumber.objects.all()]

def new_primes():
    for p in newly_found_primes: yield p

def consecutive_primes():
    return [p.value for p in PrimeNumber.objects.all()]

def db_content_message():
    text = ''
    for p in nonconsecutive_primes():
        text += str(p)+', '
    if text:
        text = messages[3] + text[:-2]+'.'

    try:
        return messages[1].format(PrimeNumber.objects.count(), PrimeNumber.objects.last().value) +text
    except:
        return messages[2]

def new_prime_found(p):
    try:
        new_prime = PrimeNumber.objects.get(value = p)
    except:
        try:
            new_prime = UnorderedPrimeNumber.objects.get(value = p)
        except:
            newly_found_primes.append(p)

def eratosthenes():
    sieve = [ [n,] for n in consecutive_primes()  ]
    nonconsecutive = nonconsecutive_primes()


    try: d = sieve[-1][0] # If the db of prime numbers is empty,
    except: d = 1           # the first prime number will be manually set to 2

    for n in sieve:
        n.append(n[0] - d % n[0])

    while True:
        d += 1
        try:
            nonconsecutive.remove(d)
            move_from_nonconsecutive_to_consecutive(d)
            sieve.append([d,d+2])
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
            new_prime_found(d)
            add_new_prime_to_db(d)
            yield d

def add_new_prime_to_db(p):
    try:
        new_prime = PrimeNumber.objects.get(value = p)
    except:
        new_prime = PrimeNumber(value = p)
        new_prime.save()

def move_from_nonconsecutive_to_consecutive(p):
    x = UnorderedPrimeNumber.objects.get(value = p)
    x.delete()
    add_new_prime_to_db(p)
    pass;


def add_new_nonconsecutive_prime(p):
    try:
        new_prime = UnorderedPrimeNumber.objects.get(value = p)
    except:
        try:
            new_prime = PrimeNumber.objects.get(value = p)
        except:
            new_prime_found(p)
            new_prime = UnorderedPrimeNumber(value = p)
            new_prime.save()



def divide(divisible, divider):
    power = 0
    remainder = divisible
    while remainder % divider == 0:
        remainder //= divider
        power += 1
    return  (power, remainder)


def factorization(x, dividers, consecutive = True):
    #This generator divides x by each of dividers and
    #yields tuples of (factor, power, remainder)
    remainder = x
    for factor in dividers:
        power, remainder = divide(remainder, factor)

        if power: #Division by a factor just completed (check factor, power, remainder)
            yield (factor, power, remainder) #Yielding factor and power and remainder
            if remainder == 1: return #This means that we have successfully factorized the input

        if consecutive and (factor ** 2 > remainder):
            add_new_nonconsecutive_prime(remainder)
            yield (remainder, 1, 1) #This means that the current remainder is the last prime factor in factorization
            return
    yield (0, 0, remainder) #This means that we have tried all the factors in dividers, but non-prime remainder still remains


def full_factorization(x):
    #This generator yields tuples (factor, power)
    #First it divides x by each of the known Primes
    #Then seeks new primes
    newly_found_primes.clear()
    for factor, power, remainder in factorization(x, consecutive_primes() ):
        if factor:
            yield (factor, power)

    if remainder > 1: #After dividing x by all the ordered known primes, the remainder is still >1
        for factor, power, remainder in factorization(remainder, nonconsecutive_primes(), consecutive = False ):
            if factor:
                yield (factor, power)

    if remainder > 1: #After dividing x by all the unordered known primes, the remainder is still >1
        for factor, power, remainder in factorization(remainder, eratosthenes()):
            yield (factor, power)#Searching for new primes
