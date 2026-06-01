import array

def sort(arr):
    if len(arr) <= 1:
        return list(arr)
        
    pivot = arr[0]
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
            
    sorted_left = sort(left)
    sorted_right = sort(right)
    
    return merge(sorted_left, sorted_right, pivot)

def merge(left, right, pivot):
    result = []
    result.extend(left)
    result.append(pivot)
    result.extend(right)
    return result

n = int(input("Enter the no. of elements of the array: "))
a = array.array('i', [])

for i in range(n):
    b = int(input("Enter the element of the array: "))
    a.append(b)

print("Unsorted array :", a.tolist())

result = sort(a)
print("Sorted array   :", result)
