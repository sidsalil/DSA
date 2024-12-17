def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.

    Args:
        arr: The input array.
        n: The size of the heap.
        i: The index of the root of the subtree.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root or left child
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Performs heap sort on the given array.

    Args:
        arr: The input array.

    Returns:
        The sorted array.
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]

        # call max heapify on the reduced heap
        heapify(arr, i, 0)
    return arr


# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is", end=" ")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")