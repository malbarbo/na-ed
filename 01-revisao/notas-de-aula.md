---
# vim: set spell spelllang=pt_br:
title: Revisão
# TODO: falar de variáveis e tipos explicitamente
# TODO: falar de modificação de parâmetros
---

Introdução
==========

## Introdução

Antes de começarmos o conteúdo da disciplina, vamos fazer uma revisão: \pause

- Processo de projeto de programas \pause

- A linguagem Python \pause

- Projeto de programas em Python



Projeto de programas
====================

## Projeto de programas

Quais são as principais atividades no projeto de um programa? \pause

- Análise (identificação o problema) \pause

- Especificação (descrição do que o programa deve fazer) \pause

- Implementação \pause

- Verificação (a implementação atende a especificação?)


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

- Tipos primitivos de dados \pause

- Operações primitivas \pause

- Definição de novas operações \pause

- Estruturas de controle \pause

- Definição de novos tipos de dados


## Instalação

O Python é um software livre e pode ser baixado e instalado de <https://python.org>. \pause

Apesar do Python vir com um ambiente de desenvolvimento e aprendizado chamado IDLE, nessa disciplina não vamos usá-lo. \pause

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
>>> # Esperávamos obter exatamente
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


## Formas de expressões

Inicialmente as expressões que vimos usavam apenas operadores matemáticos \pause

```python
30 * 2
```

\pause

Depois vimos que as expressões podem conter chamadas de funções \pause

```python
round(3.5)
```

\pause

e chamadas de métodos

```python
'José'.lower()
```

\pause

Por fim, vimos que strings podem ser indexadas \pause

```python
'veja isso'[2:6]
```


## Formas de expressões

Embora a forma de utilizar operadores, funções, métodos e indexação seja diferente, o propósito dessas construções é o mesmo: computar valores de saída a partir de valores de entrada.


## Formas de expressões

<div class="columns">
<div class="column" width="50%">
![](imagens/operacoes-entrada-saida.pdf){width=6cm}
\pause
</div>
<div class="column" width="50%">
\small
Se o propósito é o mesmo, por que não usar a mesma forma? \pause

Por conveniência! \pause

Por exemplo, se não tivéssemos a forma de operadores e apenas a forma de chamada de funções, então deveríamos escrever

```python
from operator import add, mull
add(mul(30, 2), 3)
```

ao invés de `30 * 2 + 3`{.python}, o que seria inconveniente. \pause

Além da conveniência de escrita, a forma de chamada métodos e indexação tem outras vantagens, vamos discutir isso ao longo da disciplina.
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
>>> 'Abacaxi' < 'Abacate'
False
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

Quem tem maior prioridade, o `and`{.python} ou o `or`{.python}? \pause O `and`{.python}.

\small

```python
>>> True or False and False
True
```

\pause


```python
>>> # É equivalente a expressão anterior
>>> True or (False and False)
True
```

\pause


```python
>>> # Se o or tivesse prioridade...
>>> (True or False) and False
False
```


## Listas

Os arranjos em Python são dinâmicos, isto é, podem mudar de tamanho, e são representados pelo tipo `list`{.python}.


