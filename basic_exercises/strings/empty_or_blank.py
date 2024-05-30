def is_empty_or_blank(s):
  if len(s) == 0:
    return True
  elif s.isspace():
    return True
  return False


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True