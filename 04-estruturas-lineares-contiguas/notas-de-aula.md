---
# vim: set spell spelllang=pt_br:
title: Estruturas de dados lineares
subtitle: Alocação contígua
linkcolor: Black
urlcolor: Blue
---

## Introdução

Uma **estrutura de dados** é uma forma de organizar e armazenar dados para facilitar a sua manipulação (operações). \pause

Usamos estruturas de dados para implementar TAD. \pause

A estrutura de dados mais adequada para implementar um TAD depende das operações e de como elas são utilizadas.


## Estrutura de dados lineares

Em uma **estruturas de dados linear**, os elementos são organizados de forma sequencial, um após o outro. \pause Cada elemento possui no máximo um predecessor e um sucessor.\pause

A estrutura de dados linear mais comum é o arranjo.


## Arranjos

As duas principais características dos arranjos são: \pause

- Os elementos são armazenados de forma contígua na memória, ou seja, em posições consecutivas. \pause

- Cada elemento do arranjo pode ser acessado diretamente em tempo constante. \pause

Os arranjos podem ser: \pause

- Estáticos: a quantidade de elementos não muda

- Dinâmicos: a quantidade de elementos pode mudar


## Arranjos estáticos em Python

O tipo `list`{.python} do Python é de fato um arranjo dinâmico. \pause

Diferente de outras linguagens, o Python não oferece um tipo pré-defino para arranjos estáticos. \pause

Por hora não vamos mais utilizar o tipo `list`{.python}, e sim o tipo `array`{.py}, definido na biblioteca `array` que está disponível na página da disciplina, que "simula" um arranjo de tamanho fixo.


## Arranjos estáticos em Python

<div class="columns">
<div class="column" width="40%">
\scriptsize

```python
>>> from array import array
>>> # Cria um arranjo com 5 zeros
>>> x: array[int] = array(5, 0)
>>> x
array([0, 0, 0, 0, 0])
>>> x[0] = 10
>>> x[4] = 2
>>> x
array([10, 0, 0, 0, 2])
>>> len(x)
5
>>> x[5]
Traceback (most recent call last):
...
IndexError: list index out of range
```

\pause

</div>
<div class="column" width="58%">

\scriptsize

```python
>>> soma = 0
>>> for v in x:
...     soma = soma + v
>>> soma
12
```

\pause

```python
>>> x.append(10)
Traceback (most recent call last):
...
AttributeError: 'array' object has no attribute 'append'
>>> x.pop()
Traceback (most recent call last):
...
AttributeError: 'array' object has no attribute 'pop'
```

</div>
</div>


## Conteúdo

A seguir veremos três TAD e como eles podem ser implementados usando arranjos. \pause

A apresentação de cada TAD é precedida de um exemplo de uso.


## Exemplo parênteses

Projete uma função que verifique se os parênteses em uma expressão aritmética (representada por uma string) estão corretos, isso é: \pause

- Cada `'('`{.python} tem um `')'`{.python} correspondente \pause

- Um `')'`{.python} não pode aparecer antes do `'('`{.python} correspondente


## Projeto

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def parenteses_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses de *expr*
    estão corretos, False caso contrário.
    '''
```

\pause

```python
    '''
    Exemplos:
    >>> parenteses_corretos('()')
    True
    >>> parenteses_corretos('(')
    False
    >>> parenteses_corretos(')')
    False
    >>> parenteses_corretos('())')
    False
    >>> parenteses_corretos('((a)*(b-c)-10)*((4-2)/8)')
    True
    '''
```

\pause

</div>
<div class="column" width="50%">

Ideia da implementação:

- Analisar a string um caractere por vez.
- Manter um contador de parênteses que foram abertos mas ainda não foram fechados.
- O contador é incrementado a cada abre parênteses e decrementado a cada fecha parênteses.
- O contador não pode ficar negativo.
- No final, se o contador for 0 e não ficou negativo, os parênteses estão corretos.

</div>
</div>


## Projeto

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def parenteses_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses de *expr*
    estão corretos, False caso contrário.
    '''
```


```python
    '''
    Exemplos:
    >>> parenteses_corretos('()')
    True
    >>> parenteses_corretos('(')
    False
    >>> parenteses_corretos(')')
    False
    >>> parenteses_corretos('())')
    False
    >>> parenteses_corretos('((a)*(b-c)-10)*((4-2)/8)')
    True
    '''
