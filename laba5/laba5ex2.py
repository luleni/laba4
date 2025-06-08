arr = [1,8,5,31,4,2,0]
def summa_and_multipli(arr):
    summa = 0
    multiply = 1
    for i in arr:
        summa += i
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)

    for i in arr[start_index:end_index]:
        multiply *= i
    return summa, multiply

print(summa_and_multipli(arr))
