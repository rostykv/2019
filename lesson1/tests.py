from django.test import TestCase
from .primemath import *
from .forms import *
from .models import *

class TestAccounting(TestCase):
    def test_accounting(self):
        data = {'company_name': 'Cetadir', 'company_country' : "France"}
        f = CompanyForm(data)
        if f.is_valid():
            m = Company()
            m.save()
        import pdb; pdb.set_trace()

        pass;


class TestFactorization(TestCase):

    def test_factorization(self):

        self.assertEqual( tuple( consecutive_primes() ),  () ) #Test consecutive_primes() for returning nothing

        self.assertEqual( tuple( full_factorization(2) ),  ((2,1),) )
        self.assertEqual(newly_found_primes, [2,])
        self.assertEqual(tuple(consecutive_primes()), (2,) )
        self.assertEqual(tuple(nonconsecutive_primes()), () )

        self.assertEqual( tuple( full_factorization(3) ),  ((3,1),) )
        self.assertEqual(newly_found_primes, [3,])
        self.assertEqual(tuple(consecutive_primes()), (2,) )
        self.assertEqual(tuple(nonconsecutive_primes()), (3,) )

        self.assertEqual(tuple(full_factorization(6)), ((2,1),(3,1),)) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [])
        self.assertEqual(tuple(consecutive_primes()), (2,) )
        self.assertEqual(tuple(nonconsecutive_primes()), (3,) )

        self.assertEqual(tuple(full_factorization(100)), ((2,2),(5,2),)) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [5,])
        self.assertEqual(tuple(consecutive_primes()), (2,3,5) )
        self.assertEqual(tuple(nonconsecutive_primes()), () )

        self.assertEqual(tuple(full_factorization(72)), ((2,3),(3,2),)) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [])
        self.assertEqual(tuple(consecutive_primes()), (2,3,5) )
        self.assertEqual(tuple(nonconsecutive_primes()), () )


        self.assertEqual(tuple(full_factorization(17)), ((17,1),)) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [17,])
        self.assertEqual(tuple(consecutive_primes()), (2,3,5) )
        self.assertEqual(tuple(nonconsecutive_primes()), (17,) )


        self.assertEqual(tuple(full_factorization(16)), ((2,4),)) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [])
        self.assertEqual(tuple(consecutive_primes()), (2,3,5) )
        self.assertEqual(tuple(nonconsecutive_primes()), (17,) )


        self.assertEqual(tuple(full_factorization(49)), ((7,2),)) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [7])
        self.assertEqual(tuple(consecutive_primes()), (2,3,5,7) )
        self.assertEqual(tuple(nonconsecutive_primes()), (17,) )

        b =  {1000:  ((2,3),(5,3),), 17: ((17,1),) , 49: ((7,2),), 2: ((2,1),)    }
        a = {i: tuple(full_factorization(i)) for i in b.keys() }
        self.assertEqual(b, a) #Test factorization of same numbers using the known primes
        self.assertEqual(tuple(consecutive_primes()), (2,3,5,7)
        )
        self.assertEqual(tuple(nonconsecutive_primes()), (17,) )
        self.assertEqual(newly_found_primes, [])
        self.assertEqual(tuple( consecutive_primes() ),  (2,3,5,7) )
        self.assertEqual(tuple( nonconsecutive_primes() ),  (17,) )


        self.assertEqual(tuple(full_factorization(289)), ((17,2),)) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [])
        self.assertEqual(tuple( consecutive_primes() ),  (2,3,5,7) )
        self.assertEqual(tuple( nonconsecutive_primes() ),  (17,) )

        self.assertEqual(tuple(full_factorization(361)), ((19,2),)) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [11,13,19,])
        self.assertEqual(tuple( consecutive_primes() ),  (2,3,5,7,11,13,17,19) )
        self.assertEqual(tuple( nonconsecutive_primes() ),  () )
