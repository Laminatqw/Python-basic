# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи



# def worklisting(worklist : list[str]):
#
#     def addsmth(note:str):
#         worklist.append(note)
#     def showlist()->list[str]:
#         return (worklist)
#     return [addsmth, showlist]
#
#
# worklist = ['washing', 'cleaning']
# addsmth, showlist = worklisting(worklist)

# addsmth('repair')
# print(showlist())




# 2) протипізувати перше завдання
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# def expandForm(num:int) ->str:
#     s = str(num)
#     list = []
#
#     lenght = len(s)
#
#     for i, s in enumerate(s):
#         if s != 0:
#             list.append(s + '0' * (lenght - i - 1))
#
#     return ' + '.join(list)
#
#
# print(expandForm(111111111111))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def decor(func):
    count = 1
    def inner():
        print('----------')
        nonlocal count
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

