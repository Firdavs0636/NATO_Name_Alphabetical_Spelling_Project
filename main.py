list = [1, 2, 3, 4, 5]
names = ['Firdavs', 'Abbos', 'Bekzod', 'Temurxon', 'Azizxon', 'Tima', 'Karl']

new_list = [name.upper() for name in names if len(name) > 5]
print(new_list)
