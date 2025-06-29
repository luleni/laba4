arr = [1,6,4,3,2]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
print(arr)