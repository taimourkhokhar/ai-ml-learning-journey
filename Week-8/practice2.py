

# s = "abciiidef"
# k = 3

# def max_vowels(s, k):
#     vowels = "aeiou"
#     count = 0

#     # first window
#     for i in range(k):
#         if s[i] in vowels:
#             count += 1

#     max_count = count

#     # sliding window
#     for i in range(k, len(s)):
#         if s[i - k] in vowels:
#             count -= 1

#         if s[i] in vowels:
#             count += 1

#         if count > max_count:
#             max_count = count

#     return max_count



# print(max_vowels(s, k))


prices = [7, 1, 5, 3, 6, 4]

min_price = float('inf') 
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    
    current_profit = price - min_price
    
    if current_profit > max_profit:
        max_profit = current_profit

print(f"Buy at: {min_price}")
print(f"Max Profit: {max_profit}")
