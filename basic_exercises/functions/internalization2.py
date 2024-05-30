language_greetings = {
    'en' : {'US': 'Hey!', 'GB': 'Hello!', 'AU': 'Howdy!'},
    'fr' : 'Salut!',
    'pt' : 'Olá!',
    'de' : 'Hallo!',
    'sv' : 'Hej!',
    'af' : 'Haai!'
}

def greet(language, dialect = None):
  if language == 'en': 
    return language_greetings[language][dialect]
  else:
    return language_greetings[language]

def extract_language(locale):
  return locale[0:2]

def extract_dialect(locale):
  return locale[3:5]

def local_greet(locale):
  language = extract_language(locale)
  if language == 'en':
    dialect = extract_dialect(locale)
    return greet(language, dialect)
  
  return greet(language)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!