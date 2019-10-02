def is_prime(n)：
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

for i in range(80, 110):
    if is_prime(i):
        print(i) #该函数出错

x = 0
x += 1
print(x)

a = 1 + 2 * 3
a += 1
print(a)

11 + 10 - 9 * 8 / 7 // 6 % 5
'3.14' + 3 #报错