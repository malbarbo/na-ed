---
# vim: set spell spelllang=pt_br:
title: Busca e árvores
linkcolor: Black
urlcolor: Blue
# TODO: mudar val para chave?
---

## Introdução

Os TAD's Pilha, Fila e FilaDupla, permitem o armazenamento e recuperação de itens independente do conteúdo. \pause

O TAD Lista tem apenas uma operação que é dependente do conteúdo: `remove_item`. \pause

Vamos estudar um TAD em que a maioria das operações depende do conteúdo dos itens armazenados.


## Dicionário

Um **dicionário**, também chamado de arranjo associativo, é um tipo abstrato de dados que representa uma coleção de associações chave-valor, onde cada chave é única. \pause

As operações comuns em um dicionário são a associação de uma chave com um valor, a consulta do valor associado com uma chave e a exclusão de uma chave e o valor associado.


## Dicionário

<div class="columns">
<div class="column" width="58%">

\scriptsize

```python
class Dicionario:
    '''Uma coleção de associações chave-valor, onde
    cada chave é única'''

  def num_itens(self) -> int:
      '''Devolve a quantidade de chaves no dicionário.'''

  def associa(self, chave: str, valor: int):
      '''Associa a *chave* com o *valor* no dicionário.
      Se *chave* já está associada com um valor, ele
      é sustituído por *valor*.'''

  def get(self, chave: str) -> int | None:
      ''' Devolve o valor associado com *chave* no dicio-
      nário ou None se a chave não está no dicionário.'''

  def remove(self, chave: str):
      ''' Remove a *chave* e o valor associado com ela do
      dicionário. Não faz nada se a *chave* não está no
      dicionário.'''
```

</div>
<div class="column" width="38%">

\pause

\scriptsize

```python
>>> d = Dicionario()
>>> d.num_itens()
0
>>> d.associa('Jorge', 25)
>>> d.associa('Bia', 40)
>>> d.num_itens()
2
>>> d.get('Jorge')
25
>>> d.get('Bia')
40
>>> d.get('Andre') is None
True
>>> d.associa('Bia', 50)
>>> d.get('Bia')
50
>>> d.remove('Jorge')
>>> d.get('Jorge') is None
True
>>> d.remove('Ana')
```
</div>
</div>


## Dicionário - Implementação com arranjo

<div class="columns">
<div class="column" width="48%">

Como podemos implementar o TAD Dicionário utilizando arranjo? \pause

- Armazenamos um par chave-valor em cada posição do arranjo. \pause
- Busca:  busca por todos os itens, se a chave está presente, devolve o valor associado, senão devolve `None`{.python}. \pause
- Associação: _busca_ por todos os itens, se a chave está presente, atualiza o valor, senão adiciona a nova associação chave-valor no final. \pause
- Remoção: _busca_ por todos os itens, se a chave está presente, troca pelo último item e remove o último. \pause

</div>
<div class="column" width="48%">
\scriptsize

```python
@dataclass class Item:
    chave: str
    valor: int

class Dicionario:
    itens: list[Item]

    def __init__(self) -> None:
        self.itens = []

    def num_itens(self) -> int:
        return len(self.itens)

    def __busca(self, chave: str) -> int | None:
        '''Devolve a posição da *chave* ou
        None se a *chave* não está presente.'''
        for i in range(len(self.itens)):
            if self.itens[i].chave == chave:
                return i
        return None
```
</div>
</div>


## Dicionário - Implementação com arranjo

<div class="columns">
<div class="column" width="55%">
\scriptsize

```python
class Dicionario:
    def associa(self, chave: str, valor: int):
        i = self.__busca(chave)
        if i is not None:
            self.itens[i].valor = valor
        else:
            self.itens.append(Item(chave, valor))

    def get(self, chave: str) -> int | None:
        # Operador walrus para simplificar :=
        if (i := self.__busca(chave)) is not None:
            return self.itens[i].valor
        else:
            return None

    def remove(self, chave: str):
        if (i := self.__busca(chave)) is not None:
            self.itens[i], self.itens[-1] = \
                self.itens[-1], self.itens[i]
            self.itens.pop()
```

</div>
<div class="column" width="43%">

Qual a complexidade de tempo das operações? \pause

Todas tem tempo de execução $O(n)$ pois requerem uma busca que pode analisar todos os itens. \pause

