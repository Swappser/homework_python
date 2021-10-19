import random

def f(name, otchestvo, surname, k):
    i = 0
    while i < k:
        full_name = random.choice(name) + ' ' + random.choice(otchestvo) + ' ' + random.choice(surname)
        i += 1
        yield full_name

for i in f(['Oleg', 'Alex', 'Nikita'],['Ivanovich','Olegovich'],['Hodov', 'Borov'], 3):
    print(i)