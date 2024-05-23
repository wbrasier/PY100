num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')


def multiply(num1, num2):
  return(num1 * num2)
  

print(f'{num1} * {num2} = {multiply(float(num1), float(num2))}')