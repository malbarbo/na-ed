---
# vim: set spell spelllang=pt_br:
title: Árvores AVL
linkcolor: Black
urlcolor: Blue
# TODO: criar mais um coleção de slides sobre percursos em árvores (https://en.wikipedia.org/wiki/Tree_traversal)
---

## Árvores binárias balanceadas

Informalmente, uma árvore é **balanceada** (na altura), quando a diferença das alturas das suas subárvores é "pequena" e as subárvores são **balanceadas**. \pause Ou ainda, uma árvore que tem altura $O(\lg n)$. \pause

Uma **árvore binária de busca auto balanceada** é aquela que se mantém balanceada após cada modificação. \pause

Existem diversos tipos de ABB auto balanceadas, entre elas: AVL, rubro-negra e treap.


## Árvore AVL

A árvore AVL (nomeada a partir do nome dos criadores - **A**delson-**V**elsky and **L**andis) foi a primeira árvore auto balanceada a ser criada (1962). \pause

Uma **árvore AVL**, é uma ABB de busca, que quando não é vazia, tem uma raiz $t$ e: \pause

- A diferença absoluta da altura das subárvores a direita e a esquerda de $t$ é no máximo 1; \pause
- As subárvores a esquerda e direita de $t$ são **AVL**. \pause

Para representar uma AVL, é preciso adicionar um atributo `altura` na classe `No`.


## Árvore AVL

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore
    altura: int

Arvore = No | None
```

\ \

\pause

```python
def altura(t: Arvore) -> Int:
    '''
    Devolve a altura da árvore *t*.
    Devolve -1 se *t* é None.
    '''
    if t is None:
        return -1
    else:
        return t.altura
```

\pause
</div>
<div class="column" width="48%">
Considere as seguintes árvore, onde cada nó é representado pelo seu valor e altura:

\scriptsize

\ \

```
                  20:4  t0
                /      \
            /             \
    t1  7:3              27:1  t2
      /     \           /   \
    4:2    10:1      22:0  30:0
   /  \       \
 3:0   6:1    12:0
      /
    5:0
```

\pause

\normalsize

A árvore t1 é AVL? \pause Sim. \pause

A árvore t2 é AVL? \pause Sim. \pause

A árvore t0 é AVL? \pause Não.


</div>
</div>


## Rebalanceamento e rotação

Quando um nó é inserido ou removido e a regra de balanceamento é violada, é preciso ajustar a árvore para restabelecer o balanceamento (**rebalancear**), o que é feito através de operações de rotações. \pause

Uma **rotação** é uma operação que muda localmente a estrutura de uma ABB, mas mantém a propriedade de busca. \pause No contexto de árvore AVL, a operação de rotação também deve ajustar o atributo altura dos nós envolvidos na rotação.

\pause

\scriptsize

```python
def atualiza_altura(no: No):
    '''
    Atualiza a altura do *no*.
    Requer que a altura de *no.esq* e *no.dir* esteja corretas.
    '''
    no.altura = 1 + max(altura(no.esq), altura(no.dir))
```


## Rebalanceamento e rotação

Na figura abaixo, $x$ e $y$ representam valores armazenados nos nós e $A$, $B$ e $C$ representam subárvores.

\pause

<div class="columns">
<div class="column" width="25%">
</div>
<div class="column" width="75%">
\scriptsize

```
    y      rotação a direita       x
   / \     ----------------->     / \
  x   C                          A   y
 / \       rotação a esquerda       / \
A   B      <-----------------      B   C


```

</div>
</div>

\normalsize

\pause

Note que $A < x < B < y < C$ nas duas figuras. Ou seja, essas rotações não alteram a propriedade de ABB. \pause

Veja uma [animação](https://en.wikipedia.org/wiki/Tree_rotation#/media/File:Tree_rotation_animation_250x250.gif) da rotação e outras informações na página [Tree rotation](https://en.wikipedia.org/wiki/Tree_rotation).


## Rotação a esquerda

Projete uma função para fazer a rotação a esquerda de uma árvore não vazia com raiz `r`.

\pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def rotaciona_esq(r: No) -> No:
    r'''
    Rotaciona a árvore com raiz *r*
    conforme o seguinte esquema:

         r              x
        / \            / \
       A   x    ->    r   C
          / \        / \
         B   C      A   B

    E devolve como nova raiz o nó que estava
    em *r.dir* quando a função foi chamada.

    Requer que *r.dir* não seja None.
    '''
```
</div>
<div class="column" width="48%">
\pause

