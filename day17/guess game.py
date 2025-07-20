mylist=[' ','o',' ']
from random import shuffle
def guess_game(mylist):
    shuffle(mylist)
    return mylist
def user_input():
    user_input=str(input('enter your guess 1,2,3:'))
    while user_input not in '123':
        user_input=str(input('enter your guess 1,2,3:'))
    return int(user_input)
def comparethem(mylist,user_input):
    if mylist[user_input]=='o':
        return 'correct guess'
    else:
        return 'wrong guess'
a=guess_game(mylist)
b=user_input()
print(comparethem(a,b))