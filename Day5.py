import random
r = random.randrange(1, 1000)

if r % 2 == 0:
    print(f'{r} is even.')


import random
r = random.randrange(1, 1000)

if r % 2 == 0:
    print(f'{r} is even.')
else:
    print(f'{r} is odd.')


import random
r = random.randrange(2, 13)

if r == 7:
    print('Draw!')
elif r < 7:
    print('Small!')
elif r > 7:
    print('Big!')


for a in range(10):
    print(f'value of a: {a}')


for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
        else:
            print(n)


n = 1000
a, b = 0, 1
while a < n:
    print(a, end=' ')
    a, b = b, a+b
print()


from random import randrange

coin_user, coin_bot = 10, 10
rounds_of_game = 0

def bet(dice, wager):
    if dice == 7:
        print(f'The dice is {dice};\nDRAW!\n')
        return 0
    elif dice < 7:
        if wager == 's':
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1
        else:
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
    elif dice > 7:
        if wager == 's':
            print(f'The dice is {dice};\nYou LOST!\n')
            return -1
        else:
            print(f'The dice is {dice};\nYou WIN!\n')
            return 1

while True:
    print(f'You: {coin_user}\t BOT: {coin_bot}')
    dice = randrange(2, 13)
    wager = input("what's your bet? ")
    if wager == 'q':
        break
    elif wager in 'bs':
        result = bet(dice, wager)
        coin_user += result
        coin_bot -= result
        rounds_of_game += 1
    if coin_user == 0:
        print("Woops, you've LOST ALL, and game over!")
        break
    elif coin_bot == 0:
        print("Woops, the robot's LOST ALL, and game over!")
        break
    
print(f"You've played {rounds_of_game} rounds.\n")
print(f"You have {coin_user} coins now.\nBye!")


