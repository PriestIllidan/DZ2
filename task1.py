# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11


def SumNumbers(number):
    result = 0
    if number < 0:
        number *= -1
    while number - int(number) != 0:
        number *= 10
    while number != 0:
        result += int(number % 10)
        number /= 10
    return result


number = float(input('Введите число: '))
print(SumNumbers(number))