```

</div>
<div class="column" width="50%">

\scriptsize

```python
def parenteses_corretos(expr: str) -> bool:
    abertos = 0
    corretos = True
    i = 0
    while i < len(expr) and corretos:
        if expr[i] == '(':
            abertos = abertos + 1
        elif expr[i] == ')':
            abertos = abertos - 1
            if abertos < 0:
                corretos = False
        i = i + 1
    return abertos == 0 and corretos
```

</div>
</div>


## Exemplo agrupamento

Projete uma função que verifique se os parênteses, colchetes e chaves em uma expressão aritmética (representada por uma string) estão corretos. \pause


## Projeto

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def grupos_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses,
    colchetes e chaves de *expr*
    estão corretos, False caso contrário.

    Exemplos:
    >>> parenteses_corretos('([{}])')
    True
    >>> parenteses_corretos('[](){}')
    True
    >>> parenteses_corretos('({)}')
    False
    >>> parenteses_corretos('(2*[3*{5+2]})')
    False
    >>> parenteses_corretos('([a]*{b-c}-[10])*({(4-2)/8})')
    True
    '''
```

</div>
<div class="column" width="50%">

Usar um contador (ou mais) não é suficiente. Precisamos saber não apenas quantos "grupos" foram abertos e ainda não foram fechados, mas também qual é o tipo do grupo (parênteses, colchetes ou chaves). \pause

Ideia da implementação: \pause

- Analisar a string um caractere por vez.
- Matemos uma coleção com as ocorrências dos grupos que foram abertos mas ainda não foram fechados.
- Quando um caractere de início de grupo é encontrado ele é armazenado na coleção.
- Quando um caractere de fim de grupo é encontrado verificamos se ele fecha o grupo _mais recentemente aberto_.
- No final, se todos os grupos foram abertos e fechados corretamente, a expressão está correta.

</div>
</div>


## Pilha

Uma pilha é uma coleção de itens que segue a política LIFO (Last In, First Out), isto é, o elemento mais recentemente inserido na pilha é o primeiro a ser removido.


## Pilha

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
class Pilha:
    '''Uma coleção de strings que segue a
    política LIFO, o elemento mais recente-
    mente inserido é o primeiro a ser
    removido.'''

    def empilha(self, item: str):
        '''Adiciona o *item* ao topo da
        pilha.'''

    def desempilha(self) -> str:
        '''Devolve o elemento que está no topo
        da pilha.
        Requer que a pilha não esteja vazia.'''

    def vazia(self) -> bool:
        '''Devolve True se a pilha está vazia,
        False caso contrário.'''
```

\pause

</div>
<div class="column" width="50%">
\scriptsize

```python
>>> p = Pilha()
>>> p.vazia()
True
>>> p.empilha('O')
>>> p.empilha('que')
>>> p.empilha('escrever?')
>>> p.vazia()
False
```

\pause

```python
>>> p.desempinha()
```

\pause

```python
'escrever?'
>>> p.empinha('fazer')
>>> p.empinha('agora?')
```

\pause

```python
>>> while not p.vazia():
...    print(p.desempilha())
```

\pause

```python
agora?
fazer
que
O
```

</div>
</div>


## Exemplo agrupamento

Use uma pilha para fazer a implementação da função que verifica se os parênteses, colchetes e chaves em uma expressão aritmética estão corretos.

<!--

## Primos

Projete uma função que encontre todos os números primos menores que um determinado valor.


## Primos

<div class="columns">
<div class="column" width="50%">
Especificação

\scriptsize

```python
def primos(lim: int) -> list[int]:
    '''
    Encontra todos os números primos
    menores que *lim*.

    Exemplos:
    >>> primos(2)
    []
    >>> primos(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    '''
```

\pause

</div>
<div class="column" width="50%">
Implementação

\scriptsize

```python
def primos(lim: int) -> list[int]:
    primos = []
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
</div>


## Arranjos dinâmicos

Para implementar a função `primos` utilizamos o tipo `list`{.python}, que é pré-definido em Python.

\pause

Apesar de chamar `list`{.python}, conceitualmente esse tipo representa um arranjo dinâmico.

