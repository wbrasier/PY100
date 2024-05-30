info = {'name': 'Srdjan', 'age': 38}

print("Unknown" if 'city' not in info else info['city'])

print(info.get('city', 'Unknown'))