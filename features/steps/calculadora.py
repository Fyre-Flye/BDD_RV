from behave import *

from scr.calc import Calculadora

# Soma --------------------------------------

@given("o primeiro operador da soma 3")
def set_op1_soma(context):
    context.op1 = 3

@step("o segundo operador da soma 2")
def set_op2_soma(context):
    context.op2 = 2

@when("eu somar os dois operadores")
def somar(context):
    calc = Calculadora()
    context.resultado = calc.somar(context.op1,context.op2)

@then("o resultado da soma deve ser 5")
def resultado_soma(context):
    assert context.resultado == 5

@given("o primeiro operador da soma {operador1_soma}")
def set_operador1_soma(context, operador1_soma):
    context.op1 = int(operador1_soma)

@step("o segundo operador da soma {operador2_soma}")
def set_operador2_soma(context, operador2_soma):
    context.op2 = int(operador2_soma)

@then("o resultado da soma deve ser {resultado_soma}")
def resultado_soma(context, resultado_soma):
    assert context.resultado == int(resultado_soma)

# Subtração ---------------------------

@given("o primeiro operador da subtração 5")
def set_op1_sub(context):
    context.op1 = 5

@step("o segundo operador da subtração 2")
def set_op2_sub(context):
    context.op2 = 2

@when("eu substrair os dois operadores")
def substrair(context):
    calc = Calculadora()
    context.resultado = calc.subtrair(context.op1,context.op2)

@then("o resultado da subtração deve ser 3")
def result_sub(context):
    assert context.resultado == 3

@given("o primeiro operador de substração {operador1_sub}")
def set_operador1_sub(context, operador1_sub):
    context.op1 = int(operador1_sub)

@step("o segundo operador de substração {operador2_sub}")
def set_operador2_sub(context, operador2_sub):
    context.op2 = int(operador2_sub)

@then("o resultado da subtração deve ser {resultado_sub}")
def resultado_sub(context, resultado_sub):
    assert context.resultado == int(resultado_sub)

# Mul ---------------------------

@given("o primeiro operador da multiplicacao 2")
def set_op1_mul(context):
    context.op1 = 2

@step("o segundo operador da multiplicacao 2")
def set_op2_mul(context):
    context.op2 = 2

@when("eu multiplicar os dois operadores")
def multiplicar(context):
    calc = Calculadora()
    context.resultado_mul = calc.multiplicar(context.op1,context.op2)

@then("o resultado da multiplicacao deve ser 4")
def result_mul(context):
    assert context.resultado_mul == 4

@given("o primeiro operador da multiplicacao {operador1_mul}")
def set_operador1_mul(context, operador1_mul):
    context.op1 = int(operador1_mul)

@step("o segundo operador de multiplicacao {operador2_mul}")
def set_operador2_mul(context, operador2_mul):
    context.op2 = int(operador2_mul)

@then("o resultado da multiplicacao deve ser {resultado_mul}")
def resultado_mul(context, resultado_mul):
    assert context.resultado_mul == int(resultado_mul)

# Div ---------------------------

@given("o primeiro operador da divisao 10")
def set_op1_div(context):
    context.op1 = 10

@step("o segundo operador da divisao 5")
def set_op2_div(context):
    context.op2 = 5

@when("eu dividir os dois operadores")
def dividir(context):
    calc = Calculadora()
    context.resultado_div = calc.dividir(context.op1,context.op2)

@then("o resultado da divisao deve ser 2")
def result_div(context):
    assert context.resultado_div == 2

@given("o primeiro operador da divisao {operador1_div}")
def set_operador1_div(context, operador1_div):
    context.op1 = int(operador1_div)

@step("o segundo operador da divisao {operador2_div}")
def set_operador2_div(context, operador2_div):
    context.op2 = int(operador2_div)

@then("o resultado da divisao deve ser {resultado_div}")
def resultado_div(context, resultado_div):
    assert context.resultado_div == int(resultado_div)

# Pot ---------------------------

@given("a base da potencia 2")
def set_base_op1(context):
    context.op1 = 2

@step("a potencia e 3")
def set_n_pot(context):
    context.n_pot = 3

@when("eu elevar a base a potencia")
def potencia(context):
    calc = Calculadora()
    context.resultado_pot = calc.potencia(context.op1, context.n_pot)

@then("o resultado da potencia deve ser 8")
def result_pot(context):
    assert context.resultado_pot == 8

@given("a base da potencia {operador1_pot}")
def set_base_op1(context, operador1_pot):
    context.op1 = int(operador1_pot)

@step("a potencia e {n_pot}")
def set_n_por(context, n_pot):
    context.n_pot = int(n_pot)

@then("o resultado da potencia deve ser {resultado_pot}")
def resultado_pot(context, resultado_pot):
    assert context.resultado_pot == int(resultado_pot)
