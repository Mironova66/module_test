# Написать функцию, которая считает сумму всех цифр целого числа

def module3(num):
    if type(num) != int: return "Input Error"
    else:
        sum = 0
        num=abs(num)
        k = len(str(num))+1
        for i in range (k):
            sum += num%10
            num=num//10
        return sum