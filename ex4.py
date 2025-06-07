import datetime
date_string = input("Введите дату в формате 01.09.2021: ")
weekdays = {
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница",
    "Saturday": "Суббота",
    "Sunday": "Воскресенье"}
months = {
    "January": "Января",
    "February": "Февраля",
    "March": "Марта",
    "April": "Апреля",
    "May": "Мая",
    "June": "Июня",
    "July": "Июля",
    "August": "Августа",
    "September": "Сентября",
    "October": "Октября",
    "November": "Ноября",
    "December": "Декабря"}

def date_format(date_string):
    date_object = datetime.datetime.strptime(date_string, "%d.%m.%Y")
    weekday = date_object.strftime("%A")
    day = date_object.day
    month = date_object.strftime("%B")
    year = date_object.year
    return f"{weekdays[weekday]}, {day} {months[month]}, {year} год"

print(date_format(date_string))