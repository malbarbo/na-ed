---
# vim: set spell spelllang=pt_br:
title: Árvores binárias de busca
linkcolor: Black
urlcolor: Blue
# TODO: falar sobre testes, especificamente, de uma forma de testar se a árvore tem a estrutura correta.
# TODO: falar de percursos?
# TODO: adicionar mais exemplos de funções
# TODO: mudar raiz de t para r?
# TODO: no ínicio tem a frase "Se conseguirmos, ... talvez", temos que retomar essa frase no final
---

## Encadeamento e busca binária?

Podemos fazer uma busca binária em um encadeamento linear de forma eficiente? \pause Não, pois não temos acesso em tempo constante ao elemento "do meio". \pause

Podemos fazer uma busca binária em _algum tipo de encadeamento_ de forma eficiente? \pause

Porque iríamos querer fazer isso? \pause Em um arranjo é possível fazer busca binária eficiente, mas a inserção e remoção tem complexidade de tempo $O(n)$. \pause

Se _conseguirmos_ fazer uma busca binária eficiente em um encadeamento, _talvez_ possamos fazer inserção e remoção de forma eficiente também! \pause

Vamos analisar uma sequência ordenada de elementos e tentar criar um encadeamento que permita a realização de uma busca binária.


## Encadeamento e busca binária? {.b}

<div class="columns">
<div class="column" width="15%">
</div>
<div class="column" width="85%">
\scriptsize

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|  6 |  8 | 12 | 14 | 20 | 21 | 22 | 30 | 40 | 41 | 43 | 47 | 50 | 70 |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
  0    1    2    3    4    6    7    8    9    10   11   12   13   14
```
</div>
</div>


## Encadeamento e busca binária? {.b}

<div class="columns">
<div class="column" width="15%">
</div>
<div class="column" width="85%">
\scriptsize

```
                              +----+
                              | 22 |
                          /   +----+   \
                      /                    \
                  /                            \
              /                                    \
+----+----+----+----+----+----+    +----+----+----+----+----+----+----+
|  6 |  8 | 12 | 14 | 20 | 21 |    | 30 | 40 | 41 | 43 | 47 | 50 | 70 |
+----+----+----+----+----+----+    +----+----+----+----+----+----+----+
  0    1    2    3    4    6    7    8    9    10   11   12   13   14
```
</div>
</div>


## Encadeamento e busca binária? {.b}

<div class="columns">
<div class="column" width="15%">
</div>
<div class="column" width="85%">
\scriptsize

```
                              +----+
                              | 22 |
                          /   +----+   \
                      /                    \
                  /                            \
              /                                    \
          +----+                                  +----+
          | 12 |                                  | 43 |
        / +----+ \                              / +----+ \
      /            \                          /            \
    /                \                      /                \
+----+----+    +----+----+----+    +----+----+----+    +----+----+----+
|  6 |  8 |    | 14 | 20 | 21 |    | 30 | 40 | 41 |    | 47 | 50 | 70 |
+----+----+    +----+----+----+    +----+----+----+    +----+----+----+
  0    1    2    3    4    6    7    8    9    10   11   12   13   14
```
</div>
</div>


## Encadeamento e busca binária? {.b}

<div class="columns">
<div class="column" width="15%">
</div>
<div class="column" width="85%">
\scriptsize

```
                              +----+
                              | 22 |
                          /   +----+   \
                      /                    \
                  /                            \
              /                                    \
          +----+                                  +----+
          | 12 |                                  | 43 |
        / +----+ \                              / +----+ \
      /            \                          /            \
    /                \                      /                \
+----+              +----+              +----+              +----+
|  6 |              | 20 |              | 40 |              | 50 |
+----+              +----+              +----+              +----+
      \            /      \            /      \            /      \
     +----+    +----+    +----+    +----+    +----+    +----+    +----+
     |  8 |    | 14 |    | 21 |    | 30 |    | 41 |    | 47 |    | 70 |
     +----+    +----+    +----+    +----+    +----+    +----+    +----+
  0    1    2    3    4    6    7    8    9    10   11   12   13   14
