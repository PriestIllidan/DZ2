# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек
# и находит расстояние между ними в N-мерном пространстве.
def DistanceAB(N):
    res = 0
    while N > 0:
        A = int(input('Введите координату точки A: '))
        B = int(input('Введите координату точки B: '))
        res += (A-B)**2
        N = N-1
    res = res**(1/2)
    return res


N = int(input('Введите N-пространство: '))
print(round(DistanceAB(N), 2))
