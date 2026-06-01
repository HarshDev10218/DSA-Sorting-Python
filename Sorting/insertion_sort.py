import array
a = array.array('i',[])
n = int(input("Enter the number of Elements of array : "))
temp = 0
for i in range(n):
    c = int(input("Enter the element of the array : "))
    a.append(c)
print("unsorted_array : ",a.tolist())

for i in range (1,n):
    temp = a[i]
    j = i - 1
    while j>=0 and a[j]>temp:
        a[j +1] = a[j]
        j-= 1
    a[j+1] = temp
print ("soeted_array :", a.tolist())
