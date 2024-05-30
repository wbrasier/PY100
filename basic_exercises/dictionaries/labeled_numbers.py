numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for x in numbers:
  print(f'A {x} number is {numbers[x]}.')
  
for key,value in numbers.items():
  print(f'A {key} number is {value}.')