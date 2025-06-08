a = int(input('Введите число а:'))
b = int(input('Введите число b:'))
def calculating_value(a,b):
    result = (a + 4 * b) * (a - 3 * b) + a * 2
    return result
print(calculating_value(a,b))
