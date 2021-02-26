bitcoin = 45000
print("Очень дорогой биткоин, подождем")
while ( bitcoin > 35000 ):
    bitcoin = bitcoin - 1
    print("Падает до : " + str(bitcoin)  )
print("О, цена подходит, куплю биткоин")

while( True ):  # бесконечный цикл
    bitcoin = bitcoin + 1
    print("Падает до : " + str(bitcoin))
