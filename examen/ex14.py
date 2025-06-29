arr = [1,3,5,4,2,8,9]
counter = 0
counter1 = 0
for i in arr:
    if i % 2 == 0:
        counter += 1
    elif i % 2 != 0:
        counter1 += 1
print(f'Четных чисел - {counter}, нечетных - {counter1}')