# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# простое решение
N = int(input('Введите число: '))

res = 1
for i in range(1, N+1):
    res *= i
    print(res, end = ' ')

print()

# через список

def Factorial(number):
    res = []
    res.append(1)
    res.append(1)

    for i in range(1, N+1):
        res.append(res[i] * i)
    res.pop(0)
    res.pop(0)
    return res


N = int(input('Введите число: '))
print(Factorial(N))
