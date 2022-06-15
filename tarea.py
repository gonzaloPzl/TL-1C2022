# Función para crear la cursada
def crearCursada(): 
  cursada = [] # Creamos un arreglo vacio
  return cursada # Lo devolvemos

# Función para agregar una materia a una cursada
# De parámetro recibe la cursada, el nombre de la matería y el codigo de la matería
def agregarMateria(cursada, nombre, codigo): 
  materia = [nombre, codigo] # Crea un arreglo con el nombre y el codigo de la materia
  cursada.append(materia) # con append añade la materia a la cursada

# Función para eliminar una materia
def eliminarMateria(cursada, codigo):
  # Se inicializan las variables 
  eliminar = -1; # el indice de la materia en el la cursada a eliminar
  eliminado = False # Para saber si se pudo eliminar
  for i in range(0,len(cursada)): # Se iteran la cursada
    if (cursada[i][1] == codigo): # Si el código coincide entra
      eliminar = i; # Se le asigna el indice de la materia a la variable
  if (eliminar >= 0): # Si es mayor o igual a 0 entra
    cursada.pop(eliminar) # Se utiliza pop pasandole el indice para que lo elimine de cursada
    eliminado = True # Se cambia el valor a true porque se pudo eliminar
  return eliminado # Se retorna el valor de eliminado

# Función para saber si existe la materia
def exiteMateria(cursada, codigo): # De parametro recibe la cursada y el codigo de la materia
  # Se inicializa existe en false
  existe = False 
  # Se itera la cursada
  for i in range(0, len(cursada)):
    # Si existe la materia con ese codigo se cambia el valor de existe
    if (cursada[i][1] == codigo):
      existe = True
  # Se retorn el valor de existe (True o False)
  return existe

# Función para editar materia
def editarMateria(cursada, codigo,nombreNuevo,codigoNuevo):
  # Iteramos la cursada
  for i in range(0, len(cursada)):
    # Si el codigo de la cursada coincide con el pasado por parametro entramos
    if (cursada[i][1] == codigo):
      # Cambiamos los valores de la materia por los nuevos pasados por parametro
      cursada[i][0] = nombreNuevo
      cursada[i][1] = codigoNuevo
      # Devolvemos True 
      return True
  # Si no se encontro materia con ese codigo se retorna false
  return False

# Función que retorna el nombre o el codigo segun lo que le pasemos
def nombreOCodigo(cursada, dato):
  # Si como dato le pasamos el codigo, detecta que es int y entra acá
  if(isinstance(dato, int)):
    # iteramos la cursada
    for i in range(len(cursada)):
      # Si el codigo es igual al del dato entramos
      if(cursada[i][1] == dato):
        # Devolvemos el nombre de la materia
        return cursada[i][0]
  # En el caso de ser un tipo string entraria acá
  elif(isinstance(dato, str)):
    for i in range(len(cursada)):
      # Cuando encuentra el nombre de la materia devuelve el codigo
      if(cursada[i][0] == dato):
        return cursada[i][1]
  return False # Si no coincide ninguna de las 2 se devuelve false

# UTILIZACIÓN DEL TAD
cursada22 = crearCursada() # Creamos la cursada

# Agregamos las materias
agregarMateria(cursada22, "Física", 123)
agregarMateria(cursada22, "Lengua", 223)
agregarMateria(cursada22, "Historia", 213)

print(cursada22) # -> [['Física', 123], ['Lengua', 223], ['Historia', 213]]

# Preguntamos si existe la materia con el código 223
existeLaMateria = exiteMateria(cursada22, 223)
print(existeLaMateria) # -> True
# Preguntamos si existe con el codigo 000
existeLaMateria2 = exiteMateria(cursada22, 000)
print(existeLaMateria2) # -> False

# Editamos la materia 223(Lengua) para que se llame Literatura y tenga el codigo 322
editarMateria(cursada22, 223, "Literatura", 322)

print(cursada22) # -> [['Física', 123], ['Literatura', 322], ['Historia', 213]]

# Le pasamos el codigo 322 para saber a que materia pertenece
codigoANombre = nombreOCodigo(cursada22, 322)
print(codigoANombre) # -> Literatura
# Le pasamos el nombre para saber que codigo tiene
nombreACodigo = nombreOCodigo(cursada22, "Literatura")
print(nombreACodigo) # -> 322

# Eliminamos la materia con el código 322
eliminarMateria(cursada22, 322)
print(cursada22) # -> [['Física', 123], ['Historia', 213]]