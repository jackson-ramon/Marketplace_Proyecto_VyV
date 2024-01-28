# Created by Jackson at 27/01/2024
# language: es

Característica: : Gestionar lista de deseos
  Como Cliente
  quiero una lista de deseos con productos de mi interés
  para ahorrar tiempo al organizar mis opciones y revisarlas más tarde

  Escenario: : Cliente interesado en un Producto
    Dado que un Cliente selecciona un Producto
    Cuando el Cliente agregue el Producto a una Lista de deseos
    Entonces el sistema informará al Cliente que el Producto ha sido agregado exitosamente

  Escenario: : Cliente interesado en ver su Lista de deseos
    Dado que un Cliente ha agregado al menos un Producto en su Lista de deseos
    Cuando el Cliente ingrese a su Lista de deseos
    Entonces  el sistema mostrará al Cliente todos los productos que han sido agregados a la Lista de deseos, en orden descendente dependiento del más al menos recientemente agregado.