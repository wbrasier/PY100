my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
  
even_odd_list = ['even' if num % 2 == 0 else 'odd' for num in my_list]

print(even_odd_list)