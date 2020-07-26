
"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

"""
def maxProfit(self, prices: List[int]) -> int:
    total = 0
    for i in range (1, len(prices)):
        if prices[i] > prices[i-1]:
            total+=prices[i] - prices[i-1]
    return total