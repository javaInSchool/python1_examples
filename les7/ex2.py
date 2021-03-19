x = -4

print( abs(x) ) # якщо число >0 , то це саме число

steps = -3
if abs(steps) > 0:
    print("Персонаж йде вперед")

#boolean

print( bool(0) )
print( bool(1) )
print( bool('a'))

birthday = input("your birthday? ")

if not bool(birthday): # not and or
    print("Ви не вказали рік народження")