Será que podemos fazer melhor usando encadeamento linear? \pause

Não... \pause A busca ainda precisaria analisar todos os elementos. \pause

Podemos fazer melhor? \pause As operações dependem do conteúdo do item mas não estamos usando o conteúdo para organizar os itens.

</div>
</div>


## Busca eficiente

Como organizar uma coleção de cartas Pokémon de maneira que seja possível encontrar uma carta rapidamente, isso é, sem precisar olhar todas elas? \pause

Se as cartas estiverem em ordem alfabética, pode usar o seguinte método:

- Dividimos o monte mais ou menos no meio e olhamos para a carta que está na metade, se é a carta que estamos procurando, ótimo, terminamos! Senão repetimos o processo para a primeira metade, se a carta que estamos procurando vem antes em ordem alfabética, ou para a segunda metade -- sem a carta que já vimos -- se a carta que estamos procurando vem depois. Se o monte que estamos procurando está vazio, então a carta não está presente.

\pause

Este algoritmo é chamado de **busca binária**.


## Exemplo

Busca pelo 20. `ini` e `fim` são o início do intervalo e `m = (ini + fim) // 2` é o "meio".

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|  6 |  8 | 12 | 14 | 20 | 21 | 22 | 30 | 40 | 41 | 43 | 47 | 50 | 70 |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
   0    1    2    3    4    5    6    7    8    9   10   11   12   13
  ^^                            ^^                                 ^^
 ini                             m                                fim
```


## Exemplo - pesquisa pelo 20

Busca pelo 20. `ini` e `fim` são o início do intervalo e `m = (ini + fim) // 2` é o "meio".

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|  6 |  8 | 12 | 14 | 20 | 21 |    |    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
   0    1    2    3    4    5    6    7    8    9   10   11   12   13
  ^^        ^^             ^^
 ini         m            fim
```


## Exemplo - pesquisa pelo 20

Busca pelo 20. `ini` e `fim` são o início do intervalo e `m = (ini + fim) // 2` é o "meio".

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    | 14 | 20 | 21 |    |    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
   0    1    2    3    4    5    6    7    8    9   10   11   12   13
                 ^^   ^^   ^^
                ini    m  fim
```


## Exemplo - pesquisa pelo 42

Busca pelo 42. `ini` e `fim` são o início do intervalo e `m = (ini + fim) // 2` é o "meio".

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|  6 |  8 | 12 | 14 | 20 | 21 | 22 | 30 | 40 | 41 | 43 | 47 | 50 | 70 |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
   0    1    2    3    4    5    6    7    8    9   10   11   12   13
  ^^                            ^^                                 ^^
 ini                             m                                fim
```


## Exemplo - pesquisa pelo 42

Busca pelo 42. `ini` e `fim` são o início do intervalo e `m = (ini + fim) // 2` é o "meio".

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    | 30 | 40 | 41 | 43 | 47 | 50 | 70 |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
   0    1    2    3    4    5    6    7    8    9   10   11   12   13
                                     ^^             ^^             ^^
                                    ini              m            fim
```


## Exemplo - pesquisa pelo 42

Busca pelo 42. `ini` e `fim` são o início do intervalo e `m = (ini + fim) // 2` é o "meio".

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    | 30 | 40 | 41 |    |    |    |    |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
   0    1    2    3    4    5    6    7    8    9   10   11   12   13
                                     ^^   ^^   ^^
                                    ini    m  fim
```


## Exemplo - pesquisa pelo 42

Busca pelo 42. `ini` e `fim` são o início do intervalo e `m = (ini + fim) // 2` é o "meio".

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    |    |    | 41 |    |    |    |    |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
   0    1    2    3    4    5    6    7    8    9   10   11   12   13
                                               ^^
                                            ini,m,fim
```


## Exemplo - pesquisa pelo 42

Busca pelo 42. `ini` e `fim` são o início do intervalo e `m = (ini + fim) // 2` é o "meio".

```
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|    |    |    |    |    |    |    |    |    |    |    |    |    |    |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
   0    1    2    3    4    5    6    7    8    9   10   11   12   13
                                               ^^   ^^
                                              fim  ini
```


## Complexidade de tempo da busca binária

