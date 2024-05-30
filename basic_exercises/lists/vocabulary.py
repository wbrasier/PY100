vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]


for x in vocabulary:
  if len(x) > 1:
    for y in x:
      print(y)
  else:
    print(x)