```
</div>
</div>


## Árvore

Essa tipo de estrutura é chamada de árvore binária, especificamente, uma **árvore binária de busca**. \pause

Vire de ponta cabeça para ver a árvore!!! \pause As árvores em computação crescem para baixo! \pause

\includegraphics[width=4.5cm]{imagens/arvore-binaria-real.jpg} \pause

Como podemos definir uma árvore binária?


## Definição de árvore

Uma **árvore binária** é:

- Vazia; ou
- Um nó com uma chave e uma **árvore binária** a esquerda e uma **árvore binária** a direita.

\pause

Note que esta definição de árvore não impõe nenhuma restrição sobre as chaves. \pause

Para podemos usar uma árvore binária para fazer uma busca binária, vamos precisar adicionar restrições sobre as chaves. \pause

Mas antes, vamos ver alguns definições e exemplos.


## Algumas definições

<div class="columns">
<div class="column" width="48%">
Um nó é a **raiz** da árvore composta por ele e por suas subárvores. \pause

\ \

Se $A$ é o nó raiz de uma árvore e $B$ é o nó raiz de uma das subárvores de $A$, então, $B$ é **filho** de $A$ e $A$ é **pai** de $B$. \pause

\ \

Um nó $A$ é **ancestral** de um nó $B$ se $A$ é pai de $B$ ou pai de algum ancestral de $B$. Se $A$ é ancestral de $B$, então $B$ é **descendente** de $A$.

\pause

</div>
<div class="column" width="48%">

\scriptsize

```
          4
        /   \
     /         \
    8           6
  /   \       /
 2     7     5
        \
         1
```

\ \

\pause

\normalsize

Quem são os filhos do nó 4? \pause O nós 8 e 6. \pause

Quem é o pai do nó 7? \pause O nó 8. \pause

Quem são os descendentes do nó 8? \pause Os nós 2, 7 e 1. \pause

Quem são os ancestrais do no 5? \pause Os nós 6 e 4.

</div>
</div>


## Árvores binárias em Python

<div class="columns">
<div class="column" width="40%">
Como representar uma árvore binária? \pause

\scriptsize
\ \

```python
@dataclass
class No:
    esq: Arvore
    chave: int
    dir: Arvore

Arvore = No | None
```

\ \

\pause

\normalsize

Como criar a seguinte árvore?

\scriptsize

```
      t4  4
        /   \
     /         \
t2  8           6  t3
  /   \       /
 4  t1 7     5
        \
         1
```

\pause

</div>
<div class="column" width="58%">
\scriptsize

```python
>>> t1 = No(None, 7, No(None, 1, None))
>>> t1
No(esq=None, chave=7, dir=No(esq=None, chave=1, dir=None))
```

\pause

```python
>>> t2 = No(No(None, 4, None), 8, t1)
>>> t3 = No(No(None, 5, None), 6, None)
>>> t4 = No(t2, 4, t3)
```

\pause

\ \

\normalsize

Como acessar a chave 1 a partir de `t4`?

\pause

\scriptsize

```python
>>> t4.esq.dir.dir.chave
```

\ \

\pause

\normalsize

Como adicionar uma nova subárvore (chave 4) a esquerda de `t3` a partir de `t4`? \pause

\scriptsize

```python
>>> t4.dir.dir = No(None, 4, None)
```

\ \

\pause

\normalsize

Como remover a subárvore a direita de `t2` a partir de `t4`? \pause

\scriptsize

```python
>>> t4.esq.dir = None
```
</div>
</div>


## Projeto de funções que processam árvores

<div class="columns">
<div class="column" width="48%">

Como projetar funções que processam árvores? \pause

\ \
\scriptsize

```python
@dataclass
class No:
    esq: Arvore
    chave: int
    dir: Arvore

Arvore = No | None
```

\pause

</div>
<div class="column" width="48%">

`Arvore` é um tipo com autorreferência, então podemos derivar um modelo de função recursiva para processar uma árvore:

\pause

\ \

\scriptsize

```python
def fn_para_ab(t: Arvore) -> ...:
    if t is None:
        return ...
    else:
        return t.chave ... \
               fn_para_ab(t.esq) ... \
               fn_para_ab(t.dir)
```

</div>
</div>


## Projeto de funções que processam árvores

Como o modelo guia a implementação da função? \pause

O modelo indica que, para processarmos um árvore, temos que ter pelo menos dois casos, uma para a árvore vazia, e outro para a árvore não vazia. \pause

Além disso, no caso de árvore não vazia, o modelo sugere chamar a função recursivamente para as árvores a esquerda e a direita. (Por que?) \pause

O nosso trabalho é determinar como combinar a chave do nó raiz com as respostas das chamadas recursivas para obter a resposta da função. \pause

Nos exemplos a seguir, partimos do modelo e fazemos a implementação de algumas funções.


## Projeto de funções que processam árvores

\Large

\centering

Tente completar as funções antes de ver as repostas.


## Número de folhas {.t}

<div class="columns">
<div class="column" width="45%">
O **grau** de um nó é o número de filhos do nó. \pause

Um **nó folha** é aquele que tem grau 0. \pause

Um **nó interno** é aquele que não é folha. \pause

Projete uma função que determine a quantidade de nós folhas de uma árvore. \pause

\scriptsize

\ \

```
      t4  4
        /   \
     /         \
