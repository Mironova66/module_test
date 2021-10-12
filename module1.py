# Написать функцию, которая определяет является ли целое число четным
# При ошибочном вводе вывести "Input Error"

def module1(num):
    if type(num) != int: return "Input Error"
    else:
        num = abs(num)
        if ((num % 2) == 0): return True
        else: return False

