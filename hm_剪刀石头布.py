import random

player = int(input('请输入石头1剪刀2布3'))
computer = random.randint(1,3)
print('玩家出的是%d 电脑出的是%d' % (player,computer))

if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer ==1):
    print('player wins')
elif (player == 1 and computer == 1) or (player == 2 and computer == 2) or (player == 3 and computer ==3):
    print('draw')
else:
    print('computer wins')
