class Factura():
    id = ''
    cliente_id = ''
    articulo_id = ''
    total = ''
    
    def __init__(self, id, cliente_id, articulo_id, total):
        self.id = id
        self.cliente_id = cliente_id
        self.articulo_id = articulo_id
        self.total = total
    
    def obtenerClientes(self, clientes):
        mi_cliente = None
        for cliente in clientes:
            if cliente.id == self.cliente_id:
                mi_cliente = cliente
        
        return mi_cliente

    def obtnerArticulo(self, articulos):
        mi_articulo = None
        for articulo in articulos:
            if articulo.id == self.articulo_id:
                mi_articulo = articulo
        return mi_articulo
    
    def obtenerTotal(self, articulos):
        mi_total = None
        for articulo in articulos:
            mi_total += articulo.valor
        return mi_total
