from utils import factorize
from numpy import lcm


def euler(n):
  factors = factorize(n)
  result = 1
  for num, deg in factors:
    result *= num**deg - num**(deg - 1)
  return result


def carmichael(n):
  factors = factorize(n)
  lambdas = []
  for num, deg in factors:
    if (num == 2 and deg >= 3):
      lambdas.append(euler(num**deg) // 2)
    lambdas.append(euler(num**deg))
  return int(lcm.reduce(lambdas))
