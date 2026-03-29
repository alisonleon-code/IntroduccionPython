# sep="***" cambia el separador (en vez de espacio usa ***)
# end="..." evita el salto de línea y en su lugar agrega "..."
print("Programming", "Essentials", "in", sep="***", end="...")

# Como el print anterior no hizo salto de línea,
# esto se imprime en la misma línea
print("Python")

# Se repite exactamente lo mismo otra vez
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")


# Imprime dos textos en la misma línea separados por espacio (por defecto)
# end=" " evita el salto de línea y agrega un espacio al final
print("hola", "mi nombre es", end=" ")
print("Juan")# Continúa en la misma línea por el print anterior


# Imprime dos textos en la misma línea
# end=" " evita el salto de línea
print("mi nombre es", "pyton", end=" ")
print("monty python.")# Continúa en la misma línea


# \n dentro del texto genera un salto de línea
print("hola \nMonty python")


# sep="*" cambia el separador entre palabras por "*"
print("mi", "Nombre", "es", "monty", "pyton.", sep="*")


# sep="-" separa con guiones
# end=" Monty \n" agrega texto al final y luego un salto de línea
print("mi", "nombre", "es", sep="-", end=" Monty \n")


# sep="*" separa los elementos con "*"
print("mi", "apellido", "es", sep="*")

# Imprime "Python" y luego un salto de línea
print("Python\n")
