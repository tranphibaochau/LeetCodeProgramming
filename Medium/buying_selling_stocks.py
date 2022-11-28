def max_profit(prices):
    _max_profit = 0
    buying = selling = 0
    while buying < len(prices) - 1 and selling < len(prices) - 1:
        # buy the stock everytime it decreases
        while buying < len(prices) - 1 and prices[buying] > prices[buying + 1]:
            buying += 1

        # do not sell as long as keeps going up
        selling = buying
        while selling < len(prices) - 1 and prices[selling] < prices[selling + 1]:
            selling += 1

        # calculate the profit and add it to the total and keeps going
        _max_profit += prices[selling] - prices[buying]
        buying = selling + 1
    return _max_profit
