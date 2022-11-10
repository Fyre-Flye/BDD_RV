# Created by ddn at 08/11/2022
Feature: calculadora de números inteiros
  # Enter feature description here

  Scenario: somar dois números
    Given o primeiro operador da soma 3
    And o segundo operador da soma 2
    When eu somar os dois operadores
    Then o resultado da soma deve ser 5

  Scenario Outline: somar dois números
    Given o primeiro operador da soma <operador1_soma>
    And o segundo operador da soma <operador2_soma>
    When eu somar os dois operadores
    Then o resultado da soma deve ser <resultado_soma>

    Examples:
    |operador1_soma |operador2_soma | resultado_soma |
    |4              | 5             | 9              |
    |28             | 2             | 30             |

  Scenario: subtrair dois números
    Given o primeiro operador da subtração 5
    And o segundo operador da subtração 2
    When eu substrair os dois operadores
    Then o resultado da subtração deve ser 3

  Scenario Outline: subtrair dois números
    Given o primeiro operador de substração <operador1_sub>
    And o segundo operador de substração <operador2_sub>
    When eu substrair os dois operadores
    Then o resultado da subtração deve ser <resultado_sub>

    Examples:
    |operador1_sub |operador2_sub | resultado_sub|
    |9             | 5            | 4            |
    |10            | 5            | 5            |

  Scenario: multiplicar dois números
    Given o primeiro operador da multiplicacao 2
    And o segundo operador da multiplicacao 2
    When eu multiplicar os dois operadores
    Then o resultado da multiplicacao deve ser 4

  Scenario Outline: multiplicar dois números
    Given o primeiro operador da multiplicacao <operador1_mul>
    And o segundo operador de multiplicacao <operador2_mul>
    When eu multiplicar os dois operadores
    Then o resultado da multiplicacao deve ser <resultado_mul>

    Examples:
    |operador1_mul |operador2_mul | resultado_mul|
    |9             | 9            | 81           |
    |5            | 5             | 25           |

  Scenario: dividir dois números
    Given o primeiro operador da divisao 10
    And o segundo operador da divisao 5
    When eu dividir os dois operadores
    Then o resultado da divisao deve ser 2

  Scenario Outline: dividir dois números
    Given o primeiro operador da divisao <operador1_div>
    And o segundo operador da divisao <operador2_div>
    When eu dividir os dois operadores
    Then o resultado da divisao deve ser <resultado_div>

    Examples:
    |operador1_div |operador2_div | resultado_div|
    |15            | 3            | 5            |
    |20            | 2            | 10           |

  Scenario: elevar numero em n
    Given a base da potencia 2
    And a potencia e 3
    When eu elevar a base a potencia
    Then o resultado da potencia deve ser 8

  Scenario Outline: elevar numero em n
    Given a base da potencia <operador1_pot>
    And a potencia e <n_pot>
    When eu elevar a base a potencia
    Then o resultado da potencia deve ser <resultado_pot>

    Examples:
    |operador1_pot |n_pot | resultado_pot|
    |9             |2     | 81           |
    |2             |1     | 2            |

