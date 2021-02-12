ingridient1 = "Паучьи лапки"
ingridient2 = "Волшебная палочка"
ingridient3 = "Крыло летучей мыши"
wizard_list = ["Паучьи лапки", "Волшебная палочка",
               "Крыло летучей мыши"]
print(wizard_list)
wizard_list.append('Язык улитки')
wizard_list.append('3')
print(wizard_list)
print(wizard_list[2:5])

numbers = [1, -3, 5, 10, -15]
allin = ['Serg', 5, 'Крыло мыши']

del wizard_list[1]
print(wizard_list)
wizard_list.remove('Крыло летучей мыши')
print(wizard_list)
wizard_list2 = ['Крыло летучей мыши','Волшебная палочка']
print(wizard_list + wizard_list2)
print(wizard_list * 2)
#print(numbers[2:3] / 2)