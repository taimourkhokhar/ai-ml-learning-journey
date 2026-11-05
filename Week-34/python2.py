
output = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
out = 0
s = "IV"
for i in range(len(s)):
            # If a smaller value comes before a larger value, subtract it
            if i + 1 < len(s) and output[s[i]] < output[s[i + 1]]:
                out -= output[s[i]]
            else:
                out += output[s[i]]

print(out)