t2  8           6  t3
  /   \       /
 4  t1 7     5
        \
         1
```

\pause

</div>
<div class="column" width="50%">
\scriptsize

```python
def num_folhas(t: Arvore) -> int:
    '''
    Determina a quantidade de folhas em *t*.
    Uma folha é um nó sem nenhum filho.
    >>> num_folhas(t2)
    2
    >>> num_folhas(t3)
    1
    >>> num_folhas(t4)
    3
    '''
```

\pause

```python
    if t is None:
        return ...
    else:
        return self.chave ... \
               num_folhas(t.esq) ... \
               num_folhas(t.dir)
```

</div>
</div>


## Número de folhas {.t}

<div class="columns">
<div class="column" width="45%">
O **grau** de um nó é o número de filhos do nó.

Um **nó folha** é aquele que tem grau 0.

Um **nó interno** é aquele que não é folha.

Projete uma função que determine a quantidade de nós folhas de uma árvore.

\scriptsize

\ \

```
      t4  4
        /   \
     /         \
t2  8           6  t3
  /   \       /
 4  t1 7     5
        \
         1
```

</div>
<div class="column" width="50%">
\scriptsize

```python
def num_folhas(t: Arvore) -> int:
    '''
    Determina a quantidade de folhas em *t*.
    Uma folha é um nó sem nenhum filho.
    >>> num_folhas(t2)
    2
    >>> num_folhas(t3)
    1
    >>> num_folhas(t4)
    3
    '''
```

```python
    if t is None:
        return 0
    else:
        if t.esq is None and t.dir is None:
            return 1
        else:
            return num_folhas(t.esq) + num_folhas(t.dir)
```

</div>
</div>


## Nível e altura

<div class="columns">
<div class="column" width="45%">

O **nível** de um nó em uma árvore é:

- `0`{.python} se o nó é a raiz da árvore; ou
- O **nível** do pai mais 1 caso contrário \pause

\ \

A **altura** (ou profundidade) de um nó é o máximo entre os níveis de todas as folhas da árvore com raiz nesse nó. \pause

\ \

De outra forma, é o comprimento do caminho mais longo deste o nó até uma folha. \pause

</div>
<div class="column" width="50%">

\scriptsize

```
      t4  4
        /   \
     /         \
t2  8           6  t3
  /   \       /
 4  t1 7     5
        \
      t0 1
```

\ \

\normalsize

Em relação a `t4`, qual é o nível de: \pause

`t4`? \pause 0. \pause
`t2`? \pause 1. \pause
`t3`? \pause 1. \pause
`t1`? \pause 2. \pause
`t0`? \pause 3. \pause

\ \

Qual é a altura da árvore: \pause

`t0`? \pause 0. \pause
`t1`? \pause 1. \pause
`t2`? \pause 2. \pause
`t3`? \pause 1. \pause
`t4`? \pause 3. \pause

\ \

Qual é a altura da árvore vazia? \pause -1 (convenção).

</div>
</div>


## Altura {.t}

<div class="columns">
<div class="column" width="45%">

Projete uma função que determine a altura de uma árvore.

\ \

\scriptsize

```
      t4  4
        /   \
     /         \
t2  8           6  t3
  /   \       /
 4  t1 7     5
        \
      t0 1
```

\pause

</div>
<div class="column" width="50%">

\scriptsize

```python
def altura(t: Arvore) -> int:
    '''
    Devolve a altura da árvore *t*, isto é, o
    comprimeiro do caminho mais longo da raíz
    até um no folha. Devolve -1 se *t* é None.
    >>> altura(None)
    -1
    >>> altura(t1)
    1
    >>> altura(t4)
    3
    '''
```

\pause

```python
    if t is None:
        return ...
    else:
        return t.chave ... \
               altura(t.esq)
               altura(t.dir)
```

</div>
</div>


## Altura {.t}

<div class="columns">
<div class="column" width="45%">

Projete uma função que determine a altura de uma árvore.

\ \

\scriptsize

```
      t4  4
        /   \
     /         \
t2  8           6  t3
  /   \       /
 4  t1 7     5
        \
      t0 1
