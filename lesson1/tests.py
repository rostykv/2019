from django.test import TestCase
from .primemath import *

class TestFactorization(TestCase):

    def test_factorization(self):

        self.assertEqual( tuple( known_primes() ),  () ) #Test known_primes() for returning nothing

        b =  {1000:  ((2,3),(5,3),), 2: ((2,1),), 17: ((17,1),) , 49: ((7,2),)    }
        a = {i: tuple(full_factorization(i)) for i in b.keys() }
        self.assertEqual(b, a) #Test factorization of several numbers with empty database
        self.assertEqual(newly_found_primes, [7])

        #Test if after previous factorization the newly found primes were added to database
        self.assertEqual(tuple(known_primes()), (2,3,5,7) )

        b =  {1000:  ((2,3),(5,3),), 17: ((17,1),) , 49: ((7,2),), 2: ((2,1),)    }
        a = {i: tuple(full_factorization(i)) for i in b.keys() }
        self.assertEqual(b, a) #Test factorization of same numbers using the known primes

        self.assertEqual(newly_found_primes, [])
