 #strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
# st1 = []
# for i in st:
#     if i.isdigit():
#         st1.append(i)
# print(','.join(st1))





# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34 fsk5djh784387 92ва93 3fttyf4'
# st1 = []
# st2 = []
#
#
# for i in st:
#     if i.isdigit():
#         st1.append(i)
#     else:
#         if st1:
#             st2.append(''.join(st1))
#             st1 = []
#
# if st1:
#     st2.append(''.join(st1))
# print(', '.join(st2))



# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# greeting = 'Hello, world'
# l = []
# for i in greeting:
#     l.append(i.upper())
#
# print(l)


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# l = []
# for i in range(50):
#     if i%2 != 0:
#         k = i**2
#         l.append(k)
#
# print(l)


# function
#
# - створити функцію яка виводить ліст
# def fucnlist(list):
#     print(list)
#
# l = [1,2,3,4]
# fucnlist(l)
# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def threenum(n, m, z):
#     l = [n, m ,z]
#
#     print(max(l))
#
# threenum(1,500,3)
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def func(*args):
#
#     print(max(args))
#     return min(args)
#
# func(1,2,32222222222222222222222,4,5,6,746789876543)


# - створити функцію яка повертає найбільше число з ліста

# def func(list):
#     return max(list)
#
# l = [1,2,3,4]
# func(l)

# - створити функцію яка повертає найменьше число з ліста
# def func(list):
#     return min(list)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum(list):
#     sum = 0
#     for i in list:
#         sum+=i
#     print(sum)
#
# list = [1,2,3,4,5,6,7,8,9]
# sum(list)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def average(list):
#     sum = 0
#     counter = 0
#     for i in list:
#          sum+=i
#          counter+=1
#     avrg = sum / counter
#     print(avrg)
#
# list = [1,2,3,4]
# average(list)


# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню

list = [22, 3,5,2,8,2,-23, 8,23,5]
# print(min(list))

def clear(list):
    copy = list.copy()
    print(set(copy))
# clear(list)
def replace(list):
    for i in range(3, len(list), 4):
        list[i] = 'X'
    print(list)
# replace(list)

def square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print('*'*n)
        else:
            print('*'+ ' '*(n-2) + '*')
# square(4)
def whule():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i*j
            print(res, end=' ')
            j+=1

        print()
        i+=1


whule()