Quantas comparações no máximo são feitas entre a chave e um valor do arranjo? \pause Quantas divisões sucessivas por 2 são necessárias para que um valor $n$ chegue em 1? \pause

Supondo que $n$ seja uma potência de dois, e sendo $i$ a quantidade de divisões, temos

$$\frac{n}{2^i} = 1 \pause \rightarrow n = 2^i$$

\pause

Aplicando $\log_2$ obtemos

$$\log_2 n = \log_2 2^i \pause \rightarrow i = \lg n$$


## Complexidade de tempo da busca binária

Portanto, a complexidade de tempo da busca binária é $O(\lg n)$. \pause

Como as complexidades de tempo da busca linear e binária se comparam? \pause

| $n$      | Busca Linear     | Busca binária     |
|----------|-----------------:|:-----------------:|
| $10^{1}$ |            $10$  | \pause $\approx 4$|
| $10^{2}$ |           $100$  | \pause $\approx 7$|
| $10^{3}$ |         $1.000$  | \pause$\approx 10$|
| $10^{6}$ |     $1.000.000$  | \pause$\approx 20$|
| $10^{9}$ | $1.000.000.000$  | \pause$\approx 30$|


## Implementação da busca binária

Existem várias formas de implementar a busca binária (veja a lista de exercícios!).

A seguir mostramos um implementação iterativa que devolve um índice onde a chave está na lista ou onde ela deveria estar. Isto é útil pois podemos usar esse índice para inserir a chave se ela não está presente.


## Implementação da busca binária

<div class="columns">
<div class="column" width="55%">
\scriptsize

```python
def busca_binaria(valores: list[int], chave: int) -> int:
    '''
    Se *chave* está presente em *valores*, devolve o
    índice i tal que *valores[i] == chave*. Senão devolve
    o índice i tal que a inserção de *chave* na posição
    *i* de *valores* mantém *valores* em ordem não
    decrescente.

    Requer que *valores* esteja em ordem não decrescente.

    Exemplos
    >>> busca_binaria([6, 8, 10, 12, 20], 7)
    1
    >>> busca_binaria([6, 8, 10, 12, 20], 20)
    4
    '''
```

</div>
<div class="column" width="41%">

\scriptsize

```python
    ini = 0
    fim = len(valores) - 1
    while ini <= fim:
        m = (ini + fim) // 2
        if chave == valores[m]:
            return m
        elif chave < valores[m]:
            fim = m - 1
        else: # chave > valores[m]
            ini = m + 1
    return ini
```
</div>
</div>


## Dicionário - Implementação com arranjo ordenado

O que é preciso para usar a busca binária na implementação do dicionário? \pause

Manter as associações chave-valor ordenadas pela chave (a implementação fica como exercício). \pause

Como isso afeta a complexidade de tempo de `associa` e `remove`? \pause Não afeta! A complexidade continua sendo $O(n)$. \pause

E a complexidade da busca? \pause Passa a ser $O(\lg n)$.


## Dicionário - Avaliação

De forma geral, a implementação usando arranjo ordenado e busca binária de dicionário é adequada? \pause Se a quantidade de consultas for muito maior que a quantidade de alterações, então pode ser uma boa. \pause

E a implementação usando arranjo com busca linear? \pause Pode ser adequada se a quantidade de elementos for pequena. \pause

Podemos melhor o tempo das operações de alteração? \pause Sim! \pause Mas antes precisamos revisar recursividade.


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
```
</div>
</div>


## Árvore

Essa forma de representar uma coleção de valores é chamada de árvore, especificamente, uma árvore binária. \pause

Vire de ponta cabeça para ver a árvore!!! \pause As árvores em computação crescem para baixo! \pause

Como podemos definir uma árvore binária?


## Definição de árvore

Uma **árvore binária** é:

- Vazia (`None`{.python}); ou
- Um nó (`No`{.python}) com um valor e uma **árvore binária** a esquerda e uma **árvore binária** a direita.

\pause

Um nó é a **raiz** da árvore composta por ele e por suas subárvores. \pause

Se $A$ é o nó raiz de uma árvore e $B$ é o nó raiz de uma das subárvores de $A$, então, $B$ é **filho** de $A$ e $A$ é **pai** de $B$. \pause

Um nó $A$ é **ancestral** de um nó $B$ se $A$ é pai de $B$ ou pai de algum ancestral de $B$. Se $A$ é ancestral de $B$, então $B$ é **descendente** de $A$.

## Definição de árvore

<div class="columns">
<div class="column" width="48%">
Como representar uma árvore binária em Python? \pause

\scriptsize

```python
@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore

