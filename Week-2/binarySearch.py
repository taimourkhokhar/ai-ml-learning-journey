numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]

def binary_search(numbers, find):
    left = 0
    right = len(numbers) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        mid_number = numbers[mid]

        if mid_number == find:
            return mid
        
        if mid_number < find:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def binary_search_recursive(numbers, find, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    mid_number = numbers[mid]

    if mid_number == find:
        return mid
    
    if mid_number < find:
        return binary_search_recursive(numbers, find, mid + 1, right)
    else:
        return binary_search_recursive(numbers, find, left, mid - 1)

numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
print(binary_search_recursive(numbers_list, 21, 0, len(numbers_list)-1))









print(binary_search(numbers_list, 21)) 