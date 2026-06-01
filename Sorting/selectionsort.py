import array 
a = array.array('i',[])
n = int(input("Enter the length of array :"))
float = 0
temp = 1
for i in range(n):
    b = int(input("Enter elements of a :"))
    a.append(b)
print(a.tolist())

for i in range(n-1):
    float = 0
    for j in range(i+1, n):
        if a[j] < a[i]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            float+=1
        if float == n-1:
            break

print("Sorted array:", a.tolist())
