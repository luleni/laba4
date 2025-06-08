class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
users = [
    User("lalala", "123"),
    User("nanana", "456"),
    User("tatata", "789"),
    User("xaxaxa", "012"),
    User("rarara", "345"),
]
def find_user(login, password):
    for i in users:
        if i.login == login and i.password == password:
            return i

login_to_find = input("Введите логин: ")
password_to_find = input("Введите пароль: ")

found_user = find_user(login_to_find, password_to_find)
if found_user:
    print(f"Найден пользователь: {found_user.login}")
else:
    print("Пользователь не найден")