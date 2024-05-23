my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

new_set = {name: len(name) for name in my_set if len(name) % 2 != 0}

print(new_set)