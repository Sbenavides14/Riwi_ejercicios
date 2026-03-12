frutas = ["manzana", "peras", "naranja", "uvas", "piña"]
print(frutas)
frutas.append("durazno")
print(frutas)
frutas.insert(1,"mandarina")
print(frutas)
frutas.remove("uvas")
print(frutas)
frutas.pop(2)
print(frutas)

numeros = [4,2,7,2,9,1,2]
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
print(numeros.count(2))
print(numeros.index(7))


lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_3 = []
lista_3 = lista_1.copy()
print(lista_3)
lista_3.extend(lista_2)
print(lista_3)

lista_estudiantes = ["mateo", "nick", "victor", "miguel", "joiner"]
print(lista_estudiantes)
lista_estudiantes.clear()
print(lista_estudiantes)

persona = {"nombre": "Duvan","edad": 25, "ciudad": "Miami"}
print(persona["nombre"])
edad = persona.get("edad")
print(edad)
print(persona.get("telefono", "no existe"))

persona["profesion"] = "medico"
print(persona)
persona["edad"] = 18
print(persona)
ciudad_eliminada = persona.pop("ciudad")
print(ciudad_eliminada)
print(persona)

productos = {"tv": 100, "ventilador": 75, "cafetera": 50}
print(productos.keys())
print(productos.values())
print(productos.items())

diccionario_1 = {"a": 1, "b": 2}
diccionario_2 = {"b": 5, "d": 4}
diccionario_1.update(diccionario_2)
print(diccionario_1)

elementos = {"carro": "azul", "moto": "roja", "barco": "verde", "avion": "blanco"}

elemento_eliminado = elementos.popitem()
print(elemento_eliminado)
print(elementos)

alumnos = [{"nombre": "matias", "nota": 2.8 }, {"nombre": "thomas", "nota": 4.8}, {"nombre": "yaser", "nota": 3.9}]

for alumno in alumnos:
    print(alumno['nombre'])

    suma_notas = 0
for alumno in alumnos:
    suma_notas = suma_notas + alumno['nota']

print(suma_notas/len(alumnos))

# print(sum(alumno['nota'] for alumno in alumnos)/len(alumnos))

for alumno in alumnos:
    if alumno['nota'] > 4:
        print(alumno.get('nombre','no existe'))