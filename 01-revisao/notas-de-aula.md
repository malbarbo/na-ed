---
# vim: set spell spelllang=pt_br:
title: Revisão
---

Introdução
==========

## Introdução

Antes de começarmos o conteúdo da disciplina, vamos fazer uma revisão: \pause

- Processo de projeto de programas \pause

- A linguagem Python \pause

- Projeto de programas na linguagem Python



Projeto de programas
====================

## Projeto de programas

Quais são as principais atividades no projeto de um programa? \pause

- Análise (identificar o problema) \pause

- Especificação (descrever o que o programa deve fazer) \pause

- Implementação (implementar o programa) \pause

- Verificação (verificar se a implementação atende a especificação)


## Projeto de funções

Podemos detalhar esse processo para o projeto de uma função específica: \pause

- Análise: identificar o problema a ser resolvido \pause

- Definição dos tipos de dados: identificar e definir como as informações serão representadas \pause

- Especificação: especificar com precisão o que a função deve fazer \pause

- Implementação: implementar a função de acordo com a especificação \pause

- Verificação: verificar se a implementação está de acordo com a especificação \pause

- Revisão: identificar e fazer melhorias


## Projeto de programas

Mas como projetar programas? \pause

Um programa é composto de várias funções, então decompomos o programa em funções e aplicamos esse processo para projetar cada função.


A linguagem Python
==================

## Como aprender uma nova linguagem?

Para aprender uma linguagem de programação, temos que, de maneira simplificada, aprender: \pause

- Quais os tipos primitivos de dados \pause

- Quais as operações primitivas \pause

- Como definir novos tipos de dados \pause

- Como definir novas operações


## Instalação

O Python é um software livre e pode ser baixado e instalado de <https://python.org>. \pause

Apesar do Python vir com um ambiente de desenvolvimento e aprendizado chamado IDLE, nessa disciplina vamos usá-lo. \pause

