language_greetings = {
    'en' : 'Hi!',
    'fr' : 'Salut!',
    'pt' : 'Olá!',
    'de' : 'Hallo!',
    'sv' : 'Hej!',
    'af' : 'Haai!'
}

def greet(language):
  return language_greetings[language]

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!