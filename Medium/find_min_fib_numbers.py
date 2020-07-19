#Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.
#It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.


#method 1: recursive function
def findMinFibonacciNumbers(self, k):
    #first we build an array of fibonacci numbers that is less than or equal to k
    fib_array = [1, 1]
    nxt = 2
    while nxt <= k:
        fib_array.append(nxt)
        nxt = fib_array[-1] + fib_array[-2]
    def findminNum(k, f_array, res):
        if k in f_array:
            return res+1
        remaining = k
        for n in f_array[::-1]:
            if n < k:
                remaining = k-n
                break
        return findminNum(remaining, f_array, res+1)
    return findminNum(k, fib_array, 0)

#dynamic programming