```

</div>
<div class="column" width="50%">

\scriptsize

```python
def altura(t: Arvore) -> int:
    '''
    Devolve a altura da árvore *t*, isto é, o
    comprimeiro do caminho mais longo da raíz
    até um no folha. Devolve -1 se *t* é None.
    >>> altura(None)
    -1
    >>> altura(t1)
    1
    >>> altura(t4)
    3
    '''
```

```python
    if t is None:
        return -1
    else:
        return 1 + \
               max(altura(t.esq), altura(t.dir))
```

</div>
</div>


## Nível {.t}

<div class="columns">
<div class="column" width="45%">

Projete uma função que encontre todos as chaves em um determinado nível de uma árvore.

\ \

\scriptsize

```
      t4  4
        /   \
     /         \
t2  8           6  t3
  /   \       /
 4  t1 7     5
        \
      t0 1
```

\pause

</div>
<div class="column" width="50%">

\scriptsize

```python
def chaves_nivel(t: Arvore, n: int) -> list[int]:
    '''
    Devolve os nós que estão no nível *n* de *t*.
    >>> chaves_nivel(None, 0)
    []
    >>> chaves_nivel(t4, 0)
    [4]
    >>> chaves_nivel(t4, 2)
    [4, 7, 5]
    >>> chaves_nivel(t4, 3)
    [1]
    '''
```

\pause

```python
    if t is None:
        return ... n
    else:
        return n ... \
               t.chave ... \
               chaves_nivel(t.esq, ...) ... \
               chaves_nivel(t.dir, ...) ...
```

</div>
</div>


## Nível {.t}

<div class="columns">
<div class="column" width="45%">

Projete uma função que encontre todos as chaves em um determinado nível de uma árvore.

\ \

\scriptsize

```
      t4  4
        /   \
     /         \
t2  8           6  t3
  /   \       /
 4  t1 7     5
        \
      t0 1
```

</div>
<div class="column" width="50%">

\scriptsize

```python
def chaves_nivel(t: Arvore, n: int) -> list[int]:
    '''
    Devolve os nós que estão no nível *n* de *t*.
    >>> chaves_nivel(None, 0)
    []
    >>> chaves_nivel(t4, 0)
    [4]
    >>> chaves_nivel(t4, 2)
    [4, 7, 5]
    >>> chaves_nivel(t4, 3)
    [1]
    '''
    if t is None:
        return []
    elif n == 0:
        return [t.chave]
    else:
        return chaves_nivel(t.esq, n - 1) + \
                   chaves_nivel(t.dir, n - 1)
```

</div>
</div>


## Árvore binária de busca

O que é preciso para podemos fazer uma busca binária em um árvore binária? \pause Que ela seja de busca! \pause

Uma **árvore binária de busca** (ABB) é uma árvore binária que, quando não é vazia, tem uma raiz $t$ e: \pause

- Todos os elementos da subárvore a esquerda de $t$ são menores que $t.chave$; \pause
- Todos os elementos da subárvore a direita de $t$ são maiores que $t.chave$; \pause
- As subárvores a esquerda e a direta de $t$ são **árvores binárias de busca**.


## Busca em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="50%">

\small

Busca $v$ em uma ABB $t$:

- Se $t$ é vazia, $v$ não está na árvore;
- Se $v$ é igual a $t.chave$, $v$ está na árvore;
- Senão, se $v$ é menor que $t.chave$, continuamos a busca na subárvore a esquerda;
- Senão ($v$ é maior que $t.chave$), continuamos a busca na subárvore a direita. \pause

Implemente o algoritmo de busca para uma árvore binária de busca. \pause

\scriptsize

```
          4
        /   \
     /         \
    1           7
  /   \       /
-3     2     5
        \
         3
```

\pause

</div>
<div class="column" width="46%">
\scriptsize

```python
def busca(t: Arvore, chave: int) -> bool:
    '''
    Devolve True se *chave* está em *t*,
    False caso contrário.
    >>> busca(None, 10)
    False
    >>> busca(t, 2)
    True
    >>> busca(t, 6)
    False
    '''
    if t is None:
        return ... chave
    else:
        return chave ... \
               t.chave ... \
               busca(t.esq, chave) ... \
               busca(t.dir, chave) ...
