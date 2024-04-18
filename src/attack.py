"""
attack.py
- Try to attack and exploit various RSA vulnerabilites to find original message m
"""

import gmpy2
from mpmath import mp
from Crypto.Util.number import *

from Algorithms.fermat_factoring import fermat_factors


def rsa_version_A_attack(n, e, c):
    # Calculate p and q that created n using Fermat Factoring Algorithm
    p, q = fermat_factors(n)

    # Calculate totient of n
    totient = (int(p)-1)*(int(q)-1)

    # Find private key d
    d = pow(e, -1, totient)

    # Find message m
    m = pow(c, d, n)

    print("Case A\n")
    print("Searching for p and q...")
    print(f"p: {int(p)}")
    print(f"q: {int(q)}\n")
    print("Decrypting...")
    print(f"totient: {totient}")
    print(f"d: {d}")
    print(f"m: {m}\n")

    return m

def rsa_version_B_attack(n, e, c):
    # Calculate prime number p that created n
    p = gmpy2.isqrt(gmpy2.mpz(str(n)))

    # Calculate totient of n
    totient = n - p 

    # Find private key d
    d = pow(e, -1, totient)

    # Find message m
    m = pow(c, d, n)

    print("Case B\n")
    print("Searching for p...")
    print(f"p: {int(p)}")
    print("Decrypting...")
    print(f"totient: {totient}")
    print(f"d: {d}")
    print(f"m: {m}\n")

    return m

def rsa_version_C_attack(n, c):
    for e in range(2**15, 2**16 + 1):
        if e % 2 != 0:
            m = pow(c, e, n)
            if (long_to_bytes(m).startswith(b'KRIPTOGRAFIITB{')): break

    print("Case C\n")
    print("Searching for e...")
    print(f"e: {int(e)}")
    print("Decrypting...")
    print(f"m: {m}\n")

    return m

def rsa_version_D_attack(e, c):
    # Because m and e is relatively small, 
    # Find message m by finding e-th root of c
    m = int(mp.root(mp.mpf(str(c)), e))

    print("Case D\n")
    print("Decrypting...")
    print(f"m: {m}\n")

    return m

def rsa_version_E_attack(n, e, c):
    # Calculate totient of n
    totient = n - 1 # Because n is prime

    # Find private key d
    d = pow(e, -1, totient)

    # Find message m
    m = pow(c, d, n)

    print("Case E\n")
    print("Decrypting...")
    print(f"totient: {totient}")
    print(f"d: {d}")
    print(f"m: {m}\n")
    
    return m