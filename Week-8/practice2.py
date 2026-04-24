

s = "abciiidef"
k = 3

def max_vowels(s, k):
    vowels = "aeiou"
    count = 0

    # first window
    for i in range(k):
        if s[i] in vowels:
            count += 1

    max_count = count

    # sliding window
    for i in range(k, len(s)):
        if s[i - k] in vowels:
            count -= 1

        if s[i] in vowels:
            count += 1

        if count > max_count:
            max_count = count

    return max_count



print(max_vowels(s, k))