```

</div>
</div>


## Busca em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="50%">

\small

Busca $v$ em uma ABB $t$:

- Se $t$ é vazia, $v$ não está na árvore;
- Se $v$ é igual a $t.chave$, $v$ está na árvore;
- Senão, se $v$ é menor que $t.chave$, continuamos a busca na subárvore a esquerda;
- Senão ($v$ é maior que $t.chave$), continuamos a busca na subárvore a direita.

Implemente o algoritmo de busca para uma árvore binária de busca.

\scriptsize

```
          4
        /   \
     /         \
    1           7
  /   \       /
-3     2     5
        \
         3
```

</div>
<div class="column" width="46%">
\scriptsize

```python
def busca(t: Arvore, chave: int) -> bool:
    r'''
    Devolve True se *chave* está em *t*,
    False caso contrário.
    >>> busca(None, 10)
    False
    >>> busca(t, 2)
    True
    >>> busca(t, 6)
    False
    '''
    if t is None:
        return False
    elif chave == t.chave:
        return True
    elif chave < t.chave:
        return busca(t.esq, chave)
    else:  # chave > t.chave
        return busca(t.dir, chave)
```

</div>
</div>


## Busca em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="50%">

\small

Busca $v$ em uma ABB $t$:

- Se $t$ é vazia, $v$ não está na árvore;
- Se $v$ é igual a $t.chave$, $v$ está na árvore;
- Senão, se $v$ é menor que $t.chave$, continuamos a busca na subárvore a esquerda;
- Senão ($v$ é maior que $t.chave$), continuamos a busca na subárvore a direita.

Implemente o algoritmo de busca para uma árvore binária de busca.

\scriptsize

```
          4
        /   \
     /         \
    1           7
  /   \       /
-3     2     5
        \
         3
```

</div>
<div class="column" width="46%">
\scriptsize

```python
def busca(t: Arvore, chave: int) -> bool:
    r'''
    Devolve True se *chave* está em *t*,
    False caso contrário.
    >>> busca(None, 10)
    False
    >>> busca(t, 2)
    True
    >>> busca(t, 6)
    False
    '''
    r = t
    while r is not None:
        if chave == r.chave:
            return True
        elif chave < r.chave:
            r = r.esq
        else:  # chave > r.chave
            r = r.dir
    return False
```

</div>
</div>


## Complexidade de tempo da busca em ABB

<div class="columns">
<div class="column" width="42%">

\scriptsize

```python
def busca(t: Arvore, chave: int) -> bool:
    if t is None:
        return False
    elif chave == t.chave:
        return True
    elif chave < t.chave:
        return busca(t.esq, chave)
    else:  # chave > t.chave
        return busca(t.dir, chave)

def busca(t: Arvore, chave: int) -> bool:
    r = t
    while r is not None:
        if chave == r.chave:
            return True
        elif chave < r.chave:
            r = r.esq
        else:  # chave > r.chave
            r = r.dir
    return False
```

</div>
<div class="column" width="54%">

Qual é a complexidade de tempo do algoritmo de busca em árvore binária de busca? \pause $O(h)$, onde $h$ é a altura da árvore. \pause

Qual é a relação entre a quantidade $n$ de elementos da árvore e $h$? \pause

Qual é o limite superior de $h$? \pause $n - 1$. \pause Ocorre quando todos os nós da árvore, exceto as folhas, têm apenas um filho. \pause


Qual é o limite inferior de $h$? \pause $\lg(n)$. \pause Ocorre quando todos os níveis da árvore estão cheios, exceto talvez, o último nível. \pause

O que podemos concluir sobre isso? \pause Para que a busca em uma ABB seja eficiente, precisamos manter a altura da árvore perto do valor mínimo.

</div>
</div>


## Complexidade de tempo da busca em ABB

Fato: uma ABB criada com $n$ chaves aleatórias tem altura média de $1.39 \lg n$. \pause

Então, se as chaves usadas nas inserções e remoções tem uma distribuição aleatória, a ABB resultante tem uma altura pequena. \pause

Como manter a altura pequena em uma árvore para qualquer distribuição de chaves? \pause Veremos daqui a pouco. \pause

Agora vamos ver como inserir e remover valores de uma ABB sem se preocupar com a altura.


## Inserção em árvore binária de busca

Projete uma função que insira uma nova chave, se ainda não estiver presente, em uma árvore binária de busca. \pause

Quais são os tipos dos parâmetros da função? \pause `Arvore`{.python} e `int`{.python}. \pause

Quais deve ser o tipo de saída da função? \pause `None`{.python}? \pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, chave: int) -> None:
    '''
    Insere *chave* em *t* mantendo as
    propriedades de ABB.
    Requer que *t* seja uma ABB.
    >>> r = None
    >>> insere(r, 10)
    >>> r
    No(esq=None, chave=10, dir=None)
    '''
```