Arvore = No | None
```

\pause
</div>
<div class="column" width="48%">

Como `Arvore` é um tipo com autorreferência, podemos derivar um modelo de função recursiva para processar uma árvore binária:

\pause

\scriptsize

```python
def fn_para_ab(t: Arvore) -> ...:
    if t is None:
        return ...
    else:
        return t.val ... \
               fn_para_ab(t.esq) ... \
               fn_para_ab(t.dir)
```
</div>
</div>


## Busca em árvore

Note que da mesma forma que não podemos fazer uma busca binária em um arranjo qualquer, também não podemos fazer uma busca binária em uma árvore binária qualquer! É necessário adicionar restrições a árvore que veremos daqui a pouco. \pause

Antes vamos ver alguns exemplos e definições.


## Exemplo de criação de árvore

<div class="columns">
<div class="column" width="43%">
\scriptsize

```python
@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore

Arvore = No | None
```

\normalsize

Escreva o código Python para criar as seguintes árvores:

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
<div class="column" width="55%">
\scriptsize

```python
>>> t1 = No(None, 7, No(None, 1, None))
>>> t1
No(esq=None, val=7, dir=No(esq=None, val=1, dir=None))
```

\pause

```python
>>> t2 = No(No(None, 4, None), 8, t1)
>>> t3 = No(No(None, 5, None), 6, None)
>>> t4 = No(t2, 4, t3)
```

\pause

\normalsize

Como acessar o valor 1 a partir de `t4`?

\pause

\scriptsize

```python
>>> t4.esq.dir.dir.val
```

\pause

\normalsize

Como adicionar uma nova subárvore (valor da raiz 4) a esquerda de `t3` a partir de `t4`? \pause

\scriptsize

```python
>>> t4.dir.dir = No(None, 4, None)
```

\pause

\normalsize

Como remover a subárvore a direita de `t2` a partir de `t4`? \pause

\scriptsize

```python
>>> t4.esq.dir = None
```
</div>
</div>


## Número de folhas

<div class="columns">
<div class="column" width="45%">
O **grau** de um nó é a quantidade de subárvores do nó. \pause

Um nó com grau zero é chamado de **nó folha**. Um nó que não é uma folha é chamado de **nó interno**. \pause

Projete uma função que determine a quantidade de nós folhas de uma árvore.

\pause

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
<div class="column" width="50%">
\scriptsize

```python
def num_folhas(t: Arvore) -> int:
    '''
    Determina a quantidade de folhas em *t*.
    Uma folha é um nó sem nenhum filho.
    >>> # Criação das árvores e alguns exemplos omitidos...
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
        return self.val ... \
               num_folhas(t.esq) ... \
               num_folhas(t.dir)
```

</div>
</div>


## Número de folhas

<div class="columns">
<div class="column" width="45%">
O **grau** de um nó é a quantidade de subárvores do nó.

Um nó com grau zero é chamado de **nó folha**. Um nó que não é uma folha é chamado de **nó interno**.

Projete uma função que determine a quantidade de nós folhas de uma árvore.

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


</div>
<div class="column" width="50%">
\scriptsize

```python
def num_folhas(t: Arvore) -> int:
    '''
    Determina a quantidade de folhas em *t*.
    Uma folha é um nó sem nenhum filho.
    >>> # Criação das árvores e alguns exemplos omitidos...
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
- O **nível** do pai mais 1 caso contrário

\pause

A **altura** (ou profundidade) de um nó é o máximo entre os níveis de todas as folhas da árvore com raiz nesse nó. \pause

De de outra forma, é o comprimento do caminho mais longo deste o nó até uma folha. \pause

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

\normalsize

Em relação a árvore com raiz `t4`, qual é o nível de: \pause

`t4`? \pause 0. \pause
`t2`? \pause 1. \pause
`t3`? \pause 1. \pause
`t1`? \pause 2. \pause
`t0`? \pause 3. \pause

Qual é a altura da árvore: \pause

