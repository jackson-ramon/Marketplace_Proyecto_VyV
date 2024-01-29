from behave import *
from modelos.modelos import *

use_step_matcher("re")

@step('que un Cliente ha "Finalizado" el Proceso de Compra')
def step_impl(context):
    context.cliente = Cliente("nombre", "apellido", "fecha_nacimiento", "email" )
    context.herramienta = Herramienta("martillo", "precio")

    context.cliente.agregar_herramienta_carrito(context.herramienta)
    proceso_compra_martillo = context.cliente.comprar_herramienta(context.herramienta)

    assert( proceso_compra_martillo.estado_compra == "RECIBIDO")


@step("el Cliente envíe una valoración negativa del Producto")
def step_impl(context):

    context.valoracion = context.cliente.valorar_herramienta(context.herramienta, Valoracion.BAD)

    assert( context.valoracion < 2 )


@step('el Producto será negativamente catalogado, como por ejemplo: "Producto defectuoso" o "Producto con percanse"\.')
def step_impl(context):
    context.herramienta.catalogar_producto()
    assert(context.herramienta.catalogacion == Catalogacion_herramienta.MALA)