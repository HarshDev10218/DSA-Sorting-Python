import array
def sort (array):
    if len(array) <=1:
        return array
    mid = len(array)//2
    left = sort(array[:mid])
    right = sort(array[mid:])
    return merge(left,right)
def merge(left,right):
    result =[ ]
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i]<= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
a = array.array('i',[ ])
n = int(input("Enter the no.of elements of the array : "))
for i in range (n):
    b = int(input("Enter the element of the array : "))
    a.append(b)

print("Unsorted_array : ",a.tolist())
result = sort(a)

print("Sorted_array : ",result)
