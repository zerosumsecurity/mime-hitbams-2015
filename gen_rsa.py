#!/usr/bin/python

import random
import os

def rabin_miller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(7): 
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: 
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def is_prime(num):
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    for prime in small_primes:
        if (num % prime == 0):
            return False

	return rabin_miller(num)

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
       q, r = b//a, b%a
       m, n = x-u*q, y-v*q
       b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
       return None
    else:
       return x % m

def next_prime(n):
	if 0 == n%2:
		n = n+1
 	while True:
 		if is_prime(n):
 			return n
 		else:
 			n = n+2
            
def gen_rsa_parameters():
    r = os.urandom(63)
    e = int(r.encode('hex'), 16) 
    e = next_prime(e)
    r = os.urandom(64)
    p = int(r.encode('hex'), 16) 
    p = next_prime(p)
    q = (p*modinv(p-1, e)%e)
    while not is_prime(q):
        q += e
    N = p*q
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    return N,e,d,p,q



