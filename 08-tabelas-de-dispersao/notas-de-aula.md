---
# vim: set spell spelllang=pt_br:
title: Tabelas de dispersão
linkcolor: Black
urlcolor: Blue
---

## Introdução

Vimos que algumas vezes informações sobre características da entrada nos permitem desenvolver algoritmos e estrutura de dados mais eficientes. \pause Por exemplo: \pause

- Se um arranjo está ordenado, então podemos fazer uma busca binária ao invés de uma busca linear; \pause

- Se as chaves para inserção em uma ABB são uniformemente distribuídas, então a altura da árvore será pequena e as operações serão eficientes.


## Introdução

Além disso, quando a entrada não tem aquelas características, ainda podemos tomar algumas providências: \pause

- Modificar a entrada, como por exemplo, ordenar os valores para fazer a busca binária; \pause

- Fazer o rebalanceamento em ABB, se as chaves não são uniformemente distribuídas, para manter a altura da árvore pequena.


## Desafio

Vimos que podemos implementar as operações de busca, inserção e remoção do TAD Dicionario usando árvores AVL com tempo $O(\lg n)$. \pause Será que podemos fazer melhor se soubermos algo sobre as entradas (chaves)? \pause

Na definição do TAD as chaves eram strings, e se as chaves fossem inteiros? \pause

E se as chaves estivem em um intervalo específico, com entre 0 e 10.000? \pause

Como tirar proveito desse conhecimento sobre as chaves para fazer uma implementação eficiente?


## Endereçamento direto

Podemos criar um arranjo com uma posição para cada possível chave da entrada, armazenamos na posição o valor associada com a chave, se houver um, ou `None`{.python} caso contrário. \pause

Essa estratégia é chamada de **endereçamento direto**. \pause

De forma geral, para chaves no intervalo de $0$ a $M - 1$, alocamos um arranjo com $M$ posições.


## Endereçamento direto

![](imagens/Fig-11-1.pdf){width=9cm}


## Endereçamento direto

<div class="columns">
<div class="column" width="48%">
\small

Implemente um dicionário que associa número naturais a strings usando endereçamento direto.

\pause

\scriptsize

```python
# As restrições (assert) sobre as
# chaves foram omitidas.
class Dicionario:
    valores: list[str | None]

    def __init__(self, m: int) -> None:
        assert 0 <= m
        self.valores = [None] * m

    def get(self, chave: int) -> str | None:
        return self.valores[chave]

    def associa(self, chave: int, valor: str):
        self.valores[chave] = valor

    def remove(self, chave: int):
        self.valores[chave] = None
```

\pause

</div>
<div class="column" width="48%">
Qual é a complexidade de tempo das operações de dicionário usando endereçamento direto? \pause $O(1)$.
</div>
</div>


## Endereçamento direto

Quais as desvantagens/limitações dessa estratégia? \pause

- Se a quantidade de chaves é muito menor que $M$, então existe um desperdício muito grande de memória. \pause Além disso, a quantidade de memória disponível pode não ser suficiente. \pause

- As chaves precisam ser maiores que $0$. \pause

- As chaves são restritas a inteiros. \pause

Vamos isolar e tentar lidar com cada uma dessas questões.


## Intervalos quaisquer

<div class="columns">
<div class="column" width="48%">

O que podemos fazer se as chaves puderem estar em um intervalo de $[A, B)$ qualquer? \pause

Podemos _mapear_ cada chave para um valor distinto no intervalo  $[0, B - A)$:

$A \rightarrow 0, (A + 1) \rightarrow 1, \dots, (B - 1) \rightarrow (B - A - 1)$.

\pause

Dessa forma podemos usar o resultado do mapeamento da chave como índice em um arranjo de tamanho $B - A$. \pause

Projete uma função que faça o mapeamento de uma chave usando esse esquema.

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def mapeia(chave: int, A: int, B: int) -> int:
    '''
    Mapeia uma chave no intervalo de
    *A* a *B* para um índice de um arranjo
    com *(B - A)* elementos.
    Requer que A <= chave < B.

    Exemplos
    >>> mapeia(-5, -5, 20)
    0
    >>> mapeia(19, -5, 20)
    24
    >>> mapeia(6, -5, 20)
    11
    '''
```

\pause

```python
    assert A <= chave < B
    return chave - A
