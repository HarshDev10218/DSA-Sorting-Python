import array

def sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return list(arr)
        
    pivot = arr[0]
    left = []
    right = []
    
    # Partition the elements based on the pivot
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
            
    # Recursive calls to sort the left and right sub-arrays
    sorted_left = sort(left)
    sorted_right = sort(right)
    
    # Merge the sorted parts together with the pivot
    return merge(sorted_left, sorted_right, pivot)

def merge(left, right, pivot):
    result = []
    result.extend(left)
    result.append(pivot)
    result.extend(right)
    return result

# --- User Input and Main Program Execution ---
n = int(input("Enter the no. of elements of the array: "))
a = array.array('i', [])

for i in range(n):
    b = int(input("Enter the element of the array: "))
    a.append(b)

print("Unsorted array :", a.tolist())

# Run the sorting algorithm and print the results
result = sort(a)
print("Sorted array   :", result)
