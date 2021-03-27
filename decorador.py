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