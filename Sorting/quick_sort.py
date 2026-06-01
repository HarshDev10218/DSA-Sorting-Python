def quick_sort(arr):
    """
    Quick Sort Algorithm (Divide & Conquer)
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)
    
    return sorted_left + [pivot] + sorted_right


# Interactive mode - for manual testing
if __name__ == "__main__":
    import array
    
    n = int(input("Enter the number of elements: "))
    a = array.array('i', [])
    
    for i in range(n):
        b = int(input("Enter element: "))
        a.append(b)
    
    print("Original array:", a.tolist())
    result = quick_sort(a.tolist())
    print("Sorted array:", result)
