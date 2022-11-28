def divisor_game(N):
    dp = [False] * (N+1)
    for i in range(N+1):
        for j in range(1, i//2+1):
            if i % j == 0 and dp[i-j] is False:
                dp[i] = True
                break
    print(dp)
    return dp[N]


print(divisor_game(10))