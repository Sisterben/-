#1
age = input('Please tell me your age: ')
if age < 18:
    print('I can not sell you drinks...')
else:
    print('Have a nice drink!')#错误示范
pass
age = int(input('Please tell me your age:
 an int number , e.g:22
\'))
if age <18:
    print('I can not sell you drinks...')
else:
    print('Have a nice drink!')#It seems that something goes wrong,
                               #so it would not run.
pass
age = int(input('Please tell me your age:an int number , e.g: 22'))
if age < 18:
    print('I can not sell you drinks...')
else:
    print('Have a nice drink!')#It has been solved,but why we have to print like this?
pass
#2
s = "He said, it\'s fine."      #raw
print(s)                        #presentation
#3 字符串可以用空格或+拼接
'Hey!' + ' ' + 'You!'
'Ha' * 3#copy 3 times
'o' in 'Hey!You!'
#4字符索引
s = 'Python'
for char in s:
    print(s.index(char), char)
pass
s = 'Python'
for i in range(len(s)):
    print(s[i])
#更简洁写法
for i in s:
    print(i)
s = 'Python'
s[1]
s[2:]
s[2:5]
s[:5]
s[1:2:5]
pass
#用于字符串的内建函数
len(s)
pass
#4用于处理字符串的METHOD
#大小写转换
#.str.upper()
#2.str.lower()
#3.str.swapcase()逐个字符更替大小写
#4.str.casefold()
#5.str.capitalize()
#6.str.title()
#7.str.encode()处理非中文
#page79 end