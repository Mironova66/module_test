# Написать функцию,которая заключает целое число в рамку из символов char и возвращает данную строку
# Пример:
# frame(16, '+') ==>
# ++++++
# + 16 +
# ++++++

def module4(num, char):

    if type(num) != int:
        return "Input Error"
    else:
        s = str(num)
        top=len(s)+4
        Stroka=top*char
        Stroka+="\n"+char+" "+s+" "+char
        Stroka+="\n"+top*char
        return Stroka

print(module4(-56, '/'))

