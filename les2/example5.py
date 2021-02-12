fibonacci = (0,1,1,2,3,5,8)
print(fibonacci[3])
name1 = 'Serg'
names = (name1, 'Lesha')
print(names[0])

#fibonacci[3] = 6
print( fibonacci.index(8) )

favorite_games = [ 'Милана, Dangan', 'Леша, Minecraft',
                  'Уляна, BrawlStars','Марк, Super Smash',
                  'Миша, Fontnight',
                  'Никита, Майнкрафт ','Стас, WarThunder',
                  'Марк, WarThunder']
print(favorite_games[0])
favorite_games_v = { 'Милана':'Dangan',
                     'Леша': 'Minecraft',
                  'Уляна': 'BrawlStars',
                     'Марк': 'Super Smash',
                  'Миша':'Fontnight',
                  'Никита':'Майнкрафт ',
                     'Стас':'WarThunder',
                  'Марк_fake':'WarThunder'}
print(favorite_games_v['Уляна'])
favorite_games_v['Уляна'] = 'Minecraft'
#Составить строку из любимой книги, с переменной %s

#Составить список/кортеж/словарь любимых занятий