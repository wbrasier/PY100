cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]
          
for elem in cities:
  if elem == None: continue
  print(len(elem))