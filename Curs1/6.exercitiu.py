
lista = [10,2,30,50,300,10]

# Versiunea 1
def lungime_5(alta_lista):
    return alta_lista > 5

print(list(filter(lungime_5 ,lista)))
    
# Versiunea 2
print(list(filter(lambda x:x>5,lista)))

# Versiunea 3 - list comprehention
# print[element for element in lista if element > 5]