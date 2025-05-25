Lst=['rock' , 'paper' , 'scissors']
a=input(f'''What you choose ?  
        {Lst[0]}  {Lst[1]}  {Lst[2]} :  ''')

import random as rn
b=rn.choice(Lst)
print(f'Computer chose {b}\n')
if a==b:
    print("It's a tie")
elif a=='rock' and b=='scissors' or a=='paper' and b=='rock' or a=='scissors' and b=='paper':
    print('You Won !')
else:
    print('Computer wins ! PLay Again.')