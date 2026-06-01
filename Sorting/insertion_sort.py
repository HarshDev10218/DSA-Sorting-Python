def insertion_sort(arr):
    """
    Insertion Sort Algorithm
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    arr = arr.copy()  # Don't modify original array
    n = len(arr)
    
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    
    return arr


# Interactive mode - for manual testing
if __name__ == "__main__":
    import array
    a = array.array('i', [])
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        c = int(input("Enter element: "))
        a.append(c)
    print("Original array:", a.tolist())
    result = insertion_sort(a.tolist())
    print("Sorted array:", result)
