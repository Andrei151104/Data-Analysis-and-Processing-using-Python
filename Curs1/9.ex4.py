
from functools import reduce

lista = [10,2,30,50,30]

#Versiunea 1
print(sum(lista)/len(lista))

#Versiunea 2
print(reduce(lambda x,y:x+y,lista))

print(reduce(lambda x,y:x+y,lista)/reduce(lambda x,y:x+y, map(lambda x:1 ,lista)))
