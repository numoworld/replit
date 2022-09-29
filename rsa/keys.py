import secrets

from utils import random_coprime_lt
from totient_funcs import euler, carmichael
from prime_numbers import prime_numbers
from numpy import gcd


def generate_key_pair():

  # choose random prime numbers
  p = secrets.choice(prime_numbers)
  q = secrets.choice(prime_numbers)

  # make sure they are not the same
  while p == q:
    q = secrets.choice(prime_numbers)

  # calculate n
  n = p * q

  # calculate lambda(n)
  lambda_n = carmichael(n)
  # lambda_n = euler(n)

  # get random e (it is prime, so it's automatically coprime with lamda(n))
  e = random_coprime_lt(lambda_n)

  # calculate modular multiplicative inverse
  d = pow(e, -1, lambda_n)

  # generate key pair
  pk = e, n
  sk = d, n

  return pk, sk