\scriptsize

```python
def rotaciona_esq(r: No) -> No:
    assert r.dir is not None
    x = r.dir
    r.dir = x.esq
    x.esq = r
    atualiza_altura(r)
    atualiza_altura(x)
    return x
```

\pause

\normalsize

Exercício: projete a função para fazer a rotação a direita.
</div>
</div>


## Exemplo de inserção em árvore AVL

Crie uma árvore AVL inserindo os seguintes itens na ordem que eles aparecem: 20, 10, 5, 30, 40, 25, 8, 2, 6, 9, 12, 14.

\pause

Feito e discutido em sala.

Você pode conferir o resultado usando [este](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html) simulador. \pause

Agora que vimos o funcionamento das operações de rotação, vamos sistematizar a forma que o rebalanceamento é feito a partir dessas operações.


## Rebalanceamento

Quando uma árvore AVL com raiz $r$ tem a subárvore a esquerda ou a direita alterada, é necessário verificar se a propriedade de balanceamento foi violada. \pause Como fazer essa verificação? \pause

\scriptsize

```python
abs(altura(r.esq) - altura(r.dir)) == 2
```

\pause

```python
# Desbalanceamento a esquerda
altura(r.esq) > altura(r.dir) + 1

# Desbalanceamento a direita
altura(r.dir) > altura(r.esq) + 1
```


\normalsize

\pause

Se existe violação, é necessário rebalancear a árvore usando rotações. \pause

**Note que o rebalanceamento não é feito em uma árvore qualquer, mas sim em uma árvore AVL que acabou de ficar desbalanceada devido a inserção ou remoção de um elemento.**


## Rebalanceamento

Se a subárvore a esquerda tem altura maior que a subárvore a direita, então fazemos o rebalanceamento a esquerda, senão fazemos o rebalanceamento a direita. \pause

Como o rebalanceamento a esquerda afeta as alturas das subárvores? \pause

- Aumenta a altura da árvore a direita \pause

- Diminui a altura da árvore a esquerda \pause


Como o rebalanceamento a direita afeta as alturas das subárvores? \pause

- Aumenta a altura da árvore a esquerda \pause

- Diminui a altura da árvore a direita



## Rebalanceamento a esquerda

A forma que o rebalanceamento a esquerda de uma árvore AVL com raiz `r` é feito depende de qual das subárvores de `r.esq` tem maior altura.


## Rebalanceamento a esquerda-esquerda

Esquerda-Esquerda  -- \small `altura(r.esq.esq) > altura(r.esq.dir)`{.python}

\normalsize

\pause

<div class="columns">
<div class="column" width="48%">

\scriptsize

```
      r
    // \
    y   D
  // \
  x   C
 / \
A   B

h(r) > h(y) > h(x) > h(C) == h(D)
```

\normalsize

\pause

O que é preciso para rebalancear a árvore? \pause

\scriptsize

```python
return rotaciona_dir(r)
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```
     y
   /   \
  x     r
 / \   / \
A   B C   D
```

\pause

\normalsize

Note que a árvore tem uma nova raiz e que a altura da subárvore a esquerda diminui e a altura da subárvore a direita aumentou.

</div>
</div>


## Rebalanceamento a esquerda-direita

Esquerda-Direita -- \small `altura(r.esq.esq) < altura(r.esq.dir)`{.python}

\normalsize

\pause

<div class="columns">
<div class="column" width="48%">

\scriptsize

```
      r
    // \
    y   D
   / \\
  A   x
     / \
    B   C

h(r) > h(y) > h(x) > h(A) == h(D)
```

\normalsize

\pause

O que é preciso para rebalancear a árvore? \pause

\scriptsize

```python
# Transforma no caso esquerda-esquerda
r.esq = rotaciona_esq(r.esq)
```

\pause

```python
return rotaciona_dir(r)
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```
      r              x
     / \           /   \
    x   D         y     r
   / \           / \   / \
  y   C         A   B C   D
 / \
A   B
```

\pause

\normalsize

Note que a árvore fica com uma nova raiz e que a altura da subárvore a esquerda diminui e a altura da subárvore a direita aumenta.

</div>
</div>


## Rebalanceamento a esquerda - código

