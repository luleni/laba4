arr = [1, 2, 4, 5]
n = len(arr) + 1
missing_number = n * (n + 1) // 2 - sum(arr)
print("Пропущенное число:", missing_number)
