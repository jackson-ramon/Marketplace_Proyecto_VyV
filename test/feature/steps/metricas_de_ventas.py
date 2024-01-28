from behave import *

use_step_matcher("re")


@step("que un Vendedor ha realizado al menos 20 ventas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que un Vendedor ha realizado al menos 20 ventas')


@step("el Vendedor ingresa a las métricas de ventas")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando el Vendedor ingresa a las métricas de ventas')


@step("el sistema mostrará una comparativa entre el crecimiento de ventas actual y los meses anteriores")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Entonces el sistema mostrará una comparativa entre el crecimiento de ventas actual y los meses anteriores')