Projete uma função que implemente o esquema de rebalanceamento a esquerda (e a correção da altura da árvore).


## Rebalanceamento a esquerda - código

\scriptsize

```python
def rebalanceia_esq(r: No) -> No:
    '''
    Verifica o balanceamento de *r*, considerando o caso da subárvore a esquerda com maior altura,
    e faz o rebalanceamento e atualização das alturas se necessário. Devolve a raiz da árvore balanceada.
    '''
```

\pause

```python
    assert r.esq is not None
    if altura(r.esq) - altura(r.dir) == 2:
        # r está desbalaceada
        if altura(r.esq.esq) > altura(r.esq.dir):
            # Caso Esquerda-Esquerda
            return rotaciona_dir(r)
        else:
            # Caso Esquerda-Direita
            assert altura(r.esq.dir) > altura(r.esq.esq)
            r.esq = rotaciona_esq(r.esq)
            return rotaciona_dir(r)
    else:
        # r está balaceada
        atualiza_altura(r)
        return r
```


## Rebalanceamento a direita

Projete uma função que implemente o esquema de rebalanceamento a direita (e a correção da altura da árvore). \pause

Fica como exercício.


## Atualização da função de inserção

Atualize a função de inserção em ABB para árvores AVL. \pause

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def insere(t: Arvore, val: int) -> No:
    if t is None:
        return No(None, val, None)
    else:
        if val < t.val:
            t.esq = insere(t.esq, val)
        elif val > t.val:
            t.dir = insere(t.dir, val)
        else: # val == t.val
            pass
        return t
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
def insere(t: Arvore, val: int) -> No:
    if t is None:
        return No(None, val, None)
    else:
        if val < t.val:
            t.esq = insere(t.esq, val)
            t = rebalanceia_esq(t)
        elif val > t.val:
            t.dir = insere(t.dir, val)
            t = rebalanceia_dir(t)
        else: # val == t.val
            pass
        return t
```
</div>
</div>


## Atualização da função de remoção

Atualize a função de remoção em ABB para árvores AVL. \pause

Fica como exercício.


## Testes

As funções `busca`, `insere` e `remove` definem a interface de uso da ABB e AVL. \pause

Os exemplos servem tanto para mostrar para o usuário o uso da função e o seu comportamento. Os exemplos são bons testes iniciais para essas funções. \pause

Já as funções de rotação e balanceamento são funções auxiliares, não fazem parte da interface para o usuário. \pause Além disso, as funções são mais complicadas e interagem com outras funções. \pause Os exemplos podem não ser suficientes para um bom teste. \pause

Como proceder? \pause Fazendo testes de propriedade.


## Testes de propriedade

Em um teste de propriedade executamos uma função e verificamos se a saída mantém alguma propriedade específica. \pause

No caso de árvores AVL, podemos verificar se após cada inserção e remoção, a árvore continua sendo AVL. \pause

Veja o código no arquivo `avl.py`.


## Percursos em árvores com funções recursivas e iterativas

Veja o arquivo `percursos.py`.


## Revisão

Implementação do TAD dicionário: \pause

- Com arranjos e lista encadeada com busca linear, as operações de busca inserção e remoção tem tempo $O(n)$; \pause

- Com arranjos ordenados e busca binária, a busca tem tempo $O(\lg n)$ e a inserção e remoção $O(n)$; \pause

- Com ABB o tempo de busca, inserção e remoção é $O(h)$, onde $h$ é a altura da árvore. No caso médio o tempo é de $O(\lg n)$ e no pior caso $O(n)$; \pause

- Com árvore AVL o tempo de busca, inserção e remoção é $O(\lg n)$.


## Revisão

Podemos fazer melhor? \pause Sim! \pause

Quando usamos uma ABB ou AVL, precisamos manter os elementos "ordenados", para podermos fazer uma busca binária. \pause

A seguir vamos ver como fazer uma busca eficiente sem precisar manter os elementos ordenados.


## Referências

Capítulo 10 - Árvores - Fundamentos de Python: Estruturas de dados. Kenneth A. Lambert. (Disponível na Minha Biblioteca na UEM).

Capítulo 12 - Árvores Binárias de Busca - Algoritmos: Teoria e Prática, 3a. edição, Cormen, T. at all.

Capítulo 6 - Binary Trees - [Open Data Structures](https://opendatastructures.org/ods-python.pdf).