\pause

</div>
<div class="column" width="48%">
É possível implementar a função para que o exemplo funcione? \pause Não! \pause

Dentro da função é preciso fazer `t` referenciar um novo nó, mas quando fazemos isso, `r` permanece inalterado...
</div>
</div>


## Inserção em árvore binária de busca

Como resolver essa questão? \pause Alterando o tipo de retorno para `No`{.pause} e atribuindo o retorno para `r`.

\pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, chave: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *chave* em *t*.
    Se *chave* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.

    Exemplo
    >>> r = None
    >>> r = insere(r, 10)
    >>> r
    No(esq=None, chave=10, dir=None)
    '''
```

\pause
</div>
<div class="column" width="48%">

\normalsize

Como proceder com a implementação? \pause

Partindo do modelo! \pause

Mas temos que lembrar que quando chamamos `insere` é preciso armazenar o resultado no lugar da raiz que foi chamada como parâmetro.

</div>
</div>


## Inserção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\scriptsize

```
       ins
None   --->   7
        7
```

\vspace{0.3cm}
\pause

```
7   ins       7     ins        7
    --->     /      --->     /
     4     4         6      4
                             \
                              6
```

\vspace{0.3cm}
\pause

```
    7   ins        7       ins        7
  /     --->     /   \     --->     /   \
4       10     4      10    9     4      10
 \              \                  \     /
  6              6                  6   9
```

\vspace{0.3cm}
\pause

```
    7       ins       7
  /   \     --->    /   \
4      10   12    4      10
 \     /           \    /  \
  6   9             6  9   12
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, chave: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *chave* em *t*.
    Se *chave* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return ... chave
    else:
        chave ...
        t.chave ...
        insere(t.esq, chave) ...
        insere(t.dir, chave) ...
        return ...
```
</div>
</div>


## Inserção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\scriptsize

```
       ins
None   --->   7
        7
```

\vspace{0.3cm}

```
7   ins       7     ins        7
    --->     /      --->     /
     4     4         6      4
                             \
                              6
```

\vspace{0.3cm}

```
    7   ins        7       ins        7
  /     --->     /   \     --->     /   \
4       10     4      10    9     4      10
 \              \                  \     /
  6              6                  6   9
```

\vspace{0.3cm}

```
    7       ins       7
  /   \     --->    /   \
4      10   12    4      10
 \     /           \    /  \
  6   9             6  9   12
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, chave: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *chave* em *t*.
    Se *chave* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return ... chave
    else:
        chave ...
        t.chave ...
        t.esq = insere(t.esq, chave) ...
        t.dir = insere(t.dir, chave) ...
        return ...
```
</div>
</div>


## Inserção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\scriptsize

```
       ins
None   --->   7
        7
```

\vspace{0.3cm}

```
7   ins       7     ins        7
    --->     /      --->     /
     4     4         6      4
                             \
                              6
```

\vspace{0.3cm}

```
    7   ins        7       ins        7
  /     --->     /   \     --->     /   \
4       10     4      10    9     4      10
 \              \                  \     /
  6              6                  6   9
```

\vspace{0.3cm}

```
    7       ins       7
  /   \     --->    /   \
4      10   12    4      10
 \     /           \    /  \
  6   9             6  9   12
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, chave: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *chave* em *t*.
    Se *chave* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return No(None, chave, None)
    else:
        chave ...
        t.chave ...
        t.esq = insere(t.esq, chave) ...
        t.dir = insere(t.dir, chave) ...
        return ...
```
</div>
</div>


## Inserção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\scriptsize

```
       ins
None   --->   7
        7
```

\vspace{0.3cm}

```
7   ins       7     ins        7
    --->     /      --->     /
     4     4         6      4
                             \
                              6
```

\vspace{0.3cm}

```
    7   ins        7       ins        7
  /     --->     /   \     --->     /   \
4       10     4      10    9     4      10
 \              \                  \     /
  6              6                  6   9
```

\vspace{0.3cm}

```
    7       ins       7
  /   \     --->    /   \
4      10   12    4      10
 \     /           \    /  \
  6   9             6  9   12
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, chave: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *chave* em *t*.
    Se *chave* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return No(None, chave, None)
    else:
        if chave < t.chave:
            t.esq = insere(t.esq, chave)
        elif chave > t.chave:
            t.dir = insere(t.dir, chave)
        else: # chave == t.chave
            pass
        return t
```
</div>
</div>


## Inserção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def insere(t: Arvore, chave: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *chave* em *t*.
    Se *chave* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return No(None, chave, None)
    else:
        if chave < t.chave:
            t.esq = insere(t.esq, chave)
        elif chave > t.chave:
            t.dir = insere(t.dir, chave)
        else: # chave == t.chave
            pass
        return t
```

</div>
<div class="column" width="48%">

Qual é a complexidade de tempo da inserção? \pause

$O(h)$. \pause

$O(1)$ operações para cada nó analisado. No pior caso todos os nós de um caminho de tamanho máximo são analisados.
</div>
</div>


## Remoção em árvore binária de busca

Projete uma função que remova uma chave, se estiver presente, de uma árvore binária de busca.

\pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def remove(t: Arvore, chave: int) -> Arvore:
    '''
    Devolve a raiz da ABB que é o resultado
    da remoção de *chave* de *t*.
    Se *chave* não está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.

    Exemplo
    >>> r = No(None, 10, None)
    >>> r = remove(r, 10)
    >>> r is None
    True
    '''
```

\pause
</div>
<div class="column" width="48%">

\normalsize

Como proceder com a implementação? \pause

Partindo do modelo! \pause

Mas temos que lembrar que quando chamamos `remove` é preciso armazenar o resultado no lugar da raiz que foi passada como parâmetro.

</div>
</div>


## Remoção em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: \pause retorna `None`{.python}. \pause

\small
\ \

Remoção de nó sem subárvore a esq ou dir

\scriptsize

```
     7       rem        7      rem      7
  /     \    --->     /   \    --->    / \
2        10   2     4      10   10    4   8
 \      /          / \    /          / \   \
  4    8          3   6  8          3   6   9
 / \    \                 \
3   6    9                 9
```


\pause

\small
\ \

Remoção de nó com subárvore a esq e a dir

\scriptsize

```
    7     rem      6           6
   / \    --->    / \         / \
  4   8    7     4   8       4   8
 / \   \        / \   \     /     \
3   6   9      3   6   9   3       9
               copia max    remove
               esquerda     max esq
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def remove(t: Arvore, chave: int) -> Arvore:
    '''
    Devolve a raiz da ABB que é o resultado
    da remoção de *chave* de *t*.
    Se *chave* não está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return ... chave
    else:
        chave ...
        t.chave ...
        remove(t.esq, chave) ...
        remove(t.dir, chave) ...
        return ...
