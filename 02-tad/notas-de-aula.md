---
# vim: set spell spelllang=pt_br:
title: Tipos abstratos de dados
linkcolor: Black
urlcolor: Blue
# TODO: vantagens e desvantagens de tipos abstratos de dados e concretos
---

## Introdução

Você acaba de chegar em uma empresa e a sua primeira atividade é concluir um código que havia sido iniciado pelo Roberto, que foi transferido para outra equipe. \pause

Roberto é um bom desenvolvedor e costuma fazer a especificação antes de fazer a implementação, então o seu trabalho é escrever a implementação e fazer a verificação. \pause

Note que a empresa usa uma convenção particular para nomear as funções.


## Especificação Robô

\scriptsize

```python
@dataclass
class Robo:
    '''Um robo com um nome que está em uma posição da linha do jogo, que deve
    ser um valor entre 1 e 10.'''

def robo_cria(nome: str) -> Robo:
    '''Cria um novo robo com o *nome* e que está na posição 1.'''

def robo_posicao(r: Robo) -> int:
    '''Devolve a posição atual do robo *r*.'''

def robo_info(r: Robo) -> str:
    '''Devolve um texto com o nome do robo *r* seguido da sua posição entre parêntes.'''

def robo_move(r: Robo, n: int):
    '''
    Altera a posição de *r* avançando *n* posições (até no máximo a posição 10)
    se *n* for positivo, ou recuando -*n* posições (até no mínimo a posição 1)
    se *n* for negativo. O robo *r* permanece na mesma posição se *n* for 0.
    '''
```


## Especificação Robô

<div class="columns">
<div class="column" width="50%">
\scriptsize

```python
def robo_cria(nome: str) -> Robo:
    '''Cria um novo robo com o *nome* e que
    está na posição 1.

    Exemplos
    >>> r = robo_cria('r2d2')
    >>> robo_info(r)
    'r2d2 (1)'
    '''

def robo_posicao(r: Robo) -> int:
    '''
    Devolve a posição atual do robo *r*.

    Exemplos
    >>> r = robo_cria('rob')
    >>> robo_move(r, 2)
    >>> robo_posicao(r)
    3
    '''
```
</div>
<div class="column" width="50%">
\scriptsize

```python
def robo_info(r: Robo) -> str:
    '''Devolve um texto com o nome do robo *r*
    seguido da sua posição entre parêntes.

    Exemplos
    >>> r = robo_cria('rob')
    >>> robo_move(r, 2)
    >>> robo_info(r)
    'rob (3)'
    '''
```
</div>
</div>


## Especificação Robô

\scriptsize

```python
def robo_move(r: Robo, n: int):
    '''
    Altera a posição de *r* avançando *n* posições (até no máximo a posição 10)
    se *n* for positivo, ou recuando -*n* posições (até no mínimo a posição 1) se *n* for negativo...
    >>> r = robo_cria('rob')
    >>> # Avança
    >>> robo_move(r, 5)
    >>> robo_posicao(r)
    6
    >>> robo_move(r, 6)
    >>> robo_posicao(r)
    10
    >>> # Recua
    >>> robo_move(r, -3)
    >>> robo_posicao(r)
    7
    >>> robo_move(r, -8)
    >>> robo_posicao(r)
    1
    '''
```


## Especificação Robô

O que a especificação feita pelo Roberto tem de diferente do que estamos acostumados? \pause

- Estamos acostumados a fazer a **especificação de uma função** que resolve um problema específico. \pause

- A especificação feita pelo Roberto envolve um tipo e uma coleção de funções relacionadas com esse tipo.


## Atividade

Forme uma dupla e implemente a definição e operações do tipo `Robo` e confira se a implementação funciona corretamente. \pause

Inicie com o arquivo `robo.py` disponível na página da disciplina.


## Implementação

\scriptsize

```python
@dataclass
class Robo:
    nome: str
    posicao: int

def robo_cria(nome: str) -> Robo:
    return Robo(nome, 1)

def robo_posicao(r: Robo) -> int:
    return r.posicao

def robo_info(r: Robo) -> str:
    return r.nome + ' (' + str(r.posicao) + ')'

def robo_move(r: Robo, n: int):
    r.posicao = max(1, min(10, r.posicao + n))
```


## Uso

<div class="columns">
<div class="column" width="50%">
\scriptsize

```python
>>> r = robo_cria('rob')
>>> # Avança
>>> robo_move(r, 5)
>>> robo_posicao(r)
6
>>> # Recua
>>> robo_move(r, -3)
>>> robo_posicao(r)
3
>>> # Info
>>> robo_info(r)
'rob (6)'
```

</div>
<div class="column" width="50%">
\pause

O que podemos observar de "diferente" na forma de uso da classe `Robo` em relação ao que estamos acostumados? \pause

- Estamos acostumados a criar valores de classes diretamente e também a ler e modificar os valores dos campos diretamente. \pause

- Nesse exemplo criamos valores da classe com a função `cria_robo` e usamos funções para ler e modificar os campos.
</div>
</div>


## Tipos concretos e abstratos de dados

