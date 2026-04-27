vowels = {'a', 'e', 'i', 'o', 'u'}
s = "abciiidef"       
count = 0
max_count=0
k=3
        
        # Count vowels in first window
for i in range(k):
  if s[i] in vowels:
    count += 1
        
    max_count = count
        
        # Slide the window
    for i in range(k, len(s)):
            # Remove left character
            if s[i - k] in vowels:
                count -= 1
            
            # Add right character
            if s[i] in vowels:
                count += 1
            
            max_count = max(max_count, count)
print(max_count)