# ================================
# Daneshjo: [Darya Behrooz]
# Shomareh Daneshjoii: [404130473]
# Onvan Proje: Shabihsaz Jam Jahani
# Tarikh Tahvil: [1405/05/01]
# ================================
#  utils.py | tozie Poisson | vabastegi: nadarad

import math
import random


def poisson_random(lam):
    """
    Tolid adad sahih az tozie Poisson ba estefade az Inverse Transform Method.

    Args:
        lam (float): Miangin (lambda) tozie Poisson.

    Returns:
        int: Adad sahih gheyr-manfi az tozie Poisson(lam).
    """
    # Agar lambda montafi bashad, 0 bar migardanad
    if lam <= 0:
        return 0

    # Hadd paeen baraye halghe (exp(-lambda))
    L = math.exp(-lam)
    k = 0
    p = 1.0

    # Algorithm standard Inverse Transform baraye Poisson
    # Tavalod adad random ta zamani ke p > L
    while p > L:
        k += 1
        p *= random.random()

    return k - 1