`t0`? \pause 0. \pause
`t1`? \pause 1. \pause
`t2`? \pause 2. \pause
`t3`? \pause 1. \pause
`t4`? \pause 3.

</div>
</div>


## Nível

<div class="columns">
<div class="column" width="45%">

Projete uma função que encontre todos os valores em um determinado nível de uma árvore.

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
def valores_nivel(t: Arvore, n: int) -> list[int]:
    '''
    Devolve os nós que estão no nível *n* de *t*.
    >>> valores_nivel(None, 0)
    []
    >>> valores_nivel(t4, 0)
    [4]
    >>> valores_nivel(t4, 2)
    [4, 7, 5]
    >>> valores_nivel(t4, 3)
    [1]
    '''
```

\pause

```python
    if t is None:
        return ... n
    else:
        return n ... \
               t.val ... \
               valores_nivel(t.esq, ...) ... \
               valores_nivel(t.dir, ...) ...
```

</div>
</div>


## Nível

<div class="columns">
<div class="column" width="45%">

Projete uma função que encontre todos os valores em um determinado nível de uma árvore.

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

\vspace{0.1cm}

```python
def valores_nivel(t: Arvore, n: int) -> list[int]:
    '''
    Devolve os nós que estão no nível *n* de *t*.
    >>> valores_nivel(None, 0)
    []
    >>> valores_nivel(t4, 0)
    [4]
    >>> valores_nivel(t4, 2)
    [4, 7, 5]
    >>> valores_nivel(t4, 3)
    [1]
    '''
    if t is None:
        return []
    else:
        if n == 0:
            return [t.val]
        else:
            return valores_nivel(t.esq, n - 1) + \
                   valores_nivel(t.dir, n - 1)
```

</div>
</div>


## Árvore binária de busca

O que é preciso para podemos fazer uma busca binária em um árvore binária? \pause Que ela seja de busca! \pause

Uma **árvore binária de busca** (ABB) é uma árvore binária, que quando não é vazia, tem uma raiz $t$ e: \pause

- Todos os elementos da subárvore a esquerda de $t$ são menores que o valor armazenado em $t$; \pause

- Todos os elementos da subárvore a direita de $t$ são maiores que o valor armazenado em $t$; \pause

- As subárvores a esquerda e a direta de $t$ são **árvores binárias de busca**.


## Busca em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

Dessa forma, quando estamos procurando um valor $v$ e $v$ é menor que o valor na raiz, continuamos a busca na subárvore a esquerda, se $v$ é maior que o valor da raiz, continuamos a busca na subárvore a direita. \pause

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
<div class="column" width="48%">
\scriptsize

```python
def busca(t: Arvore, val: int) -> bool:
    r'''
    Devolve True se *val* está em *t*,
    False caso contrário.
    >>> busca(None, 10)
    False
    >>> busca(t, 2)
    True
    >>> busca(t, 6)
    False
    '''
    if t is None:
        return ... val
    else:
        return val ... \
               t.val ... \
               busca(t.esq, val) ... \
               busca(t.dir, val) ...
```

</div>
</div>


## Busca em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

Dessa forma, quando estamos procurando um valor $v$ e $v$ é menor que o valor na raiz, continuamos a busca na subárvore a esquerda, se $v$ é maior que o valor da raiz, continuamos a busca na subárvore a direita.

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
<div class="column" width="48%">
\scriptsize

```python
def busca(t: Arvore, val: int) -> bool:
    r'''
    Devolve True se *val* está em *t*,
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
    elif val == t.val:
        return True
    elif val < t.val:
        return busca(t.esq, val)
    else:  # val > t.val
        return busca(t.dir, val)
```

</div>
</div>


## Busca em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

Dessa forma, quando estamos procurando um valor $v$ e $v$ é menor que o valor na raiz, continuamos a busca na subárvore a esquerda, se $v$ é maior que o valor da raiz, continuamos a busca na subárvore a direita.

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
<div class="column" width="48%">
\scriptsize

```python
def busca(t: Arvore, val: int) -> bool:
    r'''
    Devolve True se *val* está em *t*,
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
        if val == r.val:
            return True
        elif val < r.val:
            r = r.esq
        else:  # val > r.val
            r = r.dir
    return False
