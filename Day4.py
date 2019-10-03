type(3)
type(3.0)
type('3.14')
type(True)
type(range(10))
type([1,2,3])
type((1,2,3))
type({1,2,3})
type({'a':1,'b':2,'c':3})

n = -95
n < 0 and (n + 1) % 2 == 0

'Awesome' + 'Python'
'Awesome' 'Python'
'Python, ' + 'Awesome! ' * 3
'o' in 'Awesome' and 'o' not in 'Python'

'A' > 'a'
ord('A')
ord('a')

import math
math.sin(5)

3.1415926.as_integer_ratio()

True or 'Python'

for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
        else:
            print(n)#有错误