\pause

Algumas linguagens, como a C, não tem arranjo dinâmico pré-definido, apenas arranjo de tamanho fixo.

\pause

Como implementar um arranjo dinâmico em uma linguagem que só oferece arranjo de tamanho fixo?


## Arranjo

Vamos supor que ao invés de oferecer o tipo `list`{.python}, o Python oferece um tipo `array` (arranjo de tamanho fixo) e funcionasse da seguinte forma: \pause

<div class="columns">
<div class="column" width="40%">
\scriptsize

```python
>>> # Cria um arranjo com 5 zeros
>>> x = array(5)
>>> x
array([0, 0, 0, 0, 0])
>>> x[0] = 10
>>> x[4] = 2
>>> x
array([10, 0, 0, 0, 2])
>>> len(x)
5
```

\pause

</div>
<div class="column" width="58%">

\scriptsize

```
>>> x.append(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    x.append(5)
    ^^^^^^^^
AttributeError: 'array' object has no attribute 'append'
>>> x.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    x.pop()
    ^^^^^
AttributeError: 'array' object has no attribute 'pop'
>>>
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```{.python .number-lines}
def primos(lim: int) -> list[int]:
    primos = []
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```
</div>
<div class="column" width="50%">

Quais operações de lista (arranjo dinâmico) são utilizadas na função `primos`? \pause

- Criação (2 - literal) \pause
- Quantidade de elementos (7 - função) \pause
- Acesso a uma posição (8 - indexação) \pause
- Acréscimo (13 - método) \pause

Essas operações usam formas diferentes, mas a ideia de operação é a mesma, calcular valores e/ou produzir efeitos colaterais a partir das entradas.

</div>
</div>


## Operações de arranjo dinâmico

Vamos reescrever o código da função `primo` considerando que o tipo `list` e suas operações não existam. \pause

Vamos considerar que queremos criar um novo tipo, chamado `ArranjoD` (arranjo dinâmico de inteiros), que tenha as mesmas quatro operações que identificamos, mas que use a forma de chamada de função.


## Operações de arranjo dinâmico

\scriptsize

```python
def primos(lim: int) -> list[int]:
    primos = []
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = []
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

\pause

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < arranjod_len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

\pause

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < arranjod_len(primos):
            if n % arranjod_get(primos, i) == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

\pause

```python
def arranjod_get(a: ArranjoD, i: int) -> int:
    '''Devolve o elemento da posição *i* de *a*'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < arranjod_len(primos):
            if n % arranjod_get(primos, i) == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            arranjod_acresceta(primos, n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

```python
def arranjod_get(a: ArranjoD, i: int) -> int:
    '''Devolve o elemento da posição *i* de *a*'''
```

\pause

```python
def arranjod_acrescenta(a: ArranjoD, item: int):
    '''Acrescenta *item* no final *a*'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    '''
    Encontra todos os números primos
    menores que *lim*.

    Exemplos:
    >>> primos(2)
    []
    >>> primos(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    '''
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

```python
def arranjod_get(a: ArranjoD, i: int) -> int:
    '''Devolve o elemento da posição *i* de *a*'''
```

```python
def arranjod_acrescenta(a: ArranjoD, item: int):
    '''Acrescenta *item* no final *a*'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    '''
    Encontra todos os números primos
    menores que *lim*.

    Exemplos:
    >>> a = primos(12)
    >>> arranjod_get(a, 0)
    2
    >>> arranjod_get(a, 1)
    3
    >>> arranjod_get(a, 2)
    5
    >>> arranjod_get(a, 3)
    7
    >>> arranjod_get(a, 4)
    11
    '''
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

```python
def arranjod_get(a: ArranjoD, i: int) -> int:
    '''Devolve o elemento da posição *i* de *a*'''
```

```python
def arranjod_acrescenta(a: ArranjoD, item: int):
    '''Acrescenta *item* no final *a*'''
```

</div>
</div>


## Atividade

Forme uma dupla e implemente a definição e operações do tipo `ArranjoD` e confira se a implementação funciona corretamente na função `primos`. \pause

Faça o download dos arquivos `array.pyc`, `arranjod.py` e `primos_arranjod.py` da página da disciplina.

-->