```

</div>
</div>


## Complexidade de tempo da busca em ABB

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def busca(t: Arvore, val: int) -> bool:
    if t is None:
        return False
    elif val == t.val:
        return True
    elif val < t.val:
        return busca(t.esq, val)
    else:  # val > t.val
        return busca(t.dir, val)

def busca(t: Arvore, val: int) -> bool:
    r = t
    while r is not None:
        if val == r.val:
            return True
        elif val < r.val:
            r = r.esq
        else:  # val > r.val
            r = r.dir
    return False
```

</div>
<div class="column" width="48%">

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

\normalsize

Qual é a complexidade de tempo do algoritmo de busca em árvore binária de busca? \pause $O(h)$, onde $h$ é a altura da árvore. \pause

Qual é a relação entre a quantidade $n$ de elementos da árvore e $h$? \pause Qual é o limite inferior de $h$? \pause $\lg(n)$. \pause Qual é o limite superior de $h$? \pause $n - 1$.

</div>
</div>


## Complexidade de tempo da busca em ABB

O que podemos concluir sobre isso? \pause Para que a busca em uma ABB seja eficiente, precisamos manter a altura da árvore perto do valor mínimo. \pause

Fato: uma ABB criada com $n$ valores aleatórios tem altura média de $1.39 \lg n$. \pause

Então, se as chaves usadas nas inserções e remoções tem uma distribuição aleatória, a ABB resultante tem uma altura pequena. \pause

Como manter a altura pequena em uma árvore para qualquer distribuição de chaves? \pause Veremos daqui a pouco. \pause

Agora vamos ver como inserir e remover valores de uma ABB sem se preocupar com a altura.


## Inserção em árvore binária de busca

Projete uma função que insira um novo valor, se ainda não estiver presente, em uma árvore binária de busca. \pause

Quais são os tipos dos parâmetros da função? \pause `Arvore`{.python} e `int`{.python}. \pause

Quais deve ser o tipo de saída da função? \pause `None`{.python}? \pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, val: int) -> None:
    '''
    Insere *val* em *t* mantendo as
    propriedades de ABB.
    Requer que *t* seja uma ABB.
    >>> r = None
    >>> insere(r, 10)
    >>> r
    No(esq=None, val=10, dir=None)
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
def insere(t: Arvore, val: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *val* em *t*.
    Se *val* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.

    Exemplo
    >>> r = None
    >>> r = insere(None, 10)
    >>> r
    No(esq=None, val=10, dir=None)
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

\pause

```
7  ins       7   ins       7
   --->    /     --->    /
    4    4        6    4
                        \
                         6
```

\pause

```
    7  ins       7      ins       7
  /    --->    /   \    --->    /   \
4      10    4      10   9    4      10
 \            \                \     /
  6            6                6   9
```

\pause

```
    7      ins       7
  /   \    --->    /   \
4      10  12    4      10
 \     /          \    /  \
  6   9            6  9   12
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, val: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *val* em *t*.
    Se *val* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return ... val
    else:
        val ...
        t.val ...
        insere(t.esq, val) ...
        insere(t.dir, val) ...
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


```
7  ins       7   ins       7
   --->    /     --->    /
    4    4        6    4
                        \
                         6
```


```
    7  ins       7      ins       7
  /    --->    /   \    --->    /   \
4      10    4      10   9    4      10
 \            \                \     /
  6            6                6   9
```


```
    7      ins       7
  /   \    --->    /   \
4      10  12    4      10
 \     /          \    /  \
  6   9            6  9   12
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, val: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *val* em *t*.
    Se *val* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return ... val
    else:
        val ...
        t.val ...
        t.esq = insere(t.esq, val) ...
        t.dir = insere(t.dir, val) ...
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


```
7  ins       7   ins       7
   --->    /     --->    /
    4    4        6    4
                        \
                         6
```


```
    7  ins       7      ins       7
  /    --->    /   \    --->    /   \
4      10    4      10   9    4      10
 \            \                \     /
  6            6                6   9
```


```
    7      ins       7
  /   \    --->    /   \
4      10  12    4      10
 \     /          \    /  \
  6   9            6  9   12
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, val: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *val* em *t*.
    Se *val* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return No(None, val, None)
    else:
        val ...
        t.val ...
        t.esq = insere(t.esq, val) ...
        t.dir = insere(t.dir, val) ...
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


```
7  ins       7   ins       7
   --->    /     --->    /
    4    4        6    4
                        \
                         6
```


```
    7  ins       7      ins       7
  /    --->    /   \    --->    /   \
4      10    4      10   9    4      10
 \            \                \     /
  6            6                6   9
```


```
    7      ins       7
  /   \    --->    /   \
4      10  12    4      10
 \     /          \    /  \
  6   9            6  9   12
```

</div>
<div class="column" width="48%">
\scriptsize

```python
def insere(t: Arvore, val: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado
    da inserção de *val* em *t*.
    Se *val* já está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
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
</div>
</div>


## Remoção em árvore binária de busca

Projete uma função que remova um valor, se estiver presente, de uma árvore binária de busca.

\pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def remove(t: Arvore, val: int) -> Arvore:
    '''
    Devolve a raiz da ABB que é o resultado
    da remoção de *val* de *t*.
    Se *val* não está em *t*, devolve *t*.
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

