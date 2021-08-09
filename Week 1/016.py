You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling the stock.

Example

For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.

"""
Understand:
- take in array of int
- find the best day to buy and sell a stock to maximize profit
- if profit is negative, return 0

Plan:
- take in array
- create new list
- create variable to represent length
- iterate from right to left based on length of array to index 0
- create index variable set it equal to math to the last index
- assign i to index variable
- subract previous index(prices[i-1]) from current index(prices[i])
    - if difference is a positive # or zero, append to new list
    - otherwise continue with the loop
- return max value from new list
"""

def buyAndSellStock(prices):
    minPrice = float("inf")
    maxMoney = 0
    
    for price in prices:
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxMoney:
            maxMoney = price - minPrice
    return maxMoney
    
    
    
    
    
    
    # bProfit = 0
    # if len(prices) < 2:
    #     return 0
        
    # for i in range(len(prices) -1):   
    #     for j in range(i+1, len(prices)):
    #         dif = prices[j] - prices[i]
    #         if dif > bProfit:
    #             bProfit = dif   
    #         elif dif < bProfit:
    #             continue
    #         print(bProfit)   
    # return bProfit
    
    #          i  j
    # prices: [8, 5, 3, 1]