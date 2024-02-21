---
# vim: set spell spelllang=pt_br:
title: Recursividade
linkcolor: Black
urlcolor: Blue
# TODO: adicionar exemplo em que a recursão é opcional
# TODO: adicionar referências
---

## Introdução

Uma função é **recursiva** quando ela chama a si mesmo de forma direta ou indireta. \pause

A recursividade é uma técnica muito poderosa e bastante utilizada na Computação e Matemática. \pause

De certa a forma a recursividade é um caso especial da decomposição de problemas. \pause

De forma geral podemos resolver um problema decompondo-o em subproblemas mais simples, resolvendo os subproblemas e combinado as soluções para obter a solução do problema inicial. \pause

A recursividade surge quando decompomos um problema em subproblemas do _mesmo tipo_, pois nesses casos podemos utilizar _o mesmo processo_ para resolver o problema inicial e os subproblemas. \pause Note que para que o processo funciona, devemos definir situações limites em que o problema seja resolvido diretamente, sem precisar ser decomposto, que são os casos bases.


## Formas de recursividade

Então, para que possamos aplicar a recursividade é necessário decompor um problema em subproblemas do mesmo tipo. \pause Mas como fazer a decomposição? \pause

- Para algumas problemas pode ser necessário um momento "eureka" e inventar uma forma de fazer a decomposição, o que requer experiência. \pause

- Mas para a maioria dos problemas podemos fazer uma decomposição "direta", baseada na definição com autorreferência do dado (estrutura) que representa o problema. \pause

A primeira forma gera **funções recursivas generativas**, já a segunda forma gerar **funções recursivas estruturais**. Vamos explorar agora essa segunda forma.


## Restrições

Para escrever os próximos exemplos não vamos usar

- Arranjos; e

- Laços de repetição

\pause

Como representar uma quantidade arbitrária de dados sem arranjos? \pause

- Usando encadeamento


## Definição de lista

<div class="columns">
<div class="column" width="48%">

A definição para nó que utilizamos foi:

\scriptsize

```python
@dataclass
class No:
    item: int
    prox: No | None
```

\pause

\normalsize

Para facilitar o projeto e entendimento das próximas funções vamos utilizar a seguinte definição:

\scriptsize

```python
@dataclass
class No:
    primeiro: int
    resto: Lista

Lista = No | None
```

\pause

</div>
<div class="column" width="48%">

De maneira formal, uma **Lista** é:

- Vazia (`None`{.python}); ou
- Um nó (`No`) com um elemento e o resto, que é uma **Lista**.

\pause

Para implementar funções que processam uma Lista, vamos explorar a relação entre autorreferência (na definição) e recursividade (na função):

\scriptsize

```python
def fn_para_lista(lst: Lista) -> ...:
    if lst is None:
        return ...
    else:
        return lst.primeiro ... \
               fn_para_lista(lst.resto)
```

</div>
</div>


## Soma

Projete uma função que some os elementos de uma lista.


## Soma

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def soma(lst: Lista) -> int:
    '''Soma os elementos de *lst*.

                    lst
         /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma(No(10, No(4, No(3, None)))) -> 17
             |  \_________________/
      primeiro      soma(resto)
            10          7

    Como computar soma(lst) a partir de
    lst.primeiro e soma(lst.resto)?
    '''
```

\pause

```python
    if lst is None:
        return ...
    else:
        return lst.primeiro ... soma(lst.resto)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Soma

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def soma(lst: Lista) -> int:
    '''Soma os elementos de *lst*.

                    lst
         /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma(No(10, No(4, No(3, None)))) -> 17
             |  \_________________/
      primeiro      soma(resto)
            10          7

    Como computar soma(lst) a partir de
    lst.primeiro e soma(lst.resto)?
    '''
```

```python
    if lst is None:
        return 0
    else:
        return lst.primeiro + soma(lst.resto)
