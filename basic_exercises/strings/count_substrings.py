def count_substrings(string, sub):
  if sub not in string: return 0
  return string.count(sub)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0