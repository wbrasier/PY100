age = int(input('How old are you? '))

years_from_now = list(range(10, 41, 10))

print(f'You are {age} years old.')

for years in years_from_now:
  print(f'In {years}, you will be {age + years} years old.')