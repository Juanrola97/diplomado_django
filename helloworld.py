
# Funciones basicas primera parte
def HelloWorld():
  print("Hello World!")
def suma(a,b):
      print(a+b)
def resta(a,b):
    print(a-b)
def multiplica(a,b):
    print(a*b)
def division(a,b):
    print(a/b)
def potencia(a,b):
    return a**b
def saludo(nombre):
    print("Hola " + nombre)
def despedida(nombre):
    print("Adios " + nombre)


HelloWorld()
suma(5, 5)
resta(10, 20)
multiplica(30, 20)
division(10, 20)
potencia(30, 20)
saludo("Juan")
despedida("Juan")


# Funcion compleja

# Funcion para calcular el pago de cesantias
def calcularCesantias(diasLaborados, salario, diasAgno):
    return (diasLaborados*salario)/diasAgno

diasLaborados = 191
salario = 1500000
diasAgno = 360
print("El valor de tus cesantias son: " + str(calcularCesantias(diasLaborados, salario, diasAgno)))

# Funcion para calcular posibles ahorros
def calcularPosibleAhorros(salario, gastos, porcentajeAhorrar):
    return (salario-gastos) * porcentajeAhorrar

salario = 1000000
gastos = 700000
porcentajeAhorrar = 0.5
print("Tus ahorros deseados son: " + str(calcularPosibleAhorros(salario, gastos,porcentajeAhorrar)))

    