```

</div>
</div>



## Quantidade de chaves menor que o tamanho do intervalo

O que fazer quando a quantidade de chaves armazenadas $n$ é muito menor que a quantidade de chaves possíveis $U$? \pause

Usar um arranjo de tamanho $m = O(n)$ e _mapear_ as chaves para índices no intervalo de $[0, m)$ (índice válido para o arranjo).


## Quantidade de chaves menor que o tamanho do intervalo

Como mapear uma chave no intervalo de $[0, U)$ para posições no intervalo $[0, m)$? \pause

Algumas opções (sendo $k$ uma chave): \pause

- Por divisão (resto): $k \mod m$ \pause

- Por multiplicação: $\left \lfloor m \times (k \times A \mod 1) \right \rfloor$, onde $A > 1$ é um valor real -- note que $k \times A \mod 1 < 1$.


## Quantidade de chaves menor que o tamanho do intervalo

Mapeie as chaves 734, 141, 8, 230, 554, 650 usando o esquema de divisão com $m = 20$. \pause

$734 \rightarrow 14$, \pause $141 \rightarrow 1$ \pause, $8 \rightarrow 8$, \pause $230 \rightarrow 10$, \pause $554 \rightarrow 14$, \pause $650 \rightarrow 10$. \pause

Considerando que o resultado do mapeamento de uma chave é uma posição em um arranjo (onde o valor associado com a chave será armazenado), qual o problema que temos? \pause Colisões! \pause

Uma **colisão** ocorre quando duas chaves são mapeadas para a mesma posição do arranjo.


## Colisões

Podemos evitar as colisões? \pause Sem conhecer as chaves, não. \pause

Podemos lidar com as colisões? \pause Sim, de algumas maneiras que vamos ver depois. \pause

Considerando o mapeamento por divisão, qual a característica das chaves para que as colisões sejam mais raras? \pause Elas devem estar uniformemente distribuídas. \pause

E para que as colisões sejam frequentes? \pause Que tenham o mesmo resto quando divididas por $m$.


## Chaves que não são inteiros

O que fazer quando as chaves não são inteiros? \pause

_Mapear_ as chaves para valores inteiros e depois para posições. (Ou diretamente para posições) \pause

Como mapear uma string para um inteiro?


## Chaves que não são inteiros

Cada elemento em uma posição de uma string é internamente representado por um número (_code point_), esse número pode ser obtido com a função `ord`{.python}. \pause

Então, podemos, por exemplo, mapear uma string para o _code point_ do seu primeiro caractere, ou zero se a string for vazia. \pause Ou ainda, somar todos os _code point_ de todos os caracteres. \pause

Qual o problema dessas formas de mapeamento? \pause Geram muitas colisões! \pause

Mas não vamos nos preocupar com isso, porque enquanto, basta sabermos que é possível mapear _qualquer_ tipo de valor para um número inteiro.


## Revisão

Vimos que, se as chaves são inteiros em um intervalo de 0 a $M - 1$, então podemos implementar um dicionário usando endereçamento direto, onde as operações de busca, inserção e remoção tem complexidade de tempo de $O(1)$. \pause

Vimos as limitações do endereçamento direto e discutimos estratégias de como superá-las. \pause O quê essas estratégias tinham em comum? \pause

- O mapeamento da chave para uma posição de um arranjo com tamanho conhecido

\pause

Em outras palavras, a estratégia é a mesma!


## Tabelas de dispersão

Chamamos a função que mapeia a chaves para posições de um arranjo de **função de dispersão** ou **função _hash_**. \pause

Uma **tabela de dispersão** ou **tabela _hash_** é uma estrutura de dados que usa uma função de dispersão para calcular índices em um arranjo que fornece uma forma de armazenar pares de chave-valor.

\pause

Existem dois desafios no projeto e implementação de uma tabela de dispersão: \pause

- A função de dispersão \pause

- O tratamento de colisões


## Função de dispersão

Criar uma boa função de dispersão, isto é, uma função que gere poucas colisões, requer conhecimentos avançados de probabilidade e estatística, por isso não vamos tratar desse assunto. \pause

Como função de dispersão, vamos combinar a função `hash`{.python}, pré-defina em Python, com o resto da divisão. \pause Para uma chave $k$, vamos representar o resultado da função de dispersão por $h(k)$. \pause

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
>>> hash('casa')
-3155579165809741514
>>> hash('arroz')
-5974344979373615551
>>> hash(7)
7
>>> hash(-17)
-17
>>> hash(2 ** 100)
549755813888
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
>>> hash('casa') % 20
6
>>> hash('arroz') % 20
9
>>> hash(7) % 20
7
>>> hash(-17) % 20
3
>>> hash(2 ** 100) % 20
8
```
</div>
</div>


