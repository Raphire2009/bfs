def search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

my_sorted_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target_val = 70
result = search(my_sorted_list, target_val)


def recursive_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_search(arr, target, mid + 1, high)
    else:
        return recursive_search(arr,  target, low ,mid - 1)
    
    
result = recursive_search(my_sorted_list, target_val, 0, len(my_sorted_list) - 1)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")


"""
Step 1: [10, 20, 30, 40, 50, 60, 70, 80, 90]  (low=0, high=8)
                  ^ mid=4 (val=50)
        Target 70 > 50, search right half.

Step 2: [60, 70, 80, 90] (low=5, high=8)
              ^ mid=5 (val=70)
        Target 70 == 70, Match Found! Return index 5.
"""