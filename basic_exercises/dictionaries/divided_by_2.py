numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
half_numbers = []

for num in numbers:
  half_numbers.append(int(numbers[num]/2))
  
print(half_numbers)