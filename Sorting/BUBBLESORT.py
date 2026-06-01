def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    arr = arr.copy()  # Don't modify original array
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Interactive mode - for manual testing
if __name__ == "__main__":
    import array
    a = array.array('i', [])
    n = int(input("Enter the length of array: "))
    temp = 1
    for i in range(n):
        b = int(input("Enter elements: "))
        a.append(b)
    print("Original array:", a.tolist())
    result = bubble_sort(a.tolist())
    print("Sorted array:", result)
