from collections import defaultdict
from numpy import gcd
import secrets


def modular_pow(base, exponent, modulus):
  if modulus == 1:
    return 0
  c = 1
  for i in range(0, exponent):
    c = (c * base) % modulus
  return c


def random_coprime_lt(n):
  coprime_nums = []
  for i in range(2, n % 16385):
    if gcd(i, n) == 1:
      coprime_nums.append(i)
  return secrets.choice(coprime_nums)


def factorize(num):
  factors = defaultdict(lambda: 0)
  fact = 2
  n = num
  half = n // 2
  while (fact <= half and n > 1):
    if n % fact == 0:
      factors[fact] += 1
      n = n // fact
    else:
      fact += 1
  if len(factors) == 0:
    return [(n, 1)]
  return [(k, v) for k, v in factors.items()]