Mas temos lembrar que quando chamamos `remove` é preciso armazenar o resultado no lugar da raiz que foi chamada como parâmetro.

</div>
</div>


## Remoção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: \pause retorna `None`{.python}. \pause

\small

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
def remove(t: Arvore, val: int) -> Arvore:
    '''
    Devolve a raiz da ABB que é o resultado
    da remoção de *val* de *t*.
    Se *val* não está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return ... val
    else:
        val ...
        t.val ...
        remove(t.esq, val) ...
        remove(t.dir, val) ...
        return ...
```
</div>
</div>


## Remoção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: retorna `None`{.python}.

\small

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
def remove(t: Arvore, val: int) -> Arvore:
    '''
    Devolve a raiz da ABB que é o resultado
    da remoção de *val* de *t*.
    Se *val* não está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return None
    else:
        val ...
        t.val ...
        t.esq = remove(t.esq, val) ...
        t.dir = remove(t.dir, val) ...
        return ...
```
</div>
</div>


## Remoção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: retorna `None`{.python}.

\small

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
def remove(t: Arvore, val: int) -> Arvore:
    '''
    Devolve a raiz da ABB que é o resultado
    da remoção de *val* de *t*.
    Se *val* não está em *t*, devolve *t*.
    Requer que *t* seja uma ABB.
    '''
    if t is None:
        return None
    elif val < t.val:
        t.esq = remove(t.esq, val)
        return t
    elif val > t.val:
        t.dir = remove(t.dir, val)
        return t
    else: # val == t.val
        val, t.val, t.esq, t.dir
        ... = remove(t.esq, ...) ...
        ... = remove(t.dir, ...) ...
        return ...
```
</div>
</div>


## Remoção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: retorna `None`{.python}.

\small

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
def remove(t: Arvore, val: int) -> Arvore:
    if t is None:
        return None
    elif val < t.val:
        t.esq = remove(t.esq, val)
        return t
    elif val > t.val:
        t.dir = remove(t.dir, val)
        return t
    else: # val == t.val
        if t.esq is None:
            return t.dir
        elif t.dir is None:
            return t.esq
        else:
            val, t.val, t.esq, t.dir ...
            ... = remove(t.esq, ...) ...
            ... = remove(t.dir, ...) ...
            return ...
```
</div>
</div>


## Remoção em árvore binária de busca

<div class="columns">
<div class="column" width="48%">

\small

Remoção de folha: retorna `None`{.python}.

\small

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
def remove(t: Arvore, val: int) -> Arvore:
    if t is None:
        return None
    elif val < t.val:
        t.esq = remove(t.esq, val)
        return t
    elif val > t.val:
        t.dir = remove(t.dir, val)
        return t
    else: # val == t.val
        if t.esq is None:
            return t.dir
        elif t.dir is None:
            return t.esq
        else:
            m = maximo(t.esq)
            t.val = m
            t.esq = remove(t.esq, m)
            return t
```
</div>
</div>


## Referências

Capítulo 10 - Árvores - Fundamentos de Python: Estruturas de dados. Kenneth A. Lambert. (Disponível na Minha Biblioteca na UEM).

Capítulo 12 - Árvores Binárias de Busca - Algoritmos: Teoria e Prática, 3a. edição, Cormen, T. at all.

Capítulo 6 - Binary Trees - [Open Data Structures](https://opendatastructures.org/ods-python.pdf).