## Listas - inicialização e indexação

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
>>> # Inicialização
>>> x: list[int] = [9 + 1, 1, 7, 2]
>>> x
[10, 1, 7, 2]
```

\pause

```python
>>> # Lista vazia
>>> y = [] # ou list()
>>> y
[]
```

\pause

```python
>>> # Número de elementos
>>> len(x)
4
>>> len(y)
0
```

\pause

</div>
<div class="column" width="48%">

\footnotesize

```python
>>> # Indexação
>>> nomes = ['Maria', 'João', 'Paulo']
>>> nomes[1]
'João'
>>> # Acesso fora da faixa
>>> nomes[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

\pause

```python
>>> # Sublistas
>>> x = [4, 1, 5, 7, 3]
>>> x[:2]
[4, 1]
>>> x[2:]
[5, 7, 3]
```

</div>
</div>


## Listas - alteração, acréscimo e concatenação

<div class="columns">
<div class="column" width="45%">

\footnotesize

```python
>>> # Substituição de um elemento
>>> y = [4, 2]
>>> y[1] = 7
>>> y
[4, 7]
```

\pause

```python
>>> # Acrésimo de um elemento
>>> y.append(5) # list.append(y, 5)
>>> y
[4, 7, 5]
>>> y.append(3)
>>> y
[4, 7, 5, 3]
```

\pause

```python
>>> # Concatenação
>>> [1, 2, 3] + [4, 5]
[1, 2, 3, 4, 5]
```


## Aprendizagem de uma nova linguagem


- ~~Tipos primitivos de dados~~

- ~~Operações primitivas~~

- Definição de novas operações

- Estruturas de controle

- Definição de novos tipos de dados


## Definições de funções

A forma geral para definição de funções em Python é:

\small

```python
def nome(entrada1: tipo, entrada2: tipo, ...) -> tipo:
    instruções
    return exp
```


## Definições de funções

\small

```python
def soma_quadrados(a: int, b: int) -> int:
    '''Calcula a soma de *a* ao quadrado e *b* ao quadrado'''
    a2 = a ** 2
    return a2 + b * b
```


\pause

Uso da nova função

```python
>>> soma_quadrados(3, 4)
25
```


## Aprendizagem de uma nova linguagem

- ~~Tipos primitivos de dados~~

- ~~Operações primitivas~~

- ~~Definição de novas operações~~

- Estruturas de controle

- Definição de novos tipos de dados


## Seleção

A forma geral do `if else`{.python} é:

\small

```python
if condição:
    instruções então
else:
    instruções senão
```

## Exemplo seleção

<div class="columns">
<div class="column" width="48%">
\small

```python
def maximo(a: int, b: int) -> int:
    '''
    Devolve o valor máximo
    entre *a* e *b*.
    '''
    if a > b:
        m = a
    else:
        m = b
    return m
```

</div>
<div class="column" width="48%">

\pause

Exemplos

\small

```python
>>> maximo(10, 8)
10
>>> maximo(-2, -1)
-1
```

</div>
</div>


## Seleção aninhada

<div class="columns">
<div class="column" width="48%">
\footnotesize

```python
def maximo3(a: int, b: int, c: int) -> int:
    '''
    Encontra o valor máximo entre
    *a*, *b* e *c*.
    '''
    if a >= b and a >= c:
        m = a
    else:
        if b >= a and b >= c:
            m = b
        else: # c >= a and c >= b
            m = c
    return m
```

</div>
<div class="column" width="48%">

\footnotesize

```python
def maximo3(a: int, b: int, c: int) -> int:
    '''
    Encontra o valor máximo entre
    *a*, *b* e *c*.
    '''
    if a >= b and a >= c:
        m = a
    elif b >= a and b >= c:
        m = b
    else: # c >= a and c >= b
        m = c
    return m
```

</div>
</div>


## Repetição com "para cada"

A forma geral do "para cada" é \pause

\small

```python
for var in lista:
    instruções
```

\pause

\normalsize

O "para cada" funciona da seguinte maneira: \pause

- O primeiro valor de `lista` é atribuído para `var` e as `instruções` são executadas; \pause
- O segundo valor de `lista` é atribuído para `var` e as `instruções` são executadas; \pause
- ... \pause
- E assim por diante até que todos os valores de `lista` tenham sidos atribuídos para `var`. \pause

Ou seja, o "para cada" executa as mesmas instruções atribuindo cada valor de `lista` para `var`, por isso ele chama "para cada"!


## Exemplo do "para cada"

\small

```python
>>> for x in [6, 1, 4, 5]:
...     print(x)
```

\pause

```python
6
1
4
5
```


## Exemplo do "para cada"

<div class="columns">
<div class="column" width="45%">
\small

```python
def soma(lst: list[int]) -> int:
    '''Soma os elementos de *lst*.'''
    soma = 0
    for n in lst:
        soma = soma + n
    return soma
```

\pause

</div>
<div class="column" width="50%">

Exemplos

\small

```python
>>> soma([])
0
>>> soma([3])
3
>>> soma([3, 7])
10
>>> soma([3, 7, 2])
12
```
</div>
</div>


## Exemplo de execução passa a passo do "para cada"

<div class="columns">
<div class="column" width="48%">
\footnotesize

```{.python .number-lines}
def soma(lst: list[int]) -> int:
    soma = 0
    for n in lst:
        soma = soma + n
    return soma

soma([5, 1, 4])
```

</div>
<div class="column" width="48%">
Qual é a ordem que as linhas são executadas? \pause

\footnotesize

7, \pause 2 (`soma = 0`{.python}), \pause

3 (`n = 5`{.python}), \pause 4 (`soma = 5`{.python}), \pause

3 (`n = 1`{.python}), \pause 4 (`soma = 6`{.python}), \pause

3 (`n = 4`{.python}), \pause 4 (`soma = 10`{.python}), \pause

3 (identifica que não tem mais elementos), \pause 5 (devolve `10`{.python}), \pause

7
</div>
</div>


## Repetição com "para cada no intervalo"

Podemos escrever o "para cada" com a seguinte forma alternativa: \pause

\small

```python
for var in range(inicio, fim):
    instruções
```

\pause

\normalsize

O funcionamento dessa forma é a seguinte: \pause

- `var` é inicializado com `inicio` \pause
- Se `var < fim`, as `instruções` são executadas, `var` é incrementado de `1`{.python} e esse processo é executado novamente \pause
- Senão, o "para cada" é finalizado \pause

O valor `inicio` pode ser omitido, nesse caso, `var` é inicializado com `0`{.python}.


## Exemplo do "para cada no intervalo"

<div class="columns">
<div class="column" width="48%">
\small

```python
>>> for i in range(3, 7):
...     print(i)
```

\pause

```python
3
4
5
6
```

\pause

</div>
<div class="column" width="48%">

\small

```python
>>> lst = [4, 1, 5, 2]
>>> for i in range(len(lst)):
...     print(i, lst[i])
```

\pause

```python
0 4
1 1
2 5
3 2
```
</div>
</div>


## Exemplo do "para cada no intervalo"

Função que soma os valores de uma lista

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
def soma(lst: list[int]) -> int:
    soma = 0
    for n in lst:
        soma = soma + n
    return soma
```

</div>
<div class="column" width="48%">

\footnotesize

```python
def soma(lst: list[int]) -> int:
    soma = 0
    for i in range(len(lst)):
        soma = soma + lst[i]
    return soma
```

</div>
</div>

\normalsize

\ 

Qual das duas formas é mais simples? \pause A da esquerda!


## Exemplo do "para cada no intervalo"

Função que encontra o índice da primeira ocorrência do valor máximo de uma lista não vazia.

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def indice_maximo(lst: list[int]) -> int:
    assert len(lst) != 0
    i = 0
    imax = 0
    for n in lst:
        if n > lst[imax]:
            imax = i
        i = i + 1
    return imax
```

</div>
<div class="column" width="48%">

\scriptsize

```python
def indice_maximo(lst: list[int]) -> int:
    assert len(lst) != 0
    imax = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[imax]:
            imax = i
    return imax
```

</div>
</div>

\ 

Qual das duas soluções é mais simples? \pause A da direita! \pause


## Repetição com "enquanto"

A forma geral do `while`{.python} é: \pause

\small

```python
while condição:
    instruções
```

\pause

\normalsize

O funcionamento do `while`{.python} é o seguinte: \pause

- A `condição` é avaliada \pause

- Se ela for `True`{.python}, as `instruções` são executadas e o processo se repete \pause

- Senão, o `while`{.python} termina


## Exemplos do "enquanto"

<div class="columns">
<div class="column" width="48%">
\small

```python
>>> i = 4
>>> while i < 10:
...     print(i)
...     i = 2 * i
```

\pause

```python
4
8
```

\pause

</div>
<div class="column" width="48%">

\small

```python
>>> i = 0
>>> x = 12
>>> while x >= 3:
...     x = x - 3
...     i = i + 1
>>> i
```

\pause

```python
4
```
</div>
</div>


## Exemplo de execução passo a passo do "enquanto"

<div class="columns">
<div class="column" width="48%">

\footnotesize

```{.python .number-lines}
def nao_decrescente(lst: list[int]) -> bool:
    em_ordem = True
    i = 1
    while i < len(lst) and em_ordem:
        if lst[i - 1] > lst[i]:
            em_ordem = False
        i = i + 1
    return em_ordem

nao_decrescente([1, 3, 3, 2, 7, 8])
```

</div>
<div class="column" width="48%">
Qual é a ordem que as linhas são executadas? \pause

\small

10 \pause

2 (`em_ordem = True`{.python}) \pause

3 (`i = 1`{.python}) \pause

4 \pause, 5 \pause, 7 (`i = 2`{.python}) \pause

4 \pause, 5 \pause, 7 (`i = 3`{.python}) \pause

4 \pause, 5 \pause, 6 (`em_ordem = False`{.python}) \pause, 7 (`i = 4`{.python}) \pause

4 \pause

8 (produz `False`{.python})\pause

10

</div>
</div>


## Quando utilizar cada forma de repetição?

Para cada

- Quando queremos processar todos os elementos de uma sequência na ordem que eles aparecem

\pause

Para cada no intervalo

- Quando queremos processar um intervalo dos elementos de uma sequência; ou

- Quando precisamos dos índices dos elementos da sequência; ou

- Quando precisamos de uma sequência de números em progressão aritmética

\pause

Enquanto

- Quando o uso do "para cada" e do "para cada no intervalo" não são adequados


## Aprendizagem de uma nova linguagem

- ~~Tipos primitivos de dados~~

- ~~Operações primitivas~~

- ~~Definição de novas operações~~

- ~~Estruturas de controle~~

- Definição de novos tipos de dados


## Tipo de dado

Um **tipo de dado** é o conjunto de valores que uma variável pode assumir. \pause

Exemplos \pause

- `bool`{.python} $= \{$ `True`{.python} , `False`{.python} $\}$ \pause
- `int`{.python} = $\{\dots, -2, -1, 0, 1, 2, \dots \}$ \pause
- `float`{.python} = $\{\dots, -0.1, -0.0, 0.0, 0.1, \dots \}$ \pause
- `str`{.python} = $\{$ `''`{.python}, `'a'`{.python}, `'b'`{.python}, $\dots \}$


## Tipo de dados

Durante a etapa de definição de tipos de dados (do processo de projeto de funções) temos que determinar quais são as informações e como elas serão representadas. \pause

Algumas informações podem ser representas diretamente com os tipos primitivos da linguagem. Para outras informações, precisamos definir novos tipos de dados. \pause

Quais características são desejáveis no projeto/definição de um tipo de dado? \pause

- Que as informações válidas possam representadas.

- Que as informações inválidas não possam ser representadas.


## Tipos de dados

Em um programa de simulação precisamos representar a cor de um semáforo (que pode ser verde, vermelha ou amarela) e projetar uma função que indique qual deve ser a próxima cor de uma semáforo a partir da cor atual. \pause

Qual tipo de dados podemos utilizar? \pause

String é um tipo adequado? \pause Não, pois `'casa'`{.python} é uma string mas não representa uma informação (cor) válida. \pause

Como fazemos nesse caso? \pause Criamos um tipo enumerado.


## Tipos enumerados

Em um **tipo enumerado** todos os valores válidos para o tipo são enumerados explicitamente. \pause

A forma geral para definir tipos enumerados é

\small

```python
from enum import Enum, auto

class NomeDoTipo(Enum):
    VALOR1 = auto()
    ...
    VALORN = auto()
```


## Exemplo tipo enumerado

<div class="columns">
<div class="column" width="48%">
\small

```python
from enum import Enum, auto

class Cor(Enum):
    '''
    A cor de um semáforo
    de trânsito.
    '''
    VERDE = auto()
    VERMELHO = auto()
    AMARELO = auto()
```

\pause

</div>
<div class="column" width="48%">

\small

```python
>>> c = Cor.VERDE
>>> c
<Cor.VERDE: 1>
>>> c.value
1
>>> c.name
'VERDE'
>>> c == Cor.VERDE
True
>>> Cor.VERDE == Cor.VERMELHO
False
```
</div>
</div>


## Exemplo tipo enumerado

<div class="columns">
<div class="column" width="48%">

\footnotesize

```python
def proxima_cor(atual: str) -> str:
    '''
    Produz a próxima cor de uma semáfaro
    que está na cor *atual*.
    '''
    if atual == 'verde':
        proxima = 'amarelo'
    elif atual == 'amarelo':
        proxima = 'vermelho'
    elif atual == 'vermelho':
        proxima = 'verde'
    return proxima
```

```python
>>> proxima_cor('verde')
'amarelo'
```

</div>
<div class="column" width="48%">

\footnotesize

```python
def proxima_cor(atual: Cor) -> Cor:
    '''
    Produz a próxima cor de uma semáfaro
    que está na cor *atual*.
    '''
    if atual == Cor.VERDE:
        proxima = Cor.AMARELO
    elif atual == Cor.AMARELO:
        proxima = Cor.VERMELHO
    elif atual == Cor.VERMELHO:
        proxima = Cor.VERDE
    return proxima
```

```python
>>> proxima_cor(Cor.VERDE).name
'AMARELO'
```

</div>
</div>


## Tipos enumerados

Observe que o uso de tipo enumerado deixa a intenção do código mais clara:

- Entrada e saída do tipo `str`{.python} pode ser qualquer string!

- Entrada e saída do tipo `Cor`{.python} deixa claro quais valores são válidos.

\pause

O uso de tipo enumerado também permite a detecção de erros mais facilmente:

- Se digitarmos `'amarela'`{.python} ao invés de `'amarelo'`{.python} o programa ainda é "válido".

- Se digitarmos `Cor.AMARELA`{.python} ao invés de `Cor.AMARELO`{.python} o `mypy` identifica o erro.


## Tipos compostos

Em um determinado programa o tempo de uma atividade é medida em segundos, mas é preciso exibir esse tempo em horas, minutos e segundos. Para isso precisamos projetar uma função que converte uma quantidade de segundos para uma quantidade de horas, minutos e segundos equivalentes. \pause

Os segundos da entrada da função pode ser representados com um número inteiro positivo, mas como representar a saída (o tempo em h, m, s)?


## Tipos de dados

Vamos relembrar alguns tipos de dados que utilizamos até agora:

- Tipos atômicos pré-definidos na linguagem: `int, float, bool, str`{.python}
- Tipos enumerados definidos pelo usuário: `Cor`

\pause

Os tipos atômicos têm esse nome porque não são compostos por partes. \pause

Podemos criar novos tipos agregando partes (campos) de tipos já existentes. \pause

Uma forma de fazer isso é através de tipos compostos (estruturas).


## Tipos compostos

Um **tipo composto** é um tipo de dado composto por um conjunto fixo de campos com nome e tipo.

\pause

A forma geral para definir um tipo composto é

\small

```python
from dataclasses import dataclass

@dataclass
class NomeDoTipo:
    campo1: Tipo1
    ...
    campon: TipoN
```


## Exemplo tipos compostos

\small

Podemos definir um novo tipo para representar um tempo da seguinte forma

```python
@dataclass
class Tempo:
    '''
    Representa o tempo de duração de um evento.
    horas, minutos e segundos devem ser positivos.
    minutos e segundos devem ser menores que 60.
    '''
    horas: int
    minutos: int
    segundos: int
```

\pause

Assim como para definição de tipos enumerados, sempre vamos adicionar um comentário sobre o propósito do tipo.


## Exemplo tipos compostos

Para inicializar uma variável de um tipo composto, chamamos o construtor (função) para o tipo e especificamos os valores dos campos na ordem que eles foram declarados. \pause

\small

```python
>>> t1: Tempo = Tempo(0, 20, 10)
>>> t1
Tempo(horas=0, minutos=20, segundos=10)
```

\pause

```python
>>> # A anotação do tipo é opcional
>>> t2 = Tempo(4, 0, 20)
>>> t2
Tempo(horas=4, minutos=0, segundos=20)
```


## Exemplo tipos compostos

Como valores do tipo `Tempo` são compostos de outros valores (campos), podemos acessar e alterar cada campo de forma separada. \pause

<div class="columns">
<div class="column" width="48%">
\small

```python
>>> t1 = Tempo(0, 20, 10)
>>> t1.segundos
10
>>> t1.minutos
20
>>> t1.horas
0
```

\pause

</div>
<div class="column" width="48%">

\small

```python
>>> t1.horas = 3
>>> t1
Tempo(horas=3, minutos=20, segundos=10)
>>> # Podemos deixar o valor em um
>>> # estado inconsistente...
>>> t1.segundos = 70
Tempo(horas=3, minutos=20, segundos=70)
```

</div>
</div>


## Exemplo tipos compostos

<div class="columns">
<div class="column" width="55%">
\scriptsize

```python
def segundos_para_tempo(segundos: int) -> Tempo:
    '''
    Converte a quantidade *segundos* para o tempo
    equivalente em horas, minutos e segundos.
    A quantidade de segundos e minutos da resposta
    é sempre menor que 60.

    Requer que segundos seja não negativo.
    '''
    assert segundos >= 0
    h = segundos / 3600
    # segundos que não foram
    # convertidos para hora
    restantes = segundos % 3600
    m = restantes / 60
    s = restantes % 60
    return Tempo(h, m, s)
```

</div>
<div class="column" width="45%">

\scriptsize

Exemplos

```python
>>> segundos_para_tempo(160)
Tempo(horas=0, minutos=2, segundos=40)
>>> segundos_para_tempo(3760)
Tempo(horas=1, minutos=2, segundos=40)
```

</div>
</div>


## Revisão

- ~~Processo de projeto de programas~~

- ~~A linguagem Python~~

- Projeto de programas na linguagem Python



Projeto de programas em Python
==============================

## Projeto de programas

O projeto de programa envolve:

- Análise (identificação o problema)

- Especificação (descrição do que o programa deve fazer)

- Implementação

- Verificação (a implementação atende a especificação?)


## Projeto de funções

Podemos detalhar esse processo para o projeto de uma função específica: \pause

- Análise: identificar o problema a ser resolvido \pause

- Definição dos tipos de dados: identificar e definir como as informações serão representadas \pause

- Especificação: especificar com precisão o que a função deve fazer \pause

- Implementação: implementar a função de acordo com a especificação \pause

- Verificação: verificar se a implementação está de acordo com a especificação \pause

- Revisão: identificar e fazer melhorias


## Projeto de funções em Python

O que é específico da linguagem e ainda não vimos como fazer em Python é:

- Especificação

- Verificação


## Especificação

O que é a especificação? \pause

Uma descrição precisa do que a função faz (deve fazer). \pause

Note que escrevemos a especificação **antes de fazer a implementação**. \pause

Como fazer a implementação se não sabemos exatamente o que precisa ser feito!?


## Especificação em Python

<div class="columns">
<div class="column" width="48%">

A especificação de uma função consiste de \pause

- Assinatura (nome, entradas e saída) \pause
- Propósito (o que a função deve fazer / faz) \pause
- Exemplos \pause

Em Python, escrevemos o propósito e os exemplos em um comentário dentro da função. \pause

Vamos escrever a especificação de uma função que calcula a quantidade de vezes que um inteiro aparece em uma lista. \pause

</div>
<div class="column" width="48%">

\footnotesize

```python
def conta(lst: list[int], n: int) -> int:
    '''
    Conta a quantidade de vezes que o
    valor de *n* aparece em *lst*.

    Exemplos
    >>> conta([], 3)
    0
    >>> conta([5, 1, 3], 3)
    1
    >>> conta([4, 1, 2, 4], 4)
    2
    '''
    return 0
```

</div>
</div>

\footnotesize

Note que para o código ficar bem formado deixamos um `return`{.python} com um valor padrão.


## Propósito

O que escrever no propósito? \pause

No propósito escrevemos **o que** a função deve fazer / faz. \pause

Devemos usar o nome dos parâmetros na descrição do propósito para que a relação da entrada e da saída fique clara. \pause

Para diferenciar o nome do parâmetro de uma palavra "normal", colocamos um asterisco antes e depois do nome do parâmetro: \pause


```python
   '''
   Conta a quantidade de vezes que o valor de *n* aparece em *lst*.
   '''
```


## Propósito

No propósito também escrevemos as **restrições** da entrada. Por exemplo, em uma função que encontra o valor máximo de uma lista, a lista não pode ser vazia: \pause

\small

```python
def maximo(lst: list[int]) -> int:
    '''
    Encontra o valor máximo de *lst*.

    Requer que *lst* não seja vazia.
    '''
    return 0
```


## Propósito

A seguir discutimos alguns **erros comuns** na escrita do propósito.


## Erros comuns na escrita do propósito

Escrever **como** a função faz ao invés de escrever **o que** a função faz: \pause

```python
   '''
   Analisa cada elemento de *lst* e soma 1 em um contador
   caso o elemento seja igual a *n*. No final, devolve
   o contador.
   '''
```

\pause

Isto é como a função faz e pode ser visto na implementação, não é preciso "narrar" o que está na implementação! \pause

Compare com o que a função faz:

```python
   '''
   Conta a quantidade de vezes que o valor de *n* aparece em *lst*.
   '''
```


## Erros comuns na escrita do propósito

Normalmente existe mais de uma forma de implementar uma função, e para usar uma função, em geral, é mais útil saber o que a função faz do que como a função faz. \pause

Vamos ver ao longo da disciplina a importância de separar a interface (o que) da implementação (como).


## Erros comuns na escrita do propósito

Não referenciar os parâmetros. \pause

```python
   '''
   Conta quantas vezes um número aparece em uma lista.
   '''
```

\pause

Qual Número? Qual lista?


## Erros comuns na escrita do propósito

Usar palavras desnecessárias. \pause

```python
   '''
   A função conta...

   Esta função...
   '''
```


## Erros comuns na escrita do propósito

Usar verbo no infinitivo. \pause

```python
   '''
   Contar quantas vezes...
   '''
```

\pause

A função não contar, a função conta!


## Exemplos

Qual o propósito dos exemplos? \pause

O primeiro propósito é ajudar o projetista a entender como a saída será determinada a partir das entradas. \pause Por isso escrevemos os exemplos **antes de fazer a implementação**. \pause

Depois os exemplos são usados como parte da verificação.


## Exemplos

Como escrever os exemplos? \pause

O exemplos são escritos na forma de uma sessão iterativa do Python. Uma linha que inicia com `>>>` indica uma instrução, as seguintes (até uma linha sem nada) indicam a reposta esperada:

\small

```python
    '''
    Exemplos
    >>> conta([], 3)
    0
    >>> conta([5, 1, 3], 3)
    1
    >>> conta([4, 1, 2, 4], 4)
    2
    '''
```


## Exemplos

Quantos exemplos escrever? \pause

Pelo menos um exemplos para cada "forma" de calcular a saída. \pause

Note que devemos evitar escrever muitos exemplos "iguais". Por exemplo, para uma função que indica se um número natural é par ou ímpar, basta fazer um ou dois exemplos de número par e ímpar, não é preciso fazer cinco exemplos de números pares.


## Verificação em Python

O que é a verificação? \pause

É o processo para determinar se a implementação está de acordo com a especificação. \pause

A verificação pode ser: \pause

- Estática: sem executar o programa \pause

- Dinâmica: executando o programa


## Verificação estática

Apesar de ser possível provar, usando verificação estática, que um programa está de acordo com a sua especificação, este processo é custoso e inviável para a maioria dos programas. \pause

No entanto, podemos usar a verificação estática para identificar diversas inconsistências entre a especificação e a implementação, principalmente em relação aos tipos de dados. \pause

Para fazer a verificação estática dos tipos vamos utilizar o programa [`mypy`](https://mypy-lang.org/).


## Verificação estática

Instalação do `mypy`:

```
pip install mypy
```

\pause

Execução do `mypy`:

```
mypy arquivo.py
```


## Verificação estática

<div class="columns">
<div class="column" width="48%">
\scriptsize

```{.python .number-lines}
def conta(lst: list[int], n: int) -> int:
    '''
    Conta a quantidade de vezes que o
    valor de *n* aparece em *lst*.

    Exemplos
    >>> conta([], 3)
    0
    >>> conta([4, 1, 2, 4], 4)
    2
    '''
    vezes = 0.0
    for x in lst:
        if x == n:
            vezes = vezes + 1
    return vezes
```

</div>
<div class="column" width="48%">

\scriptsize

```
conta.py:16: error: Incompatible return
value type (got "float", expected "int")
Found 1 error in 1 file (checked 1 source file)
```

</div>
</div>


## Verificação dinâmica

Existem muitas estratégias de verificação dinâmica, a que vamos utilizar inicialmente é verificar se chamadas de funções com entradas específicas produzem as saídas esperadas (que já é conhecida). \pause

Como já temos exemplos de entradas e saídas na especificação, podemos usar inicialmente esses exemplos para fazer a verificação dinâmica. \pause

O módulo `doctest`{.python}, que já vem com o Python, analisa os comentários das funções, identifica e executa automaticamente os exemplos indicando caso haja divergências entre os valores esperados e os valores obtidos com a execução dos exemplos. \pause

Execução do `doctest`:

```
python -m doctest -v arquivo.py
```


## Verificação dinâmica

<div class="columns">
<div class="column" width="48%">
\scriptsize

```{.python .number-lines}
def conta(lst: list[int], n: int) -> int:
    '''
    Conta a quantidade de vezes que o
    valor de *n* aparece em *lst*.

    Exemplos
    >>> conta([], 3)
    0
    >>> conta([4, 1, 2, 4], 4)
    2
    '''
    vezes = 0
    for x in lst:
        if x == n:
            vezes = vezes + 10
    return vezes
```

</div>
<div class="column" width="48%">

\scriptsize

```
Trying:
    conta([4, 1, 2, 4], 4)
Expecting:
    2
***************************************
File "conta.py", line 9, in conta.conta
Failed example:
    conta([4, 1, 2, 4], 4)
Expected:
    2
Got:
    20
1 items had no tests:
    conta
***************************************
1 items had failures:
   1 of   2 in conta.conta
2 tests in 2 items.
1 passed and 1 failed.
***Test Failed*** 1 failures.
```

</div>
</div>

## Verificação dinâmica

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def conta(lst: list[int], n: int) -> int:
    '''
    Conta a quantidade de vezes que o
    valor de *n* aparece em *lst*.

    Exemplos
    >>> conta([], 3)
    0
    >>> conta([4, 1, 2, 4], 4)
    2
    '''
    vezes = 0
    for x in lst:
        if x == n:
            vezes = vezes + 1
    return vezes
```

</div>
<div class="column" width="48%">

\scriptsize

```
Trying:
    conta([], 3)
Expecting:
    0
ok
Trying:
    conta([4, 1, 2, 4], 4)
Expecting:
    2
ok
1 items had no tests:
    conta
1 items passed all tests:
   2 tests in conta.conta
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

</div>
</div>


Continua
========
