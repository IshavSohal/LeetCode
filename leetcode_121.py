from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    prices[i] is the price of a stock on the ith day
    return: maximum profit that can be earned
    """
    max_profit = 0

    # for every stock price, compare will all subsequent costs, and record the largest difference
    for i in range(len(prices)):
        price1 = prices[i]
        price2 = max(prices[i:])
        profit = price2 - price1

        if profit> max_profit:
            max_profit = profit

    return max_profit


def maxProfit2(prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0

    max_profit = 0
    max_price = max(prices[1:])
    max_price_index = prices.index(max_price)

    # for every stock price, compare will all subsequent costs, and record the largest difference
    # Idea: reuse max price for multiple iterations, until index has surpassed it, where we recalculate
    # the max_price
    for i in range(len(prices) - 1): # Buying stock last day should not be considered
        price1 = prices[i]

        if i >= max_price_index:
            max_price = max(prices[i+1:])
            max_price_index = prices.index(max_price)

        price2 = max_price
        profit = price2 - price1

        if profit > max_profit:
            max_profit = profit


    return max_profit


def maxProfit3(prices: List[int]) -> int:
    """
    prices[i] is the price of a stock on the ith day
    return: maximum profit that can be earned
    """
    if len(prices) <= 1:
        return 0

    max_profit = 0
    i = 0

    while i < len(prices) - 1:

        max_price = max(prices[i+1:])
        max_index = prices.index(max_price, i+1)

        min_price = min(prices[i:max_index])
        #min_index = prices.index(min_price, i)

        profit = max_price - min_price

        if profit > max_profit:
            max_profit = profit


        i = max_index + 1

    return max_profit

