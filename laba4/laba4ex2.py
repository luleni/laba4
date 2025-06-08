array = []
print('Введите 14 чисел:')
for i in range(14):
    j = int(input())
    array.append(j)
array.append(sum(array))
for i in array:
    print(array)