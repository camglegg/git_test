catNames = []
while True:
    print('Enter the name of a cat '+str(len(catNames)+1)+ ' (Or Enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print("The cat's names are: ")
for name in catNames:
    print(' ' + name)