# def licz_od_zera(do):
#     licznik = 0
#     while licznik < do:
#         yield licznik
#         licznik += 1
#
# # Używanie generatora
# generator = licz_od_zera(10)
#
# for liczba in generator:
#     print(liczba)

#
# from collections import OrderedDict
#
# dict = {'b': 2, 'a': 1, 'c': 3}
# dict['e'] = 5
# dict['f'] = 4
#
# ordered_dict = OrderedDict(dict)
#
# reversed_ordered_dict = OrderedDict(reversed(ordered_dict.items()))
#
# print(f"Słownik: ", dict)
# print(f"Posegregowany", ordered_dict)
# print(f"Odwrócony", reversed_ordered_dict)
#
# sum = lambda x,y: x + y
#
# res = sum(9, 3)
# print(res)
#
# def multiply_number(n):
#     return lambda x: x*n
#
# multiply_by_5 = multiply_number(5)
# res = multiply_by_5(7)
# print(res)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(n):
    return n % 2 == 1

#res = map(lambda x: x ** 3, numbers)
#res = filter(is_odd, numbers)
res = filter(lambda x: x % 2 == 1, numbers)

print(list(res))