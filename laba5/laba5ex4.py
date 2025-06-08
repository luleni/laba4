string = input('Введите строку:')

def string_change(string):
    if string.startswith('abc'):
        return string.replace('abc', 'www')
    else:
        return string + 'zzz'

print(string_change(string))
