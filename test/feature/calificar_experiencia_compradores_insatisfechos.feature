# Created by Jackson at 27/01/2024
# language: es

Característica: Permitir a mis compradores insatisfechos calificar su experiencia
  Como vendedor
  quiero permitir a mis compradores insatisfechos calificar su experiencia después del proceso de compra de un producto
  para aprender de los resultados y mejorar la satisfacción de mis clientes

  Escenario: Cliente insatisfecho califica su experiencia
    Dado que un Cliente ha "Finalizado" el Proceso de Compra
    Cuando el Cliente envíe una valoración negativa del Producto
    Entonces el Producto será negativamente catalogado, como por ejemplo: "Producto defectuoso" o "Producto con percanse".