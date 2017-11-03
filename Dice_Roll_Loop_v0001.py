import random

while True:
    side = input('How many sides? ')
    # if side == 'str':
        # break
    # print('Rolling a ' + side + ' sided dice.')
    print('You rolled ' + str(int(random.randint(1,int(side)))))
    roll_again = input('Would you like to roll again? ')
    if roll_again == 'no':
        break
print('See you next time!')


