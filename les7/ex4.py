print( eval("10*5") )

#print( eval("if True: 10*5"))

sentence = input("Що обчислити? ")
print(eval( sentence) )

myProgram = "print('Hello, world')\nprint('my program')"
myProgram = '''print('Hello, world')
print('my program')'''
exec(myProgram)

text = "56"
number = int(text)
print(text * 2)
print(number * 2)
print( float(number) )
