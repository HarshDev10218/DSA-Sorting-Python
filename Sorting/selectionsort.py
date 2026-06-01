def selection_sort(arr):
    """
    Selection Sort Algorithm
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    arr = arr.copy()  # Don't modify original array
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                # Swap elements
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr


# Interactive mode - for manual testing
if __name__ == "__main__":
    import array
    a = array.array('i', [])
    n = int(input("Enter the length of array: "))
    for i in range(n):
        b = int(input("Enter elements: "))
        a.append(b)
    print("Original array:", a.tolist())
    result = selection_sort(a.tolist())
    print("Sorted array:", result)
