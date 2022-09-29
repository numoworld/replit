from utils import modular_pow


def encrypt(pk, m):
  e, n = pk
  return modular_pow(m, e, n)


def decrypt(sk, c):
  d, n = sk
  return modular_pow(c, d, n)
