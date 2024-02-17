def summa(*args):
    n = 0
    for i in args:
        n += i
    return n

def subtraction(a, *args):
    for i in args:
        a -= i
    return a

def multipli(num, num2):
    n = num * num2
    return n

def division(a, b):
    try:
        n = a/b
        return n
    except ZeroDivisionError:
        raise ZeroDivisionError("На ноль делить нельзя!")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
sign = int(input("""Выберите операцию, которую хотите выполнить: 
1. Сложение
2. Вычетание
3. Умножение
4. Деление"""))

if sign == 1:
    print(summa(num1, num2))
elif sign == 2:
    print(subtraction(num1, num2))
elif sign == 3:
    print(multipli(num1, num2))
elif sign == 4:
    print(division(num1, num2))
