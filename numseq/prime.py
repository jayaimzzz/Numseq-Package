'''
Prime: can return a list of primes or test if a number is prime.
'''

__author__ = 'jayaimzzz'

def primes(n):
    return [i for i in range(1,n) if is_prime(i)]

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True