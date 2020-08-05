def isPowerOfTwo(n):
    if n == 0:
        return False
    return (n & -(n)) == n #n & -n returns the right-most 1-bit of the number, and for numbers that are power of 2, 
    						#their binary form has only one 1-bit, which is also also the right-most one