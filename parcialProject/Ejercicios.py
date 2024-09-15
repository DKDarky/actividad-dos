# Conversión de tipos de datos

# Variables iniciales
entero = 10
decimal = 3.14
cadena = "20"

# Conversión de cadena a entero
entero_desde_cadena = int(cadena)
print("Conversión de cadena a entero:", entero_desde_cadena)

# Conversión de entero a decimal
decimal_desde_entero = float(entero)
print("Conversión de entero a decimal:", decimal_desde_entero)

# Conversión de decimal a entero (perderá la parte decimal)
entero_desde_decimal = int(decimal)
print("Conversión de decimal a entero:", entero_desde_decimal)

# Conversión de decimal a cadena
cadena_desde_decimal = str(decimal)
print("Conversión de decimal a cadena:", cadena_desde_decimal)

# Conversión de entero a cadena
cadena_desde_entero = str(entero)
print("Conversión de entero a cadena:", cadena_desde_entero)

# Conversión de cadena a decimal
decimal_desde_cadena = float(cadena)
print("Conversión de cadena a decimal:", decimal_desde_cadena)


# Multilíneas de cadenas

# Uso de comillas triples para definir una cadena multilínea
cadena_multilinea = """Esta es una cadena
que abarca varias líneas.
Puedo escribir lo que quiera
y no necesito preocuparme
por agregar saltos de línea."""

print("Cadena multilínea:")
print(cadena_multilinea)

# Uso de comillas triples para definir una cadena multilínea con indentación
cadena_multilinea_indentada = """
    Esta es una cadena
    que abarca varias líneas
    y tiene indentación.
    Puedo escribir lo que quiera
    y no necesito preocuparme
    por agregar saltos de línea."""

print("\nCadena multilínea con indentación:")
print(cadena_multilinea_indentada)

# Uso de la barra invertida (\) para agregar saltos de línea
cadena_con_saltos = "Esta es una cadena que abarca varias líneas.\n" \
                    "Puedo escribir lo que quiera y no necesito preocuparme\n" \
                    "por agregar saltos de línea."

print("\nCadena con saltos de línea:")
print(cadena_con_saltos)

# Función len()

# Cadena
cadena = "Hola, mundo!"
print("Longitud de la cadena:", len(cadena))

# Lista
lista = [1, 2, 3, 4, 5]
print("Longitud de la lista:", len(lista))

# Tupla
tupla = (1, 2, 3, 4, 5)
print("Longitud de la tupla:", len(tupla))

# Diccionario
diccionario = {"nombre": "Juan", "apellido": "Pérez", "edad": 30}
print("Longitud del diccionario:", len(diccionario))


def obtener_primeros_n_caracteres(cadena, n):
  """Obtiene los primeros n caracteres de una cadena.

  Args:
    cadena: La cadena de la que se quieren obtener los caracteres.
    n: El número de caracteres a obtener.

  Returns:
    Los primeros n caracteres de la cadena.
  """
  return cadena[:n]

def obtener_caracteres_del_medio(cadena):
  """Obtiene los caracteres del medio de una cadena.

  Args:
    cadena: La cadena de la que se quieren obtener los caracteres.

  Returns:
    Los caracteres del medio de la cadena.
  """
  longitud = len(cadena)
  medio = longitud // 2
  return cadena[medio - 1:medio + 1]

def obtener_ultimos_n_caracteres(cadena, n):
  """Obtiene los últimos n caracteres de una cadena.

  Args:
    cadena: La cadena de la que se quieren obtener los caracteres.
    n: El número de caracteres a obtener.

  Returns:
    Los últimos n caracteres de la cadena.
  """
  return cadena[-n:]

# Ejemplo de uso
cadena = "Hola Mundo"

# Obtener los primeros 5 caracteres
primeros_5 = obtener_primeros_n_caracteres(cadena, 5)
print("Primeros 5 caracteres:", primeros_5)

# Obtener los caracteres del medio
medio = obtener_caracteres_del_medio(cadena)
print("Caracteres del medio:", medio)

# Obtener los últimos 3 caracteres
ultimos_3 = obtener_ultimos_n_caracteres(cadena, 3)
print("Últimos 3 caracteres:", ultimos_3)

#Funcion Upper
my_string = "hello world"
try:
    print(my_string.upper())
except AttributeError:
    print("Error: The variable is not a string.")


#funcion lower

my_string = "HELLO WORLD"
try:
    print(my_string.lower())
except AttributeError:
    print("Error: The variable is not a string.")



#Multilíneas de cadenas de caracteres.

multiline_string = """This is a multiline string
that spans across multiple lines
and is very useful for formatting text."""

print(multiline_string)

# or

string1 = "This is the first line"
string2 = "This is the second line"
multiline_string = string1 + "\n" + string2
print(multiline_string)

# or

strings = ["This is the first line", "This is the second line"]
multiline_string = "\n".join(strings)
print(multiline_string)


#Función strip().
string = "+++Hello, World!+++"
stripped_string = string.strip("+")
print(stripped_string)  # Output: "Hello, World!"


#Función replace().

string = "Hello, World!"
new_string = string.replace("World", "Universe")
print(new_string)  # Output: "Hello, Universe!"


#Función split().

string = "Hello, World! Python,is,awesome"
words = string.split(",", 2)
print(words)  # Output: ["Hello, World! Python", "is", "awesome"]


#Formato de cadenas F-String.

name = "John"
age = 30
print(f"Hello, {name}! You are {age} years old.")
# Output: "Hello, John! You are 30 years old."

x = 5
y = 3
print(f"The result of {x} + {y} is {x + y}.")
# Output: "The result of 5 + 3 is 8."

name = "John"
print(f"{name:>10}")  # Right-align the name in a field of width 10
# Output: "      John"

pi = 3.14159
print(f"The value of pi is {pi:.2f}.")  # Format pi to 2 decimal places
# Output: "The value of pi is 3.14."

