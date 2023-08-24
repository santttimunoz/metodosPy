#las tuplas son datos de no son mutables y no pueden ser cambiados
#son una forma de proteger la informacion contra sobreescritura


tupla = ("santiago", "programacion avanzada", [4.5, 3.5])
#el metodo index permite mostrar la primera pocision en que un elemento se repite
print(tupla)
print(tupla.index("santiago"))

#el metodo count permite ver la cantidad de veces que se repite un dato en la tupla
print(tupla.count("santiago"))

print("cantidad de elementos de la lista = ", len(tupla))

for indice in tupla:
    print(indice)