```
</div>
</div>


## Remoção em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: retorna `None`{.python}.

\small
\ \

Remoção de nó sem subárvore a esq ou dir

\scriptsize

```
     7       rem        7      rem      7
  /     \    --->     /   \    --->    / \
2        10   2     4      10   10    4   8
 \      /          / \    /          / \   \
  4    8          3   6  8          3   6   9
 / \    \                 \
3   6    9                 9
```

\small
\ \

Remoção de nó com subárvore a esq e a dir

\scriptsize

```
    7     rem      6           6
   / \    --->    / \         / \
  4   8    7     4   8       4   8
 / \   \        / \   \     /     \
3   6   9      3   6   9   3       9
               copia max    remove
               esquerda     max esq
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def remove(t: Arvore, chave: int) -> Arvore:
    '''
    Devolve a raiz da ABB que é o resultado
    da remoção de *chave* de *t*.
    Se *chave* não está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return None
    else:
        chave ...
        t.chave ...
        t.esq = remove(t.esq, chave) ...
        t.dir = remove(t.dir, chave) ...
        return ...
```
</div>
</div>


## Remoção em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: retorna `None`{.python}.

\small
\ \

Remoção de nó sem subárvore a esq ou dir

\scriptsize

```
     7       rem        7      rem      7
  /     \    --->     /   \    --->    / \
2        10   2     4      10   10    4   8
 \      /          / \    /          / \   \
  4    8          3   6  8          3   6   9
 / \    \                 \
3   6    9                 9
```

\small
\ \

Remoção de nó com subárvore a esq e a dir

\scriptsize

```
    7     rem      6           6
   / \    --->    / \         / \
  4   8    7     4   8       4   8
 / \   \        / \   \     /     \
3   6   9      3   6   9   3       9
               copia max    remove
               esquerda     max esq
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def remove(t: Arvore, chave: int) -> Arvore:
    '''
    Devolve a raiz da ABB que é o resultado
    da remoção de *chave* de *t*.
    Se *chave* não está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return None
    elif chave < t.chave:
        t.esq = remove(t.esq, chave)
        return t
    elif chave > t.chave:
        t.dir = remove(t.dir, chave)
        return t
    else: # chave == t.chave
        chave, t.chave, t.esq, t.dir
        ... = remove(t.esq, ...) ...
        ... = remove(t.dir, ...) ...
        return ...
