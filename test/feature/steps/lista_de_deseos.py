from behave import *

use_step_matcher("re")


@step("que un Cliente selecciona un Producto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que un Cliente selecciona un Producto')


@step("el Cliente agregue el Producto a una Lista de deseos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando el Cliente agregue el Producto a una Lista de deseos')


@step("el sistema informará al Cliente que el Producto ha sido agregado exitosamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Entonces el sistema informará al Cliente que el Producto ha sido agregado exitosamente')


@step("que un Cliente ha agregado al menos un Producto en su Lista de deseos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que un Cliente ha agregado al menos un Producto en su Lista de deseos')


@step("el Cliente ingrese a su Lista de deseos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando el Cliente ingrese a su Lista de deseos')


@step(
    "el sistema mostrará al Cliente todos los productos que han sido agregados a la Lista de deseos, en orden descendente dependiento del más al menos recientemente agregado\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Entonces  el sistema mostrará al Cliente todos los productos que han sido agregados a la Lista de deseos, en orden descendente dependiento del más al menos recientemente agregado.')