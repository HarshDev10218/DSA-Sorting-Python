import array 
a = array.array('i',[ ])
n = int(input("Enter the length of array :"))
temp = 1
for i in range(n):
    b = int(input("Enter elements of a :"))
    a.append(b)
print(a.tolist())
for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print("Sorted array:", a.tolist())