Para desenvolver os nossos programas vamos utilizar o [vscode](https://code.visualstudio.com/).


## Números

O Python tem diversos **tipos numéricos**, os dois principais são \pause

<div class="columns">
<div class="column" width="50%">

Inteiros (`int`{.python}) \pause

```python
>>> 102
102
>>> -18
-18
```

\pause

</div>
<div class="column" width="50%">

Ponto flutuante (`float`{.python}), representação aproximada de números reais \pause

```python
>>> 1.3
1.3
>>> 0.345
0.345
>>> # Notação científica
>>> 1.23e2 # 1.23 * 10^2
123.0
```

</div>
</div>


## Operações básicas

<div class="columns">
<div class="column" width="50%">

```python
>>> # Soma e subtração
>>> 4 + 2
6
>>> 4 + 2.0 - 5
1.0
```

\pause

```python
>>> # Multiplicação e divisão
>>> 3 * 5.0
15.0
>>> 7 / 2
3.5
```

\pause

```python
>>> # Divisão sempre produz float
>>> 8 / 4
2.0
```
</div>
<div class="column" width="50%">
\pause

```python
>>> # Piso da divisão
>>> 7 // 2
3
>>> 5 // 1.3
3.0
```

\pause

```python
>>> # Resto da divisão
>>> 14 % 3
2
>>> # Experávamos obter exatamente
>>> # 1.1, mas float é apenas
>>> # uma aproximação dos reais...
>>> 5 % 1.3
1.0999999999999999
```

</div>
</div>


## Exponenciação

```python
>>> # Exponenciação e radiciação
>>> 3 ** 4 # 3 elevado a 4
81
>>> 2 ** 80
1208925819614629174706176
>>> 16 ** 0.5 # raiz quadrada, o mesmo que 16 ** (1 / 2)
4.0
```

\pause

```python
>>> # A exponenciação tem prioridade sobre a divisão
>>> 27 ** 1 / 3 # o mesmo que (27 ** 1) / 3
9.0
>>> # Usamos parênteses para mudar a prioridade
>>> 27 ** (1 / 3) # raiz cúbica
3.0
```


## Conversão entre números

<div class="columns">
<div class="column" width="50%">

```python
>>> # Arredondamento
>>> round(3.4)
3
>>> round(3.5)
4
>>> round(3.5134, 2)
3.51
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Conversão entre int e float
>>> int(7.6)
7
>>> int(-2.3)
-2
>>> float(4)
4.0
```

</div>
</div>


## Piso e teto

<div class="columns">
<div class="column" width="50%">

```python
>>> import math
>>> # Piso
>>> # maior inteiro <= ao número
>>> math.floor(4.2)
4
>>> math.floor(4.0)
4
>>> math.floor(-2.3)
-3
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Teto
>>> # menor inteiro >= ao númeo
>>> math.ceil(4.2)
5
>>> math.ceil(4.0)
4
>>> math.ceil(-2.3)
-2
```

</div>
</div>


## Cadeia de caracteres

Outro tipo de dado pré-definido em Python é a cadeia de caracteres (`str`{.python}), _string_ em inglês. \pause

Uma string em Python é escrita entre apóstrofo (`'`{.python}) ou aspas (`"`{.python}) \pause

```python
>>> 'casa'
'casa'
>>> "gota d'agua"
"gota d'agua"
>>> "mesa"
'mesa'
```


## Operações com strings

Assim como existem operações pré-definidas para números, também existem operações pré-definidas para strings. \pause

<div class="columns">
<div class="column" width="50%">

```python
>>> # Concatenação
>>> 'casa' + ' da ' + 'sogra'
'casa da sogra'
```

\pause

```python
>>> # Repetição
>>> 'abc' * 3
'abcabcabc'
```

\pause

```python
>>> 'algum' * 0
''
>>> 'algum' * -4
''
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Quantidade de caracteres
>>> len('ciência da computação')
21
```

\pause

```python
>>> # Conversão maiúscula
>>> 'José'.upper() # ou str.upper('José')
'JOSÉ'
>>> # Conversão minúscula
>>> 'José'.lower() # ou str.lower('José')
'josé'
```

</div>
</div>


## Substrings

```python
>>> # Indexação de caractere
>>> # O primeiro caractere tem índice 0
>>> 'casa'[0] # ou str.__getitem__('casa', 0)
'c'
```

\pause

```python
>>> 'casa'[1]
'a'
```

\pause

```python
>>> # Acesso de índice fora do intervalo
>>> 'casa'[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```


## Substrings

```python
>>> # Substring do início até 3 - 1
>>> 'veja isso'[:3] # ou str.__getitem__('veja isso', slice(None, 3))
'vej'
```

\pause

```python
>>> # Substring de 4 até o final
>>> 'veja isso'[4:] # ou str.__getitem__('veja isso', slice(4, None))
' isso'
```

\pause

```python
>>> # Substring de 2 até 6 - 1
>>> 'veja isso'[2:6] # ou str.__getitem__('veja isso', slice(7, 9))
'ja i'
```


## Conversão entre strings e números

<div class="columns">
<div class="column" width="50%">

```python
>>> # Conversão de int para str
>>> str(127)
'127'
>>> # Conversão de float para str
>>> str(4.1)
'4.1'
```

\pause

```python
>>> # Concatenação de str e int
>>> 'Idade: ' + str(19)
'Idade: 19'
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Conversão de str para int
>>> int('127')
127
```

\pause

```python
>>> # Conversão de str para float
>>> float('25')
25.0
>>> float('12.67')
12.67
```

</div>
</div>


## Operações relacionais

<div class="columns">
<div class="column" width="50%">

```python
>>> # Maior e maior ou igual
>>> 4 > 4
False
>>> 4 >= 4
True
```

\pause

```python
>>> # Menor e menor ou igual
>>> 6.0 < 6.0
False
>>> 6.0 <= 1.0 + 5.0
True
```

\pause

</div>
<div class="column" width="50%">

```python
>>> # Igual
>>> 5 == 6
False
>>> 9 == 5 + 2 ** 2
True
```

\pause

```python
>>> # Diferente
>>> 3 * 2 != 4 + 2 ** 2
True
>>> 9 != 4 + 2 ** 2
False
```

</div>
</div>

\pause

\ 

Observe que as operações relacionais tem prioridade menor do que as operações aritméticas.


## Operações relacionais

As operações relacionais podem ser utilizadas com outros tipos, incluindo strings e booleanos. \pause

<div class="columns">
<div class="column" width="50%">

```python
>>> # As strings são comparadas
>>> # lexicograficamente, o
>>> # que pode gerar algumas
>>> # supressas
>>> 'a' < 'b'
True
>>> 'á' < 'b'
False
```

\pause

</div>
<div class="column" width="50%">
```python
>>> 'André' < 'Paulo'
True
>>> 'André' < 'paulo'
True
>>> 'casa' == 'Casa'
False
>>> 'á' != 'a'
True
```
</div>
</div>


## Operações relacionais

<div class="columns">
<div class="column" width="50%">

```python
>>> # O valor False é considerado
>>> # menor que o valor True
>>> False < True
True
>>> True > False
True
```

\pause

</div>
<div class="column" width="50%">

```Python
>>> False == False
True
>>> False == True
False
>>> True == False
False
>>> True == True
True
```

</div>
</div>


## Operadores booleanos

<div class="columns">
<div class="column" width="50%">

```python
>>> # O not é um operator unário.
>>> not True
False
>>> not False
True
>>> not not True
True
```

\pause

</div>
<div class="column" width="50%">

```Python
>>> # O not tem menor precedência
>>> # do que os operadores relacionais
>>> # e aritméticos.
>>> # 4 > 4.0 é False
>>> not 3 + 1 > 2 + 2.0
True
>>> # 14 == 14 é True
>>> not 2 + 3 * 4 == 14
False
```

</div>
</div>


## Operadores booleanos

<div class="columns">
<div class="column" width="50%">

```python
>>> # O and é um operador binário
>>> # que só produz True se os
>>> # dois operandos forem True.

>>> # Tabela verdade do and
>>> False and False
False
>>> False and True
False
>>> True and False
False
>>> True and True
True
```

\pause

</div>
<div class="column" width="50%">

```Python
>>> # O and tem menor precedência
>>> # do que os operadores relacionais
>>> # e aritméticos.

>>> # 15 > 8 é True
>>> # 4 == 3 é False
>>> 15 > 2 ** 3 and 4 == 1 + 2
False
>>> # 2 == 2 é True
>>> # 3 != 4 é True
>>> 2 == 1 + 1 and 3 != 4
True
```

</div>
</div>


## Operadores booleanos

<div class="columns">
<div class="column" width="50%">

```python
>>> # O or é um operador binário
>>> # que produz True se pelo menos
>>> # um dos operandos for True.

>>> # Tabela verdade do or
>>> False or False
False
>>> False or True
True
>>> True or False
True
>>> True or True
True
```

\pause

</div>
<div class="column" width="50%">

```Python
>>> # O or tem menor precedência
>>> # do que os operadores relacionais
>>> # e aritméticos.

>>> # 15 > 8 é True
>>> # 4 == 3 é False
>>> 15 > 2 ** 3 or 4 == 1 + 2
True
>>> # 2 == 3 é False
>>> # 3 + 1 != 4 é False
>>> 2 == 2 + 1 or 3 + 1 != 4
False
```

</div>
</div>


## Operadores relacionais

Quem tem maior prioridade, o `and`{.python} ou o `or`{.python}? \pause O `and`{.python}. \pause Vamos criar uma expressão que mostre que isso é verdade. \pause

\small

```python
>>> # A expressão é equivalente a
>>> # (False and False) or True
>>> # que produz True
>>> False and False or True
True
>>> # Se o or tivesse prioridade
>>> # sobre o and, então a expressão
>>> # seria equivalente a
>>> # False and (False or True)
>>> # que produz False
>>> False and (False or True)
False
```


## Definições de funções

A forma geral para definição de funções em Python é?

```python
def nome(entrada1: tipo, entrada2: tipo, ...) -> tipo:
    instruções...
    return exp
```

\pause

Vamos definir uma função que calcule o quadrado de um número inteiro.


## Definições de funções

```python
def quadrado(x: int) -> int:
    return x * x
```


Projeto de programas na linguagem Python
========================================

## Como projetar programas em uma linguagem?

Para projetar um programa em uma linguagem precisamos

- Uma forma de fazer a especificação \pause

- Uma forma de fazer a implementação \pause

- Uma forma de fazer verificação
