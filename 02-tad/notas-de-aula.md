---
# vim: set spell spelllang=pt_br:
title: Tipos abstratos de dados
linkcolor: Black
urlcolor: Blue
---

## Introdução

Projete uma função que encontre todos os números primos menores que um determinado valor.

## Introdução

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
def primos(n: int) -> list[int]:
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


## Introdução

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

```python
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
def primos(n: int) -> list[int]:
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

Vamos considerar que queremos criar um novo tipo, chamado `ArranjoD` (um arranjo dinâmico de inteiros), que tenha as mesmas quatro operações que identificamos, mas que use a forma de chamada de função.


## Operações de arranjo dinâmico

\scriptsize

```python
def primos(n: int) -> list[int]:
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
def primos(n: int) -> ArranjoD:
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
def primos(n: int) -> ArranjoD:
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
    ...
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(n: int) -> ArranjoD:
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
    ...
```

\pause

```python
def arranjod_len(a: ArranjoD) -> int:
    ...
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(n: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < arranjod_len(primos):
            if n % arranjod_pos(primos, i) == 0:
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
    ...
```

```python
def arranjod_len(a: ArranjoD) -> int:
    ...
```

\pause

```python
def arranjod_pos(a: ArranjoD, i: int) -> int:
    ...
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(n: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < arranjod_len(primos):
            if n % arranjod_pos(primos, i) == 0:
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
    ...
```

```python
def arranjod_len(a: ArranjoD) -> int:
    ...
```

```python
def arranjod_pos(a: ArranjoD, i: int) -> int:
    ...
```

\pause

```python
def arranjod_acrescenta(a: ArranjoD, item: int):
    ...
```

</div>
</div>

## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(n: int) -> ArranjoD:
    '''
    Encontra todos os números primos
    menores que *lim*.

    Exemplos:
    >>> lst = primos(12)
    >>> lst[0]
    2
    >>> lst[1]
    3
    >>> lst[2]
    5
    >>> lst[3]
    7
    >>> lst[4]
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
    ...
```

```python
def arranjod_len(a: ArranjoD) -> int:
    ...
```

```python
def arranjod_pos(a: ArranjoD, i: int) -> int:
    ...
```

```python
def arranjod_acrescenta(a: ArranjoD, item: int):
    ...
```

</div>
</div>

## Atividade

Forme uma dupla e implemente a definição e operações do tipo `ArranjoD` e confira se a implementação funciona corretamente na função `primos`.
