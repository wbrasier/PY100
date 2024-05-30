def starts_with(string, prefix):
  return string.startswith(prefix)
  
def starts_with_first_attempt(string, prefix):
  removed = string.removeprefix(prefix)
  if removed == string:
    return False
  return True


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True