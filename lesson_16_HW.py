#1
# d = {'name': 'John Doe', 'age': 30, 'city': 'New York', 'email': 'johndoe@exemple.com'}
# delete = input('Введите значение для удаления: ')
#
# print(d.pop(delete))
# print(d)

#2
# d = {'name': 'Alice Smith', 'age': 25, 'city': 'LA', 'email': 'alice.smith@exemple.com', 'favorite_subjects': ['Maths', 'History', 'Literature']}
#
# for i in d.pop('favorite_subjects'):
#     print(d)

#3
favorites = {'movies': ['Interstellar', 'Fast & Furious', 'Pirates of the Caribbean'], 'music': ['Queen', 'The Beatles', 'Coldplay'], 'sports': ['football', 'basketball', 'tennis']}
print(favorites.setdefault('serials', ['one', 'second', 'lost']))
print(favorites)
