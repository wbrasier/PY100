string = 'launch school tech & talk'

arr = string.split()
arr = [word.capitalize() for word in arr]
string = ' '.join(arr)
print(string)