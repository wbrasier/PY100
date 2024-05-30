def compare_by_length(string1, string2):
  length1 = len(string1)
  length2 = len(string2)
  if length1 > length2:
    return 1
  elif length2 > length1:
    return -1
  else:
    return 0
    
print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0