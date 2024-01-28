from behave import *

use_step_matcher("re")


@step("que un Pedido fue entregado con retraso a un Cliente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que un Pedido fue entregado con retraso a un Cliente')


@step("el Vendedor ingrese a la lista los Pedidos realizados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando el Vendedor ingrese a la lista los Pedidos realizados')


@step("el Vendedor podrá obtener las estadísticas de los Pedidos entregados con retraso")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Entonces el Vendedor podrá obtener las estadísticas de los Pedidos entregados con retraso')


@step("que un Pedido no fue entregado a un Cliente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que un Pedido no fue entregado a un Cliente')


@step("el Vendedor podrá obtener las estadísticas de los Pedidos que no fueron entregados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Entonces el Vendedor podrá obtener las estadísticas de los Pedidos que no fueron entregados')