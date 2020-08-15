def kthGrammar(N, K):
    previous = "0"
    if N == 0:
        return 0
    def kth_rec(N, previous):
        if N == 0:
            return previous
        result = ''
        for i, n in enumerate(previous):
            if n == '0':
                result+='01'
            else:
                result+='10'
        return kth_rec(N-1, result)
    return int(kth_rec(N+1, previous)[K-1])

print(kthGrammar(0, 2))
