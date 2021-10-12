# Написать функцию, которая определяет является ли шестизначное число "счастливым"
# (сумма первых трех цифр равна сумме последних трех цифр)
# При ошибочном вводе вывести "Input Error"



def module2(number):
    if type(number) != int:
        return "Input Error"
    else:
        if len(str(number)) != 6: return "Input Error"
        sum1 = number // 100000 + number // 10000 % 10 + number // 1000 % 10
        sum2 = number % 1000 // 100 + number % 100 // 10 + number % 10
        return sum1 == sum2



