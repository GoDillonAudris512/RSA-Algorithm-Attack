"""
fermat_factoring.py
- Find the factor p and q of n = pq
- p and q are roughly the same size
"""

from mpmath import mp

def fermat_factors(n):
    # Find smallest k so k^2 > n
    root_n = mp.sqrt(mp.mpf(str(n)))
    k = int(mp.ceil(root_n))

    # Start trying to find p and q
    p, q = find_p_and_q(k, n)
    
    return p, q

def find_p_and_q(k, n):
    new_k = k
    result = pow(new_k, 2) - n

    while not is_square(result):
        new_k = new_k + 1
        result = pow(new_k, 2) - n

    root_result = mp.floor(mp.sqrt(mp.mpf(str(result))))

    p = new_k + root_result
    q = new_k - root_result

    return p, q

def is_square(n):
    root = mp.sqrt(mp.mpf(str(n)))
    power = mp.power(mp.floor(root), 2)
    return int(power) == n