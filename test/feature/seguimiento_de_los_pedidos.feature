# Created by Jackson at 27/01/2024
# language: es

Característica: : Hacer un seguimiento de los pedidos
  Como vendedor
  quiero obtener información de las entregas que hayan tenido retrasos o que no fueron entregados
  para reducir la presencia de defectos de calidad dentro del proceso de entrega de mis Pedidos

  Escenario: : Envío de pedidos con retraso
    Dado que un Pedido fue entregado con retraso a un Cliente
    Cuando el Vendedor ingrese a la lista los Pedidos realizados
    Entonces el Vendedor podrá obtener las estadísticas de los Pedidos entregados con retraso

  Escenario: : Envío de pedidos que no fueron entregados
    Dado que un Pedido no fue entregado a un Cliente
    Cuando el Vendedor ingrese a la lista los Pedidos realizados
    Entonces el Vendedor podrá obtener las estadísticas de los Pedidos que no fueron entregados