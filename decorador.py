# Ejercicio decoradores

def prevet_error(f):
    def wrapper(*args, **kwargs):
        try:
          f(*args, **kwargs)
        except: 
          print('ocurrio un error')
    return wrapper


@prevet_error
def dummy_code(nota_1, nota_2):
  prom = nota_1 + nota_2 /nota_2
  print(prom)

dummy_code(5, 0)


# Error de prevencion indice de una lista que no existe #

@prevet_error
def dummy_code2(lista):
  respuesta = lista[10]
  print(respuesta)

lista = ['hola','mundo']
dummy_code2(lista)

# Error de prevencion de un valor null #


@prevet_error
def dummy_code3(valor):
  respuesta = valor*valor
  print(respuesta)

valor = None
dummy_code3(valor)