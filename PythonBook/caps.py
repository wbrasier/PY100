def cap_if_over_10(string):
  return(string.upper() if len(string) >=10 else string)

print(cap_if_over_10('hello there'))
print(cap_if_over_10('less'))