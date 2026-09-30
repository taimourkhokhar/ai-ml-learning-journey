# prices = [7,1,5,3,6,4]
# mini=min(prices)
# print(mini)
# maxi=mini
# diff=0
# for i in range(prices.index(mini),len(prices)):
#     if prices[i]>maxi:
#         maxi=prices[i]
#     diff=maxi-mini
# print(diff)
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         min_price = float('inf')
#         max_profit = 0

#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             elif price - min_price > max_profit:
#                 max_profit = price - min_price

#         return max_profit