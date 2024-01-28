from behave import *

use_step_matcher("re")


@step('que un Cliente ha "Finalizado" el Proceso de Compra')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que un Cliente ha "Finalizado" el Proceso de Compra')


@step("el Cliente envíe una valoración negativa del Producto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando el Cliente envíe una valoración negativa del Producto')


@step('el Producto será negativamente catalogado, como por ejemplo: "Producto defectuoso" o "Producto con percanse"\.')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Entonces el Producto será negativamente catalogado, como por ejemplo: "Producto defectuoso" o "Producto con percanse".')