import random
list_food = ["морозиво", "шоколадки", "тістечка", "печиво"]

print(random.choice(list_food))

import pickle
user_data = {'login':'asassin2000ru','password':'qwerty','email':'asassin2000ru@gmail.com'}
file = open('save.dat','wb')
pickle.dump(user_data,file)
file.close

file = open('save.dat','rb')
user_data2 = pickle.load(file)
file.close()
print(user_data2)