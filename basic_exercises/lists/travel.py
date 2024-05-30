destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(x, collection):
  return collection.count(x) >= 1

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations)) # False