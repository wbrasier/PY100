pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

def get_noise(animal):
  if animal in pets:
    print(pets[animal])
  else:
    print('<silence>')
  
get_noise('Cat')
get_noise('Lizard')