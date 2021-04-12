#-- TIENDA DE BARRIO --# 

from objetos.articulo import Articulo
from objetos.cliente import Cliente
from objetos.factura import Factura

def rellenarDatos():

    clientes = []
    facturas = []
    articulos = []
    
    # --- ARTICULOS ---
    articulo_1 = Articulo(
        id = 1,
        nombre = 'Papas 100gr', 
        valor = 1500
    )

    articulo_2 = Articulo(
        id = 2,
        nombre = 'Salsa Tomate',
        valor = 3000
         
    )

    articulo_3 = Articulo(
        id = 3,
        nombre = 'Cereal',
        valor = 9750
    )
    
    articulos.append(articulo_1)
    articulos.append(articulo_2)
    articulos.append(articulo_3)
    
    # --- CLIENTES ---
    cliente_1 = Cliente(
        id = 1,
        nombre = 'Juan Sebastian', 
        documento = 123
    )

    cliente_2 = Cliente(
        id = 2,
        nombre = 'Pedro Lopez',
        documento = 124
         
    )

    cliente_3 = Cliente(
        id = 3,
        nombre = 'Maria Hernandez',
        documento = 125
    )
    
    clientes.append(cliente_1)
    clientes.append(cliente_2)
    clientes.append(cliente_3)
    
    # --- FACTURAS ---
    factura_1 = Factura(
        id = 1,
        cliente_id = cliente_1.id,
        articulo_id = [articulo_1.id, articulo_2.id],
        total = articulo_1.valor + articulo_2.valor
    )

    factura_2 = Factura(
        id = 2,
        cliente_id = cliente_2.id,
        articulo_id = [articulo_1.id, articulo_3.id],
        total = articulo_1.valor + articulo_3.valor
         
    )

    factura_3 = Factura(
        id = 3,
        cliente_id = cliente_3.id,
        articulo_id = [articulo_2.id, articulo_3.id],
        total = articulo_2.valor + articulo_3.valor
    )
    
    facturas.append(factura_1)
    facturas.append(factura_2)
    facturas.append(factura_3)
    
    return {
        'clientes' : clientes,
        'articulos' : articulos,
        'facturas': facturas,
    }
    
    
# Rellenar datos
data = rellenarDatos()
print('---- MENU --- ')
opcion = 1
index_cliente = 1
index_factura = 1
index_articulo = 1
while opcion != '0':
    print('selecciona una opcion: ')

    print('''
    1) Agregar Articulo
    2) Agregar Articulo al Carrito
    3) Ver Factura
    9) Imprimir lista de articulos
    0) Salir

    ''')
    try:
        opcion = input('ingresa la opcion que deseas realizar: ')
        if opcion == '1':
            # Agregar Articulo
            
            nombre = input('ingresa el nombre del articulo: ')
            valor = input('ingresa un valor para el articulo')
            articulo = Articulo(index_articulo, nombre, valor)
            data.get('articulos').append(articulo)
    
            index_articulo += 1
        
        if opcion == '2':
            # Agregar articulo al carrito
            
            documento_cliente = input('ingrese su numero de documento: ')
            nombre_articulo = input('ingresa el nombre del producto que desea agregar: ')
            articulo_id = None
            clienteid_agregar = None
            articulo_agregar = None
            factura_agregar = None
            for articulo in data.get('articulos'):
                if articulo.nombre == nombre_articulo:
                    articulo_agregar = articulo
            for cliente in data.get('clientes'):
                if documento_cliente == cliente.documento:
                    clienteid_agregar = cliente_id
            for factura in data.get('facturas'):
                if factura.cliente_id == clienteid_agregar:
                    factura_agregar = factura
            data.get('facturas').append(factura)
            index_factura += 1

        if opcion == '9':
            # Imprimir articulos 
            print('-- Articulos --')
            for articulo in data.get('articulos'):
                print(articulo.nombre)
                print('')
                print('')

        else:
            print('Ingrese una opcion valida')
    except:
        pass
print('-- se acabo de ejecutar todo el codigo--')    