```

</div>
<div class="column" width="48%">
\pause

\scriptsize

```python
def soma(lst: Lista) -> int:
    '''Soma os elementos de *lst*.

                    lst
         /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma(No(10, No(4, No(3, None)))) -> 17
            \_______/    |     |
                s    p.primeiro |
               14             p.resto

    Como inicializar s e p?
    Como atualizar s e p?
    '''
```

\pause

```python
    s = 0
    p = lst
    while p is not None:
        s += p.primeiro
        p = p.resto
    return s
```
</div>
</div>


## Número de itens

Projete uma função que determine a quantidade de itens em uma lista.


## Número de itens

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def num_itens(lst: Lista) -> int:
    '''Devolve a quantidade de itens em *lst*.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
   num_itens(No(10, No(4, No(3, None)))) -> 3
                |   \_________________/
         primeiro     num_itens(resto)
               10        2

    Como computar num_itens(lst) a partir de
    lst.primeiro e num_itens(lst.resto)?
    '''
```

\pause

```python
    if lst is None:
        return ...
    else:
        return lst.primeiro ... num_itens(lst.resto)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Número de itens

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def num_itens(lst: Lista) -> int:
    '''Devolve a quantidade de itens em *lst*.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
   num_itens(No(10, No(4, No(3, None)))) -> 3
                |   \_________________/
         primeiro     num_itens(resto)
               10        2

    Como computar num_itens(lst) a partir de
    lst.primeiro e num_itens(lst.resto)?
    '''
```

```python
    if lst is None:
        return 0
    else:
        return 1 + num_itens(lst.resto)
```

</div>
<div class="column" width="48%">

\pause

\scriptsize

```python
def num_itens(lst: Lista) -> int:
    '''Devolve a quantidade de itens em *lst*.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
   num_itens(No(10, No(4, No(3, None)))) -> 3
                \______/    |     |
                  num   p.primeiro |
                   2              p.resto

    Como inicializar num e p?
    Como atualizar num e p?
    '''
```

\pause

```python
    num = 0
    p = lst
    while p is not None:
        num += 1
        p = p.resto
    return num
```

</div>
</div>


## Todos pares

Projete uma função que verifique se todos os elementos de uma lista são pares.


## Todos pares

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(6, None)))) -> True
                |   \_________________/
         primeiro    todos_pares(resto)
               10        True

    Como computar todos_pares(lst) a partir de
    lst.primeiro e todos_pares(lst.resto)?
    '''
```

```python





```

</div>
<div class="column" width="48%">
</div>
</div>


## Todos pares

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(11, No(4, No(6, None)))) -> False
                |   \_________________/
         primeiro    todos_pares(resto)
               11        True

    Como computar todos_pares(lst) a partir de
    lst.primeiro e todos_pares(lst.resto)?
    '''
```

```python





```

</div>
<div class="column" width="48%">
</div>
</div>


## Todos pares

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(3, None)))) -> False
                |   \_________________/
         primeiro    todos_pares(resto)
               10        False

    Como computar todos_pares(lst) a partir de
    lst.primeiro e todos_pares(lst.resto)?
    '''
```

\pause

```python
    if lst is None:
        return ...
    else:
        return lst.primeiro ... \
                   todos_pares(lst.resto)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Todos pares

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(3, None)))) -> False
                |   \_________________/
         primeiro    todos_pares(resto)
               10        False

    Como computar todos_pares(lst) a partir de
    lst.primeiro e todos_pares(lst.resto)?
    '''
```

```python
    if lst is None:
        return True
    else:
        return lst.primeiro % 2 == 0 and \
                   todos_pares(lst.resto)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Todos pares

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(3, None)))) -> False
                |   \_________________/
         primeiro    todos_pares(resto)
               10        False

    Como computar todos_pares(lst) a partir de
    lst.primeiro e todos_pares(lst.resto)?
    '''
```

```python
    return lst is None or \
               lst.primeiro % 2 == 0 and \
                   todos_pares(lst.resto)


```

</div>
<div class="column" width="48%">
\pause

