# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
# функцию pr менять не можно
from dataclasses import replace
# def pr():
#   return 'Hello_boss_!!!'
#
# def decor(func):
#     def inner():
#         word = func()
#         return word.replace('_', ' ')
#     return inner
#
# @decor
# def pr():
#   return 'Hello_boss_!!!'
#
# print(pr())

# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
#
# size = 10
# i = 1
# j = 0
# count = 0
#
# while count <size:
#     res = i + j
#     i = j
#     j = res
#     count+=1
#     print(res)







# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
# x = 233243451
#
# parne = 0
# neparne = 0
#
# for i in str(x):
#     if int(i)%2 == 0:
#         parne += 1
#     else:
#         neparne += 1
#
# print(parne)
# print(neparne)

# прога, що виводить кількість кожного символа з введеної строки, наприклад:
# st = 'as 23 fdfdg544'  # введена строка
#
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2

# st = 'as 23 fdfdg544'
# st1 = set()
# for i in st:
#     if i not in st1:
#         print(set(i), ' =', st.count(i))
#         st1.add(i)
#     else:
#         pass

#створити декоратор який буде рахувати кількість запущених функцій продекорованих цим декоратором
count = 1
def decor(func):
    def inner():
        print('----------')
        global count
        print('counter = ', count)
        func()
        count +=1
    return inner



@decor
def func1():
    print('hello')
@decor
def func2():
    print('hello2')

func1()
func2()
func1()
func1()
func2()
func2()
func1()
