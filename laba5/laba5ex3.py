import random
arr = []
for i in range(10):
    arr.append(random.randint(1,100)*2)
    arr.sort()
print(arr)