```
</div>
</div>


## Remoção em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: retorna `None`{.python}.

\small
\ \

Remoção de nó sem subárvore a esq ou dir

\scriptsize

```
     7       rem        7      rem      7
  /     \    --->     /   \    --->    / \
2        10   2     4      10   10    4   8
 \      /          / \    /          / \   \
  4    8          3   6  8          3   6   9
 / \    \                 \
3   6    9                 9
```

\small
\ \

Remoção de nó com subárvore a esq e a dir

\scriptsize

```
    7     rem      6           6
   / \    --->    / \         / \
  4   8    7     4   8       4   8
 / \   \        / \   \     /     \
3   6   9      3   6   9   3       9
               copia max    remove
               esquerda     max esq
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def remove(t: Arvore, chave: int) -> Arvore:
    if t is None:
        return None
    elif chave < t.chave:
        t.esq = remove(t.esq, chave)
        return t
    elif chave > t.chave:
        t.dir = remove(t.dir, chave)
        return t
    else: # chave == t.chave
        if t.esq is None:
            return t.dir
        elif t.dir is None:
            return t.esq
        else:
            chave, t.chave, t.esq, t.dir ...
            ... = remove(t.esq, ...) ...
            ... = remove(t.dir, ...) ...
            return ...
```
</div>
</div>


## Remoção em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: retorna `None`{.python}.

\small
\ \

Remoção de nó sem subárvore a esq ou dir

\scriptsize

```
     7       rem        7      rem      7
  /     \    --->     /   \    --->    / \
2        10   2     4      10   10    4   8
 \      /          / \    /          / \   \
  4    8          3   6  8          3   6   9
 / \    \                 \
3   6    9                 9
```

\small
\ \

Remoção de nó com subárvore a esq e a dir

\scriptsize

```
    7     rem      6           6
   / \    --->    / \         / \
  4   8    7     4   8       4   8
 / \   \        / \   \     /     \
3   6   9      3   6   9   3       9
               copia max    remove
               esquerda     max esq
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def remove(t: Arvore, chave: int) -> Arvore:
    if t is None:
        return None
    elif chave < t.chave:
        t.esq = remove(t.esq, chave)
        return t
    elif chave > t.chave:
        t.dir = remove(t.dir, chave)
        return t
    else: # chave == t.chave
        if t.esq is None:
            return t.dir
        elif t.dir is None:
            return t.esq
        else:
            m = maximo(t.esq)
            t.chave = m
            t.esq = remove(t.esq, m)
            return t
```
</div>
</div>


## Remoção em árvore binária de busca {.t}

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def remove(t: Arvore, chave: int) -> Arvore:
    if t is None:
        return None
    elif chave < t.chave:
        t.esq = remove(t.esq, chave)
        return t
    elif chave > t.chave:
        t.dir = remove(t.dir, chave)
        return t
    else: # chave == t.chave
        if t.esq is None:
            return t.dir
        elif t.dir is None:
            return t.esq
        else:
            m = maximo(t.esq)
            t.chave = m
            t.esq = remove(t.esq, m)
            return t
```

</div>
<div class="column" width="48%">
Qual é a complexidade de tempo da remoção? \pause

$O(h)$. \pause

$O(1)$ operações para cada nó analisado. No pior caso, todos os nós de um caminho de tamanho máximo são analisados.
</div>
</div>


## Complexidade de tempo das operações em uma ABB

A complexidade de tempo das operações de busca, inserção e remoção em uma ABB tem tempo de execução $O(h)$. \pause

Como vimos anteriormente, se as chaves usadas nas inserções e remoções têm distribuição aleatória, então a altura média da ABB é $O(\lg n)$. \pause

Como garantir que a altura seja $O(\lg n)$ para uma distribuição qualquer de chaves? \pause

Mantendo a árvore balanceada.


## Referências

Capítulo 10 - Árvores - Fundamentos de Python: Estruturas de dados. Kenneth A. Lambert. (Disponível na Minha Biblioteca na UEM).

Capítulo 12 - Árvores Binárias de Busca - Algoritmos: Teoria e Prática, 3a. edição, Cormen, T. at all.

Capítulo 6 - Binary Trees - [Open Data Structures](https://opendatastructures.org/ods-python.pdf).
