some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

def is_list(obj):
  return type(obj) == list
  
print(is_list(some_value1))
print(is_list(some_value2))