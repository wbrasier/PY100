import random
random_number = random.randint(0, 1)

if random_number:
  print('Yes!')
else:
  print('No')


print('Yes!' if random_number else 'No')