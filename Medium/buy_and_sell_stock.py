def max_profit(prices):
    """
    :param prices: list of prices for stock on a given day
    :return: maximum profit after making a buying then selling the stock
    """
    if len(prices) < 2:
        return 0
    # two pointers left and right
    left = 0
    right = 1
    result = max(0, prices[right] - prices[left])

    while right < len(prices) - 1:
        # if we find a new low of stock, move both pointers
        if prices[right] < prices[left]:
            left = right
            right = left + 1
        # else, gradually move to the right to calculate maximum profit
        else:
            right += 1
        result = max(result, prices[right] - prices[left])
    return result
