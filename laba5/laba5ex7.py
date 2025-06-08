x = float(input("Введите точку х:"))
y = float(input("Введите точку у:"))
r = float(input("Введите радиус:"))
def point_on_circle(x, y, r):
    if x*x + y*y <= r*r:
        return "Точка принадлежит окружности"
    else:
        return "Точка не принадлежит окружности"
print(point_on_circle(x, y, r))