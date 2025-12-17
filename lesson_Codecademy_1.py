name = input('What is your name? - ')
asks = input('What is your Question? - ')

print(name, ' asks: ', asks)

import random
number = random.randint(1, 9)
print('Number: ', number)

if number == 1:
  print('Magic 8-Ball’s answer: Yes - definitely')
elif number == 2:
  print('Magic 8-Ball’s answer: It is decidedly so')
elif number == 3:
  print('Magic 8-Ball’s answer: Without a doubt')
elif number == 4:
  print('Magic 8-Ball’s answer: It is decidedly so')
elif number == 5:
  print('Magic 8-Ball’s answer: Without a doubt')
elif number == 6:
  print('Magic 8-Ball’s answer: It is decidedly so')
elif number == 7:
  print('Magic 8-Ball’s answer: Without a doubt')
elif number == 8:
  print('Magic 8-Ball’s answer: It is decidedly so')
elif number == 9:
  print('Magic 8-Ball’s answer: Without a doubt')
else:
  print('Error')
  