Um tipo de dado (classe) em que a representação interna é conhecida e pode ser manipulada diretamente é chamado de **tipo concreto de dado**. \pause

Um tipo de dado em que a representação interna não é conhecida e que é manipulado apenas através de funções é chamada do **tipo abstrato de dado**. \pause

A ocultação da representação interna é chamada de encapsulamento.


## Tipo abstrator de dados

De maneira mais formal, um **tipo abstrato de de dado** (TAD) é um modelo teórico de tipo de dado, definido pela comportamento do ponto de vista do usuário do tipo, incluindo:

- Possíveis valores

- Possíveis operações

- Comportamento das operações

\pause

A especificação criada pelo Roberto define um TAD para um Robô!


## Classes em Python

A forma de criar novos tipos em Python é usando a construção `class`{.python}. \pause

Até agora usamos classes como um forma de definir dados compostos, que usávamos como tipos concretos de dados, isto é, manipulando diretamente os campos (representação interna) da classe. \pause

Na especificação feita pelo Roberto usamos uma classe para implementar um TAD. \pause Observe a diferença entre quem implementa o TAD e quem usa o TAD: \pause

- Quem implementa o tipo tem acesso e manipula diretamente os campos da classe \pause

- Quem usa o tipo não tem acesso direto aos campos e utiliza funções para fazer operações com os dados do tipo


## Métodos

Apesar de podemos usar funções "livres" para implementar TADs, o comum em Python é usar métodos. \pause

Um método é uma função que está associada com uma classe particular. \pause

Para criar um método em um classe, basta definir uma função "dentro" da classe!


## Definição de Métodos

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class Robo:
    nome: str
    posicao: int

def robo_cria(nome: str) -> Robo: ...

def robo_posicao(r: Robo) -> int: ...

def robo_info(r: Robo) -> str: ...

def robo_move(r: Robo, n: int):
    '''
    >>> r = robo_cria('rob')
    >>> robo_move(r, 5)
    >>> robo_posicao(r)
    6
    '''
```

\pause

</div>
<div class="column" width="50%">
\scriptsize

```python
@dataclass
class Robo:
    nome: str
    posicao: int

    def robo_cria(nome: str) -> Robo: ...

    def robo_posicao(r: Robo) -> int: ...

    def robo_info(r: Robo) -> str: ...

    def robo_move(r: Robo, n: int):
        '''
        >>> r = Robo.robo_cria('rob')
        >>> r.robo_move(5)
        >>> r.robo_posicao()
        6
        '''
```
</div>
</div>


## Definição de Métodos

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class Robo:
    nome: str
    posicao: int

def robo_cria(nome: str) -> Robo: ...

def robo_posicao(r: Robo) -> int: ...

def robo_info(r: Robo) -> str: ...

def robo_move(r: Robo, n: int):
    '''
    >>> r = robo_cria('rob')
    >>> robo_move(r, 5)
    >>> robo_posicao(r)
    6
    '''
```

</div>
<div class="column" width="50%">
\scriptsize

```python
@dataclass
class Robo:
    nome: str
    posicao: int

    def cria(nome: str) -> Robo: ...

    def posicao(r: Robo) -> int: ...

    def info(r: Robo) -> str: ...

    def move(r: Robo, n: int):
        '''
        >>> r = Robo.cria('rob')
        >>> r.move(5)
        >>> r.posicao()
        6
        '''
```
</div>
</div>


## Definição de Métodos

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class Robo:
    nome: str
    posicao: int

def robo_cria(nome: str) -> Robo: ...

def robo_posicao(r: Robo) -> int: ...

def robo_info(r: Robo) -> str: ...

def robo_move(r: Robo, n: int):
    '''
    >>> r = robo_cria('rob')
    >>> robo_move(r, 5)
    >>> robo_posicao(r)
    6
    '''
```

</div>
<div class="column" width="50%">
\scriptsize

```python

class Robo:
    nome: str
    posicao: int

    def __init__(r: Robo, nome: str): ...

    def posicao(r: Robo) -> int: ...

    def info(r: Robo) -> str: ...

    def move(r: Robo, n: int):
        '''
        >>> r = Robo('rob')
        >>> r.move(5)
        >>> r.posicao()
        6
        '''
```
</div>
</div>


## Definição de Métodos

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class Robo:
    nome: str
    posicao: int

def robo_cria(nome: str) -> Robo: ...

def robo_posicao(r: Robo) -> int: ...

def robo_info(r: Robo) -> str: ...

def robo_move(r: Robo, n: int):
    '''
    >>> r = robo_cria('rob')
    >>> robo_move(r, 5)
    >>> robo_posicao(r)
    6
    '''
```

</div>
<div class="column" width="50%">
\scriptsize

```python

class Robo:
    nome: str
    posicao: int

    def __init__(self, nome: str): ...

    def posicao(self) -> int: ...

    def info(self) -> str: ...

    def move(self, n: int):
        '''
        >>> r = Robo('rob')
        >>> r.move(5)
        >>> r.posicao()
        6
        '''
```
</div>
</div>


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
