arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 56


def binary_search_recursive(arr, target, left, right):
    # If the search bounds cross, the target isn't in the array
    if left > right:
        return -1
    # Calculate the middle index
    mid = left + (right - left) // 2
    # If middle value equals the target, return the index
    if arr[mid] == target:
        return mid
    # If the target is bigger than the middle value, search in the right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    # If the target is smaller than the middle value, search in the left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_iterative(arr, target):
    # Define the search bounds
    left, right = 0, len(arr) - 1
    while left <= right:
        # Calculate the middle index
        # mid = left + ((right - left) // 2)
        mid = (left + right) // 2
        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid
            # If the target is bigger, narrow the search to the right half
        elif arr[mid] < target:
            left = mid + 1
            # If the target is smaller, narrow the search to the left half
        else:
            right = mid - 1
            # Return -1 if the target is not found
    return -1


# result = binary_search_recursive(arr, target, 0, len(arr) - 1)
result = binary_search_iterative(arr, target)
if result != -1:
    print(f"Iterative: Target found at index {result}")
else:
    print("Iterative: Target not found")
