#las listas son datos que son mutables y pueden cambiar 
modulos = ["logica", "python", "html", "css", "123"]

#el metodo append agrega un elemento al final de la lista
elemento = modulos.append("webI")

print("elemento inicial de modulos ",modulos[0])
print("elemento inicial de modulos ",modulos[-1])
#el metodo len muestra la cantidad de elementos que tiene una lista
print("numero de elemento que tiene la lista = ",modulos[len(modulos)-1])
elemento2 = modulos.append("metodologia agiles")
print("nuevo elemento agregado = ", modulos[-1])

#el metodo insert agrega un elemento y lo pone en la posicion deseada
elemento3 = modulos.insert(0, "java")
print(f'elemenot "{modulos[5]}" agregado en la pocision 0')

#el metodo count cuenta la cantidad de veces que se repite un dato
elemento4 = modulos.count("css")
print("numeor de veces que se repite css = ",elemento4)

#el metodo sort ordena los elementos de la lista en orden alfabetico(solo oredena strings)
modulos.sort()
print(modulos)

#esto seria el equivalente a un foreach en otros lenguajes
i = 0
for indice in modulos:
    print(i, indice)
    i+=1