## Colisão

Considere os pares de chave-valor: \footnotesize `(734, 'maça')`{.python}, `(141, 'mamão')`{.python}, `(84, 'banana')`{.python}, `(236, 'goiaba')`{.python}, `(554, 'ameixa')`{.python}, `(1, 'laranja')`{.python}. \pause

\normalsize

Considerando um tabela (arranjo) de 10 posições, calcule $h(k)$ para cada chave $k$ listada anteriormente. \pause

Proponha uma forma de lidar com as colisões, isto é, uma maneira de armazenar, busca, inserir e remover os pares chave-valor na tabela.


## Encadeamento

Podemos armazenar todas os pares chave-valor cuja a chave gerou o mesmo índice em um coleção: \pause

- Arranjo dinâmico \pause
- Lista encadeada \pause
- Árvore AVL \pause
- Outra tabela de dispersão!

\pause

Quanto usamos listas encadeadas, chamamos a estratégia **encadeamento**.


## Encadeamento

<div class="columns">
<div class="column" width="40%">
\scriptsize

```
(734, 'maça') -> 4

(141, 'mamão') -> 1

(84, 'banana') -> 4

(236, 'goiaba') -> 6

(554, 'ameixa') -> 4

(1, 'laranja') -> 1
```

\pause

</div>
<div class="column" width="60%">

\scriptsize

\vspace{-0.1cm}

```
  +---+
0 |   |
  +---+   +-----------+   +-----------+
1 |   |-->| 141 mamão |-->| 1 laranja |
  +---+   +-----------+   +-----------+
2 |   |
  +---+
3 |   |
  +---+   +-----------+   +-----------+   +-----------+
4 |   |-->| 734  maça |-->| 84 banana |-->| 554 ameixa|
  +---+   +-----------+   +-----------+   +-----------+
5 |   |
  +---+   +-----------+
6 |   |-->| 236 goiaba|
  +---+   +-----------+
7 |   |
  +---+
8 |   |
  +---+
9 |   |
  +---+
```

</div>
</div>


## Encadeamento

<div class="columns">
<div class="column" width="48%">

Como definir os tipos para implementar um dicionario usando uma tabela de dispersão com encadeamento? \pause

\scriptsize

```python
@dataclass
class No:
    chave: str
    valor: int
    prox: No | None
```

\pause

```python
class Dicionario:
    tabela: list[No | None]
    num_itens: int
```

\pause

</div>
<div class="column" width="48%">
Como implementar `get`?

\pause

\scriptsize

```python
def get(self, chave: str) -> int | None:
    # procurar por chave em self.tabela[h(chave)]
```

\pause

\normalsize

Como implementar `assoc`?

\pause

\scriptsize

```python
def assoc(self, chave: str, valor: int):
    # inserir (chave, valor) em self.tabela[h(chave)]
    # ou atualizar o valor associado com a chave
```

\pause

\normalsize

Como implementar `remove`?

\pause

\scriptsize

```python
def remove(self, chave: str):
    # remover (chave, valor) de self.tabela[h(chave)]
```

</div>
</div>

\pause

Qual é a complexidade de tempo de `get`, `assoc` e `remove`? \pause Depende da quantidade de itens no encadeamento...


## Fator de carga

Para discutirmos a complexidade de tempo, precisamos de uma definição. \pause

Chamado de **fator de carga** $\alpha$ de uma tabela de dispersão $T$ o $n / m$, onde $n$ é a quantidade de posições na tabela e $m$ é a quantidade de elementos armazenados.


## Referências

Capítulo 11 - Seção Estratégias de hashing - Fundamentos de Python: Estruturas de dados. Kenneth A. Lambert. (Disponível na Minha Biblioteca na UEM).

Capítulo 11 - Tabelas de Dispersão - Algoritmos: Teoria e Prática, 3a. edição, Cormen, T. at all.

Capítulo 5 - Hash Tables - [Open Data Structures](https://opendatastructures.org/ods-python.pdf).

Funções [`hash`](https://docs.python.org/3/library/functions.html#hash) e [`object.__hash__`](https://docs.python.org/3/reference/datamodel.html#object.__hash__) do Python.
