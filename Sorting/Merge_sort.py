def merge_sort(arr):
    """
    Merge Sort Algorithm (Divide & Conquer)
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Helper function to merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Interactive mode - for manual testing
if __name__ == "__main__":
    import array
    a = array.array('i', [])
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        b = int(input("Enter element: "))
        a.append(b)
    
    print("Original array:", a.tolist())
    result = merge_sort(a.tolist())
    print("Sorted array:", result)
