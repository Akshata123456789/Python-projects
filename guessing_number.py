import random
count = 0
while True:
  choice = input('enter y/n:').lower()
  if choice == 'y':
       num = int(input('enter how many dice to roll:'))
       if num <10 or num!=0:
           for i in range(num):
                 dice1=random.randint(1,6)
                 dice2=random.randint(1,6)
                 print(f'{dice1},{dice2}')
           count = count+1
  
  elif choice == 'n':
        print('Thanks for playing')
        print('rolled count is:',count)
        break
  else:
        print('invalid input')
        
  