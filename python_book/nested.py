my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

# do not use any for loops, and print every even number

total_len = len(my_list)
outer_counter = 0

while outer_counter < total_len:
  inner_counter = 0
  inner_obj = my_list[outer_counter]
  inner_len = len(inner_obj)
  if inner_len > 1:
    while inner_counter < inner_len:
      if inner_obj[inner_counter] % 2 == 0: 
        print(inner_obj[inner_counter])
      inner_counter += 1
  else:
    if inner_obj % 2 == 0: print(inner_obj)
  outer_counter += 1
  