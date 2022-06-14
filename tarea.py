def crearCursada():
  # Crea una cursada con materias dentro
  cursada = [] # Creamos la cursada
  return cursada # Devolvemos la cursada


def agregarMateria(cursada, nombre, codigo):
  # Crea el arreglo de materia y codigo
  materia = [nombre, codigo]
  cursada.append(materia) # Añade la materia a la cursada
  
def eliminarMateria(cursada, codigo):
  # Saca una materia de la cursada
  for i in range(0,len(cursada)):
    for j in range(0, len(cursada[i])):
      # print(cursada[i][j])
      if (cursada[i][j] == codigo):
        print(cursada[i][j])
        print(cursada[i])

#  for (i = 0; i < cursada.length; i++): #Bucle que me permite sacar materias de cursada usando su codigo
#	  for(j = 0; i < cursada[i].length; j++):
#    	if (cursada[i][j] == codigo):
#        materia_borrada = cursada.pop(i)#POP elimina y retorna un elemento de la lista
#  return materia_borrada


cursada22 = crearCursada()
print(cursada22)

agregarMateria(cursada22, "Física", 123)
agregarMateria(cursada22, "Lengua", 223)

print(cursada22)

eliminarMateria(cursada22, 123)
print(cursada22)