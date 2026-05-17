import sympy, numpy, math, pygame

def findD(phi: int, e: int):
    quotient_list = []
    tally_sequence = [0, 1]
    remainder = 0
    previous = phi
    current = e
    
    while remainder != 1:
        quotient = previous // current
        quotient_list.append(quotient)
        remainder = previous % current

        tally_sequence.append(tally_sequence[-2] - (quotient * tally_sequence[-1]))
        previous, current = current, remainder
    
    d = tally_sequence[-1]
    if d < 0:
        d += phi
    return d

def rsaEncryption():
    # Generate the two random primes for encryption
    p = sympy.randprime(100, 999)
    q = sympy.randprime(100, 999)
    if q == p:
        q = sympy.randprime(100, 999)
    print(f"p: {p}")
    print(f"q: {q}")
    # Create the first part of the public key
    n = p * q
    print(f"n: {n}")
    # Find number of coprimes of n
    phi = (p - 1) * (q - 1)
    print(f"phi: {phi}")
    # Find e (second part of public key)
    e = 65537 if math.gcd(65537, phi) and (65537 < phi) else 257
    public_key = (e, n)
    print(f"e: {e}")
    print(f"public_key: {public_key}")
    # Find d (private key)
    d = findD(phi, e)
    private_key = (d, n)
    print(f"d: {d}")
    print(f"private_key: {private_key}")

rsaEncryption()