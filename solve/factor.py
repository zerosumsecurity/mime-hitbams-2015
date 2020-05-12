#!/usr/bin/python

import sys

def exact_sqrt(x):
    """Calculate the square root of an arbitrarily large integer. 

    The result of exact_sqrt(x) is a tuple (a, r) such that a**2 + r = x, where
    a is the largest integer such that a**2 <= x, and r is the "remainder".  If
    x is a perfect square, then r will be zero.

    The algorithm used is the "long-hand square root" algorithm, as described at
    http://mathforum.org/library/drmath/view/52656.html

    Tobin Fricke 2014-04-23
    Max Planck Institute for Gravitational Physics
    Hannover, Germany
    """

    N = 0   # Problem so far
    a = 0   # Solution so far

    # We'll process the number two bits at a time, starting at the MSB
    L = x.bit_length()
    L += (L % 2)          # Round up to the next even number

    for i in xrange(L, -1, -1):

        # Get the next group of two bits
        n = (x >> (2*i)) & 0b11

        # Check whether we can reduce the remainder
        if ((N - a*a) << 2) + n >= (a<<2) + 1:
            b = 1
        else:
            b = 0

        a = (a << 1) | b   # Concatenate the next bit of the solution
        N = (N << 2) | n   # Concatenate the next bit of the problem

    return a

def factor(N, e):
	s = N%e
	count =0
	while True:
		count = count+1
		if count > 10000:
			print "[-] factorization failed"
			return
		a = exact_sqrt(s*s - 4*N)
		p = (s+a)/2
		if 0 == N%p:
			q = N/p
			print "[+] factored n in %d iterations" % count
			print "[+] p = %s" % str(p)
			print "[+] q = %s" % str(q)
			return
		else:
			s = s+e

usage = "usage: ./factor <N> <e>"

if __name__ == "__main__":
	if 3 == len( sys.argv ):
		try:
			factor( int(sys.argv[1]), int(sys.argv[2]) )
		except:
			print usage
	else:
		print usage
			 

