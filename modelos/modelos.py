from enum import Enum
class Cliente:
    def __init__(self, nombre, apellido, fecha_nacimiento, email ):
        self.nombre = nombre
        self.apellidos = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.herramientas_carrito = []
        self.herramientas_compradas = []
    def agregar_herramienta_carrito(self, herramienta):
        self.herramientas_carrito.append(herramienta)

    def comprar_herramienta(self, herramienta):
        proceso = Proceso_compra(herramienta)
        if proceso.pagar_herramienta():
            self.herramientas_compradas.append(herramienta)
            self.herramientas_carrito.remove(herramienta)
        return proceso

    def valorar_herramienta(self, herramienta, valoracion):
        if valoracion in Valoracion:
            herramienta.agregarValoracion(valoracion)
        else:
            print("Error: Valoración no válida")
        return valoracion.value
class Catalogacion_herramienta(Enum):
    BUENA = "Producto en buenas condiciones"
    MALA = "Producto defectuoso"
    EMPTY = "No hay valoraciones"


class Valoracion(Enum):
    EXCELLENT = 4
    GOOD = 3
    NEUTRAL = 2
    BAD = 1
    AWFUL = 0

class Herramienta:
    def __init__(self, nombre_herramienta, precio_herramienta):
        self.nombre_herramienta = nombre_herramienta
        self.precio_herramienta = precio_herramienta
        self.valoraciones = []
        self.catalogacion = Catalogacion_herramienta

    def agregarValoracion(self, valoracion):
        self.valoraciones.append(valoracion)

    def obtener_calificacion_promedio(self):
        if self.valoraciones:
            return sum([valoracion.value for valoracion in self.valoraciones]) / len(self.valoraciones)
        else:
            return None
    def catalogar_producto(self):
        promedio = self.obtener_calificacion_promedio()

        if promedio is None:
            return Catalogacion_herramienta.EMPTY.value
        elif promedio >= 3.0:
            return Catalogacion_herramienta.BUENA.value
        else:
            return Catalogacion_herramienta.MALA.value


class EstadoCompra(Enum):
    EN_PROCESO = "En proceso"
    PAGADO = "Pagado"
    CANCELADO = "Cancelado"
    RECIBIDO = "Recibido"

class Proceso_compra:
    def __init__(self, herramienta):
        self.herramienta = herramienta
        self.estado_compra = EstadoCompra.EN_PROCESO

    def pagar_herramienta(self):
        #Pagar con tajerta
        self.estado_compra = EstadoCompra.PAGADO
        return True

    def cancelar_pedido(self):
        self.estado_compra = EstadoCompra.CANCELADO