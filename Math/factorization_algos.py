"""
GCD or GCF, greatest common denominator
Euclidean Algorithm
"""
def gcd(a,b):
    if not b:
        return a
    return gcd(b,a%b)

"""
prime factor decomposition:  Finding the prime factors of any number.
if the number itself is prime then the prime factorization is that number.
Yikes don't forget the +1 so you can get anything that is a square, such as 5 for 25, cause 5 is a prime factor of 25 and 
the square root of 25 is 5. 
"""
import math
def prime_factors(n):
    primes=set()
    while n%2==0:
        primes.add(2)
        n//=2

    for i in range(3,int(math.sqrt(n))+1,2):

        while n%i==0:
            primes.add(i)
            n//=i

    if n>2:
        primes.add(n)

    return primes