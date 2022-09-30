# Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами,
# выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!

# переворот
# from random import randint
# n=10
# list1 = []*10
# for i in range(n):
#     i = randint(-5, 5)
#     list1.append(i)
# print(list1)

# list2 = []
# for i in range(len(list1)):
#     i = list1[len(list1)-1-i]
#     list2.append(i)
# print(list2)

# рандом
from random import randint
n = 10
lst1 = []*n
for i in range(n):
    i = randint(-5, 5)
    lst1.append(i)
print(lst1)


def ShuffleLst(lst, number):
    for i in range(number):
        i = randint(0, len(lst)-1)
        j = randint(0, len(lst)-1)
        tmp = lst[i]
        lst[i] = lst[j]        
        lst[j] = tmp        
    return lst


N = int(input('Введите N (количество перемешиваний: '))
ShuffleLst(lst1, N)
print(lst1)
