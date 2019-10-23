#a_list = []
#b_list = [1,2,3]
#list(), or list(iterable)
#[(expression with x) for x in iterable]
#1
a_list = []
a_list.append(1)
a_list.append(2)
print(a_list, f'has a length of {len(a_list)}.')
#2
b_list = list(range(1, 9))
b_list.append(11)
print(b_list, f'has a length of {len(b_list)}.')
#3
c_list = [2**x for x in range(8)]
print(c_list, f'has a length of {len(c_list)}.')
pass
import random
n = 10
a_list = [random.randrange(1,100) for i in range(n)]
print(f'a_list comprehends {len(a_list)} random numbers:{a_list}')
pass
b_list = [x for x in a_list if x % 2 == 0]
print(f'... and it has {len(b_list)} even numbers: {b_list}')
-------------
a_list = [1,2,3]
b_list = [4,5,6]
c_list = a_list + b_list * 3
c_list
7 not in c_list
a_list > b_list
#Tuple
n = 10000
a = range(n)
b = tuple(a)
c = list(a)
a.__sizeof__()
b.__sizeof__()
c.__sizeof__()#I don't know why!
pass
a = 1,
print(a)
print(id(a))
a += 3, 5
print(a)
print(id(a))
#List, Tuple, Set
a = {}  # 这样创建的是dict，而不是set
b = set()  #√
type(a)
type(b)
pass
a = "abcabcabcabcdef"
b = range(10)
c = [1,2,2,3,3,1]
d = ('a', 'b','e','b','a')
set(a)
set(b)
set(c)
set(d)
pass
a = "abcabcdeabcdef"
b = {x for x in a if x not in 'abc'}
b
pass
#并集“|”，交集“&”，差集“-”，对称差集“^”