\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(3, None)))) -> False
                \_______/    |     |
                  pares  p.primeiro |
                  True             p.resto
    Como inicializar pares e p?
    Como atualizar pares e p?
    '''
```

\pause

```python
    pares = True
    p = lst
    while pares and p is not None:
        pares = p.primeiro % 2 == 0
        p = p.resto
    return pares
```
</div>
</div>


## Todos pares

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(3, None)))) -> False
                |   \_________________/
         primeiro    todos_pares(resto)
               10        False

    Como computar todos_pares(lst) a partir de
    lst.primeiro e todos_pares(lst.resto)?
    '''
```

```python
    return lst is None or \
               lst.primeiro % 2 == 0 and \
                   todos_pares(lst.resto)


```

</div>
<div class="column" width="48%">
\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(3, None)))) -> False
                \_______/    |     |
                  pares  p.primeiro |
                  True             p.resto
    Como inicializar pares e p?
    Como atualizar pares e p?
    '''
```


```python
    p = lst
    while p is not None:
        if p.primeiro % 2 != 0:
             return False
        p = p.resto
    return True
```
</div>
</div>


## Todos pares

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(3, None)))) -> False
                |   \_________________/
         primeiro    todos_pares(resto)
               10        False

    Como computar todos_pares(lst) a partir de
    lst.primeiro e todos_pares(lst.resto)?
    '''
```

```python
    return lst is None or \
               lst.primeiro % 2 == 0 and \
                   todos_pares(lst.resto)


```

</div>
<div class="column" width="48%">
\scriptsize

```python
def todos_pares(lst: Lista) -> bool:
    '''Devolve True se todos os elementos
    de *lst* são pares, False caso contrário.

                        lst
             /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
 todos_pares(No(10, No(4, No(3, None)))) -> False
                \_______/    |     |
                  pares  p.primeiro |
                  True             p.resto
    Como inicializar pares e p?
    Como atualizar pares e p?
    '''
```


```python
    while lst is not None and lst.primeiro % 2 == 0:
        lst = lst.resto
    return lst is None




```
</div>
</div>


## Contém

Projete uma função que verifique se um item está em uma lista.


## Contém

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def contem(lst: Lista, v: int) -> bool:
    '''Devolve True se *v* está em *lst*,
    False caso contrário.

                      lst              v
           /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\  |
    contem(No(10, No(4, No(3, None))), 4) -> True
                | \_________________/
         primeiro   contem(resto, v)
               10        True

    Como computar contem(lst, v) a partir de
    lst.primeiro e contem(lst.resto, v)?
    '''
```

\pause

```python
    if lst is None:
        return ... v
    else:
        return v ... lst.primeiro ... \
                   contem(lst.resto, v)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Contém

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def contem(lst: Lista, v: int) -> bool:
    '''Devolve True se *v* está em *lst*,
    False caso contrário.

                      lst              v
           /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\  |
    contem(No(10, No(4, No(3, None))), 4) -> True
                | \_________________/
         primeiro   contem(resto, v)
               10        True

    Como computar contem(lst, v) a partir de
    lst.primeiro e contem(lst.resto, v)?
    '''
```

```python
    if lst is None:
        return False
    else:
        return v == lst.primeiro or \
                   contem(lst.resto, v)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Contém

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def contem(lst: Lista, v: int) -> bool:
    '''Devolve True se *v* está em *lst*,
    False caso contrário.

                      lst              v
           /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\  |
    contem(No(10, No(4, No(3, None))), 4) -> True
                | \_________________/
         primeiro   contem(resto, v)
               10        True

    Como computar contem(lst, v) a partir de
    lst.primeiro e contem(lst.resto, v)?
    '''
```

```python
    return lst is not None and \
               (v == lst.primeiro or
                    contem(lst.resto, v))


```

</div>
<div class="column" width="48%">
\pause

\scriptsize

```python
def contem(lst: Lista, v: int) -> bool:
    '''Devolve True se *v* está em *lst*,
    False caso contrário.

                      lst              v
           /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\  |
    contem(No(10, No(4, No(3, None))), 4) -> True
              \_______/    |     |
                achou  p.primeiro |
                False            p.resto
    Como inicializar achou e p?
    Como atualizar achou e p?
    '''
```

\pause

```python
    achou = False
    p = lst
    while not achou and p is not None:
        achou = v == p.primeiro
        p = p.resto
    return False
```
</div>
</div>


## Contém

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def contem(lst: Lista, v: int) -> bool:
    '''Devolve True se *v* está em *lst*,
    False caso contrário.

                      lst              v
           /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\  |
    contem(No(10, No(4, No(3, None))), 4) -> True
                | \_________________/
         primeiro   contem(resto, v)
               10        True

    Como computar contem(lst, v) a partir de
    lst.primeiro e contem(lst.resto, v)?
    '''
```

```python
    return lst is not None and \
               (v == lst.primeiro or
                    contem(lst.resto, v))


```

</div>
<div class="column" width="48%">
\scriptsize

```python
def contem(lst: Lista, v: int) -> bool:
    '''Devolve True se *v* está em *lst*,
    False caso contrário.

                      lst              v
           /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\  |
    contem(No(10, No(4, No(3, None))), 4) -> True
              \_______/    |     |
                achou  p.primeiro |
                False            p.resto
    Como inicializar achou e p?
    Como atualizar achou e p?
    '''
```

```python
    while lst is not None and v != lst.primeiro:
        lst = lst.resto
    return lst is not None




```
</div>
</div>


## Soma 1

Projete uma função que modifique uma lista somando 1 em cada um dos seus elementos.


## Soma 1

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def soma1(lst: Lista):
    '''Modifica *lst* somando 1 a cada elemento
    de *lst*.

                     lst
          /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma1(No(10, No(4, No(3, None))))
             |   \_________________/
      primeiro       soma1(resto)
            10   No(5, No(4, None))

    Como implementar soma1(lst) usando
    lst.primeiro e soma1(lst.resto)?
    '''
```

\pause

```python
    if lst is None:
        ...
    else:
        lst.primeiro ... \
            soma1(lst.resto)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Soma 1

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def soma1(lst: Lista):
    '''Modifica *lst* somando 1 a cada elemento
    de *lst*.

                     lst
          /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma1(No(10, No(4, No(3, None))))
             |   \_________________/
      primeiro       soma1(resto)
            10   No(5, No(4, None))

    Como implementar soma1(lst) usando
    lst.primeiro e soma1(lst.resto)?
    '''
```

```python
    if lst is None:
        return
    else:
        lst.primeiro += 1
        soma1(lst.resto)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Soma 1

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def soma1(lst: Lista):
    '''Modifica *lst* somando 1 a cada elemento
    de *lst*.

                     lst
          /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma1(No(10, No(4, No(3, None))))
             |   \_________________/
      primeiro       soma1(resto)
            10   No(5, No(4, None))

    Como implementar soma1(lst) usando
    lst.primeiro e soma1(lst.resto)?
    '''
```

```python
    if lst is not None:
        lst.primeiro += 1
        soma1(lst.resto)


```

</div>
<div class="column" width="48%">
\pause
\scriptsize

```python
def soma1(lst: Lista):
    '''Modifica *lst* somando 1 a cada elemento
    de *lst*.

                     lst
          /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma1(No(10, No(4, No(3, None))))
             \_______/    |     |
             11     5 p.primeiro |
                                p.resto

    Como modificar p.primeiro e atualizar p?
    '''
```

\pause

```python
    p = lst
    while p is not None:
        p.primeiro += 1
        p = p.resto
```
</div>
</div>


## Soma 1

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def soma1(lst: Lista):
    '''Modifica *lst* somando 1 a cada elemento
    de *lst*.

                     lst
          /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma1(No(10, No(4, No(3, None))))
             |   \_________________/
      primeiro       soma1(resto)
            10   No(5, No(4, None))

    Como implementar soma1(lst) usando
    lst.primeiro e soma1(lst.resto)?
    '''
```

```python
    if lst is not None:
        lst.primeiro += 1
        soma1(lst.resto)


```

</div>
<div class="column" width="48%">
\scriptsize

```python
def soma1(lst: Lista):
    '''Modifica *lst* somando 1 a cada elemento
    de *lst*.

                     lst
          /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
    soma1(No(10, No(4, No(3, None))))
             \_______/    |     |
             11     5 p.primeiro |
                                p.resto

    Como modificar p.primeiro e atualizar p?
    '''
```

```python
    while lst is not None:
        lst.primeiro += 1
        lst = lst.resto

```
</div>
</div>


## Duplica

Projete uma função que modifique uma lista criando uma cópia de cada item da lista (que deve ficar após o item que foi copiado).


## Duplica

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def duplica(lst: Lista):
    '''
    Modifica *lst* criando uma cópia de cada nó
    que é colocado após o nó copiado.

    Como implementar duplica(lst) usando
    lst.primeiro e duplica(lst.resto)?
    '''
```

\pause

```python
    if lst is None:
        return ...
    else:
        lst.primeiro
        duplica(lst.resto)
```

</div>
<div class="column" width="48%">
</div>
</div>


## Duplica

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def duplica(lst: Lista):
    '''
    Modifica *lst* criando uma cópia de cada nó
    que é colocado após o nó copiado.

    Como implementar duplica(lst) usando
    lst.primeiro e duplica(lst.resto)?
    '''
```

```python
    if lst is None:
        return
    else:
        duplica(lst.resto)
        lst.resto = No(lst.primeiro, lst.resto)

```

</div>
<div class="column" width="48%">
</div>
</div>


## Duplica

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def duplica(lst: Lista):
    '''
    Modifica *lst* criando uma cópia de cada nó
    que é colocado após o nó copiado.

    Como implementar duplica(lst) usando
    lst.primeiro e duplica(lst.resto)?
    '''
```

```python
    if lst is not None:
        duplica(lst.resto)
        lst.resto = No(lst.primeiro, lst.resto)



```

</div>
<div class="column" width="48%">
\pause
\scriptsize

```python
def duplica(lst: Lista):
    '''
    Modifica *lst* criando uma cópia de cada nó
    que é colocado após o nó copiado.

    Como duplicar um nó p e atualizar p?
    '''
```

\pause

```python
    p = lst
    while p is not None:
        p.resto = No(p.primeiro, p.resto)
        p = p.resto.resto
```
</div>
</div>


## Considerações sobre recursividade com lista

Projetar uma função recursiva pode ser um desafio se for preciso "inventar" uma forma de decompor o problema. \pause

No entanto, se fizermos a decomposição estrutural, isto é, decompor o problema conforme o dado que descreve o problema, então o projeto de funções recursivas se torna um processo mais sistemático. \pause

Podemos aplicar a o processo de projeto de funções recursivas baseada na decomposição estrutural em dados que não sejam listas? \pause Sim, podemos aplicar em qualquer dado que tenha autorreferência!


## Recursão com número natural

<div class="columns">
<div class="column" width="48%">
Como definir um número natural? \pause Usando autorreferência. \pause

Um **número natural** é:

- 0; ou
- $n + 1$, onde $n$ é um **número natural**.

\pause

A partir dessa definição podemos criar um modelo de função para processar número naturais (que precisam ser decompostos):

\scriptsize

```python
def fn_para_n(n: int) -> ...:
    if n == 0:
        return ...
    else:
        return n ... fn_para_n(n - 1)
```

</div>
<div class="column" width="48%">
\pause

Projete uma função que some todos os número naturais até um dado $n$.

\scriptsize

```python
def soma(n: int) -> int:
    '''
    Devolve a soma de todos os números
    naturais até *n*. Requer que n >=0.
    Exemplos
    >>> soma(0)
    0
    >>> soma(4)
    10
    '''
```

\pause

```python
    if n == 0:
        return 0
    else:
        return n + soma(n - 1)
```
</div>
</div>


## Recursão com número natural

<div class="columns">
<div class="column" width="48%">
Como definir um número natural? Usando autorreferência.

Um **número natural** é:

- 0; ou
- $n + 1$, onde $n$ é um **número natural**.

A partir dessa definição podemos criar um modelo de função para processar número naturais (que precisam ser decompostos):

\scriptsize

```python
def fn_para_n(n: int) -> ...:
    if n == 0:
        return ...
    else:
        return n ... fn_para_n(n - 1)
```

</div>
<div class="column" width="48%">

Projete uma função que receba como parâmetro um número natural $n$ e crie um arranjo $[1, 2, \dots, n]$. \pause

\scriptsize

```python
def lista_n(n: int) -> list[int]:
    '''
    Devolve a lista [1, 2, ..., *n*].
    Requer que n >= 0.

    >>> lista_n(0)
    []
    >>> lista_n(3)
    [1, 2, 3]
    '''
```

\pause

```python
    if n == 0:
        return []
    else:
        return lista_n(n - 1) + [n]
```
</div>
</div>


## Recursão com número natural

<div class="columns">
<div class="column" width="48%">
Como definir um número natural? Usando autorreferência.

Um **número natural** é:

- 0; ou
- $n + 1$, onde $n$ é um **número natural**.

A partir dessa definição podemos criar um modelo de função para processar número naturais (que precisam ser decompostos):

\scriptsize

```python
def fn_para_n(n: int) -> ...:
    if n == 0:
        return ...
    else:
        return n ... fn_para_n(n - 1)
```

</div>
<div class="column" width="48%">

Projete uma função que receba como parâmetro um número natural $n$ e crie um arranjo $[1, 2, \dots, n]$.

\scriptsize

```python
def lista_n(n: int) -> list[int]:
    '''
    Devolve a lista [1, 2, ..., *n*].
    Requer que n >= 0.
    >>> lista_n(0)
    []
    >>> lista_n(3)
    [1, 2, 3]
    '''
```

```python
    if n == 0:
        return []
    else:
        lst = lista_n(n - 1)
        lst.append(n)
        return lst
```
</div>
</div>


## Recursão com arranjos

<div class="columns">
<div class="column" width="48%">

Podemos usar recursão estrutural com arranjos? \pause Sim e não! \pause

Tentar definir um arranjo usando autorreferência pode ser um pouco confuso... \pause Mas podemos pensar que um arranjo é vazio, ou tem um primeiro elemento e o restante dos elementos. \pause

Dessa forma, podemos definir o seguinte modelo:

\scriptsize

```python
def fn_para_array(lst: list[int]) -> ...:
    if lst == []:
        return ...
    else:
        return lst[0] ... fn_para_array(lst[1:])
```

</div>
<div class="column" width="48%">

\pause

Projete uma função que some todos os elementos de um arranjo.

\pause

\scriptsize

```python
def soma(lst: list[int]) -> int:
    '''
    Soma todos os elementos de *lst*.
    '''
```

\pause

```python
    if lst == []:
        return 0
    else:
        return lst[0] + soma(lst[1:])
```

\pause

\normalsize

Qual o problema com essa estratégia? \pause

O _slice_ cria um novo arranjo a cada chamada, o que é custoso. \pause

Podemos fazer melhor? \pause Sim!
</div>
</div>


## Recursão com arranjos

<div class="columns">
<div class="column" width="48%">

\small

Ao invés de "diminuir" o arranjo do início, vamos diminuir do fim usando um "tamanho virtual". \pause

Junto com o arranjo passamos também um valor $n$, que representa quantos elementos a partir do início do arranjo devem ser considerados. \pause Na chamada recursiva, passamos o arranjo inalterado e o valor $n - 1$, que representa a diminuição do arranjo. \pause O modelo fica assim:

\scriptsize

```python
def fn_para_array(lst: list[int], n: int) -> ...:
    if n == 0:
        return ...
    else:
        return lst[n - 1] ... \
                   fn_para_array(lst, n - 1)
```

</div>
<div class="column" width="48%">

\pause

\small

Projete uma função que some todos os elementos de um arranjo.

\pause

\scriptsize

```python
def soma(lst: list[int], n: int) -> int:
    '''
    Soma os primeiros *n* elementos de *lst*.
    Requer que 0 <= n <= len(lst)
    >>> soma([5, 1, 4, 2, 3], 3)
    10
    '''
```

\pause

```python
    if n == 0:
        return 0
    else:
        return lst[n - 1] + soma(lst, n - 1)
```

\pause
\small

Não parece melhor que um laço de repetição... \pause Além disso, a função precisa de um argumento extra!

</div>
</div>


## Recursão com arranjos

Esse exemplo de função recursiva com arranjo é ilustrativa e de fato não é muito útil. \pause

Na prática, recursividade em arranjo é feita em subarranjos quaisquer, e não em um subarranjo sem o último elemento. \pause

Nesse caso, a função receba como parâmetro além do arranjo um índice de início e outro de fim, que define o subarranjo que vai ser processado. \pause

Note que dessa forma não temos mais recursão estrutural e sim recursão generativa. \pause É preciso determinar uma forma específica para o subarranjo.


## Palíndromo

Projete uma função recursiva que determine se um arranjo de números é palíndromo, isto é, tem os mesmos elementos quando lido da direita para e esquerda e da esquerda para a direita. \pause

Para esse problema o principal desafio é definir como decompor o problema em subproblema(s) da mesma natureza. \pause

Por exemplo, para o arranjo `[4, 1, 3, 3, 1, 4]`{.python}, que subproblema (subarranjo) podemos resolver de forma recursiva que nos ajude a resolver o problema para o arranjo todo? \pause

Se determinamos se `[1, 3, 3, 1]`{.python} (arranjo original sem o primeiro e último) é palíndromo, então podemos utilizar esse fato para determinar se o arranjo original é palíndromo verificando se o primeiro e último elementos são iguais. \pause

Em que situação não precisamos decompor o problema original? \pause Se o subarranjo é vazio ou tem apenas um elemento.


## Palíndromo

<div class="columns">
<div class="column" width="65%">
\scriptsize

```python
def palindromo(lst: list[int], ini: int, fim: int) -> bool:
    '''
    Devolve True se o subarranjo *lst[ini:fim+1]* é palíndromo,
    isto é, o subarranjo tem os mesmos elementos quando visto
    da direita para esquerda e da esquerda para a direita.
    Requer que 0 <= ini < len(lst) e 0 <= fim < len(lst)
    Exemplos
    >>> palindromo([1, 1, 3, 4, 3, 1], 1, 5)
    True
    >>> palindromo([1, 1, 3, 4, 3, 1], 0, 5)
    False
    '''
    assert 0 <= ini < len(lst)
    assert 0 <= fim < len(lst)
    if fim <= ini:
        return True
    else:
        return lst[ini] == lst[fim] and palindromo(lst, ini + 1, fim - 1)
```
</div>
<div class="column" width="33%">
</div>
</div>


## Palíndromo

<div class="columns">
<div class="column" width="65%">
\scriptsize

```python
def palindromo(lst: list[int], ini: int, fim: int) -> bool:
    '''
    Devolve True se o subarranjo *lst[ini:fim+1]* é palíndromo,
    isto é, o subarranjo tem os mesmos elementos quando visto
    da direita para esquerda e da esquerda para a direita.
    Requer que 0 <= ini < len(lst) e 0 <= fim < len(lst)
    Exemplos
    >>> palindromo([1, 1, 3, 4, 3, 1], 1, 5)
    True
    >>> palindromo([1, 1, 3, 4, 3, 1], 0, 5)
    False
    '''
    assert 0 <= ini < len(lst)
    assert 0 <= fim < len(lst)
    return fim <= ini or \
               lst[ini] == lst[fim] and \
                   palindromo(lst, ini + 1, fim - 1)
```
</div>
<div class="column" width="33%">
\pause
Quais os problemas dessa implementação? \pause

- Requer argumentos extras; \pause
- Verifica a validade dos parâmetros em todas as chamadas. \pause

Como podemos melhorar? \pause Vamos criar um função auxiliar interna que recebe o inicio e o fim e deixar a função principal recebendo apenas um argumento.
</div>
</div>


## Palíndromo

<div class="columns">
<div class="column" width="65%">
\scriptsize

```python
def palindromo(lst: list[int]) -> bool:
    '''
    Devolve True se o lst é palíndromo, isto é, tem os mesmos elementos quando
    visto da direita para esquerda e da esquerda para a direita.
    Exemplos
    >>> palindromo([1, 1])
    True
    >>> palindromo([2, 1, 0, 1, 2])
    True
    >>> palindromo([2, 1, 0, 1, 1])
    False
    '''
    def _palindromo(lst: list[int], ini: int, fim: int) -> bool:
        return fim <= ini or \
                   lst[ini] == lst[fim] and \
                       _palindromo(lst, ini + 1, fim - 1)

    return _palindromo(lst, 0, len(lst) - 1)
```
</div>
<div class="column" width="33%">
</div>
</div>


## Exemplos de execução passo a passo

Exemplos de execução passo a passo no [PythonTutor](https://pythontutor.com):

- [Soma](https://pythontutor.com/render.html#code=def%20soma%28n%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20if%20n%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20n%20%2B%20soma%28n%20-%201%29%0A%0Aprint%28soma%284%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) dos números naturais menores que um $n$.

- [Soma](https://pythontutor.com/render.html#code=class%20No%3A%0A%20%20%20%20primeiro%3A%20int%0A%20%20%20%20resto%3A%20%22Lista%22%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self,%20primeiro%3A%20int,%20resto%3A%20%22Lista%22%29%3A%0A%20%20%20%20%20%20%20%20self.primeiro%20%3D%20primeiro%0A%20%20%20%20%20%20%20%20self.resto%20%3D%20resto%0A%0A%0ALista%20%3D%20No%20%7C%20None%0A%0A%0Adef%20soma%28lst%3A%20Lista%29%20-%3E%20int%3A%0A%20%20%20%20if%20lst%20is%20None%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20lst.primeiro%20%2B%20soma%28lst.resto%29%0A%0Alst%20%3D%20No%2810,%20No%282,%20No%283,%20No%285,%20None%29%29%29%29%0A%0Aprint%28soma%28lst%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) dos elementos de uma lista encadeada.

- [Soma](https://pythontutor.com/render.html#code=def%20soma_slice%28lst%3A%20list%5Bint%5D%29%20-%3E%20int%3A%0A%20%20%20%20if%20lst%20%3D%3D%20%5B%5D%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20lst%5B0%5D%20%2B%20soma_slice%28lst%5B1%3A%5D%29%0A%0Adef%20soma%28lst%3A%20list%5Bint%5D,%20n%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20if%20n%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20lst%5Bn%20-%201%5D%20%2B%20soma%28lst,%20n%20-%201%29%0A%20%20%20%20%20%20%20%20%0A%0Aprint%28soma_slice%28%5B4,%201,%205,%202%5D%29%29%0A%0Aprint%28soma%28%5B4,%201,%205,%202%5D,%204%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) dos elementos de um arranjo.

- [Palíndromo](https://pythontutor.com/render.html#code=def%20palindromo%28lst%3A%20list%5Bint%5D%29%20-%3E%20bool%3A%0A%20%20%20%20def%20_palindromo%28lst%3A%20list%5Bint%5D,%20ini%3A%20int,%20fim%3A%20int%29%20-%3E%20bool%3A%0A%20%20%20%20%20%20%20%20return%20fim%20%3C%3D%20ini%20or%20lst%5Bini%5D%20%3D%3D%20lst%5Bfim%5D%20and%20_palindromo%28lst,%20ini%20%2B%201,%20fim%20-%201%29%0A%20%20%20%20return%20_palindromo%28lst,%200,%20len%28lst%29%20-%201%29%0A%0Aprint%28palindromo%28%5B4,%201,%203,%200,%203,%201,%204%5D%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) de arranjo.

