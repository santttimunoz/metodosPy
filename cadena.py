mensaje = "     Bienvenidos ...  al curso de python     "

#metodo len, impirme el tamño de longitud del string(los espacios son careacteres que tambien cuentan)

print("el tamaño del texto es de ", len(mensaje))

#el metodo strip, quita los espacios al inicio y al final del string

mensaseStrip = mensaje.strip()
print("texto sin espacios al principio y al final ", mensaseStrip)
print("el tamaño del texto es de ", len(mensaseStrip))

#el metodo upper convierte el todos los caracteres del string a mayuscula
mayus = mensaje.upper()
print("mensaje en mayuscula ", mayus)

#el metodo lower convierte el todos los caracteres del string a minuscula
minus = mensaje.lower()
print("mensaje en minusculas", minus)

#el metodo title convierte la inicial de cada palabra en mayuscula
tittle = mensaje.title()
print("metodo title aplicado", tittle)

#el metodo capitalize convierte solo la primera inicial de la cadena a mayuscula
capit = mensaseStrip.capitalize()
print("metodo capitalize aplicado", capit)

#el metodo split divide las palabras en un arrglo de string
spplit = mensaje.split("...")
print("metodo split aplicado ", spplit)
print(spplit[1])
 # "control a" selecciona todo
