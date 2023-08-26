# this code created by Mahdi Abbasi

# annotations in python has different with annotations in Django.
# annotations just is a guide for other user that read your code.


import typing as tp


def show(names: tp.Dict[str, int]):
    for name in names:
        return name


print(['ali', 'mahdi', 'hassan'])

# def show( n:'your name', a:'your age') -> 'this function returns string representation':

#     return f'{n} is {a} years old'

# print(show('mahdi',21))
# for github achivments and new branch