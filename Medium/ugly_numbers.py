#Write a program to find the n-th ugly number.

#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5
# n does not exceed 1690

def nthUglyNumber(n):
    results = [1]
    i1= i2= i3 = 0
    for i in range(n):
        a = min(results[i1]*2, results[i2]*3, results[i3]*5)
        results.append(a)
        if a == results[i1]*2:
            i1+=1
        if a== results[i2]*3:
            i2+=1
        if a==results[i3]*5:
            i3+=1
    return results[n-1]