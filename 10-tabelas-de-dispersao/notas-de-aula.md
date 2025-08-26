---
# vim: set spell spelllang=pt_br:
title: Tabelas de dispersão
linkcolor: Black
urlcolor: Blue
---

## Introdução

Vimos que algumas vezes informações sobre características da entrada nos permitem desenvolver algoritmos e estruturas de dados mais eficientes. \pause Por exemplo: \pause

- Se um arranjo está ordenado, então podemos fazer uma busca binária em vez de uma busca linear; \pause

- Se as chaves para inserção em uma ABB são uniformemente distribuídas, então a altura da árvore será pequena e as operações serão eficientes.


## Introdução

Além disso, quando a entrada não tem essas características, ainda podemos tomar algumas providências: \pause

- Modificar a entrada, como por exemplo, ordenar os valores para fazer a busca binária; \pause

- Fazer o rebalanceamento em ABB, se as chaves não são uniformemente distribuídas, para manter a altura da árvore pequena.


## Desafio

Vimos que podemos implementar as operações de busca, inserção e remoção do TAD Dicionário usando árvores AVL com tempo $O(\lg n)$. \pause Será que podemos fazer melhor se soubermos algo sobre as entradas (chaves)? \pause

Na definição do TAD as chaves eram strings, e se as chaves fossem inteiros? \pause

E se as chaves estiverem em um intervalo específico, entre 0 e 10.000? \pause

Como tirar proveito desse conhecimento sobre as chaves para fazer uma implementação eficiente?


## Endereçamento direto

Podemos criar um arranjo com uma posição para cada possível chave da entrada, armazenamos na posição o valor associado à chave, se houver tal valor, ou `None`{.python} caso contrário. \pause

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

    def busca(self, chave: int) -> str | None:
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

Quais são as desvantagens/limitações dessa estratégia? \pause

- Se a quantidade de chaves é muito menor que $M$, então existe um desperdício muito grande de memória. \pause Além disso, a quantidade de memória disponível pode não ser suficiente. \pause

- As chaves precisam ser maiores que $0$. \pause

- As chaves são restritas a inteiros. \pause

Vamos isolar e tentar lidar com cada uma dessas questões separadamente.


## Intervalos quaisquer

<div class="columns">
<div class="column" width="48%">

O que podemos fazer se as chaves estão em um intervalo $[A, B)$ qualquer? \pause

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

Considerando que o resultado do mapeamento de uma chave é uma posição em um arranjo (onde o valor associado com a chave será armazenado), qual é o problema que temos? \pause Colisões! \pause

Uma **colisão** ocorre quando duas chaves são mapeadas para a mesma posição do arranjo.


## Colisões

Podemos evitar as colisões? \pause Sem conhecer as chaves, não. \pause

Podemos lidar com as colisões? \pause Sim, de algumas maneiras que vamos ver depois. \pause

Considerando o mapeamento por divisão, qual é a característica das chaves para que as colisões sejam mais raras? \pause Elas devem estar uniformemente distribuídas. \pause

E para que as colisões sejam frequentes? \pause Que tenham o mesmo resto quando divididas por $m$.


## Chaves que não são inteiros

O que fazer quando as chaves não são inteiros? \pause

_Mapear_ as chaves para valores inteiros e depois para posições. (Ou diretamente para posições) \pause

Como mapear uma string para um inteiro?


## Chaves que não são inteiros

Cada elemento em uma posição de uma string é internamente representado por um número (_code point_), esse número pode ser obtido com a função `ord`{.python}. \pause

<div class="columns">
<div class="column" width="25%">
\scriptsize

```python
>>> ord('a')
97
```
</div>
<div class="column" width="25%">
\scriptsize

```python
>>> ord('z')
122
```
</div>
<div class="column" width="25%">
\scriptsize

```python
>>> ord('7')
55
```
</div>
<div class="column" width="25%">
\scriptsize

```python
>>> ord('%')
37
```
</div>
</div>

\pause

Então, podemos, por exemplo, mapear uma string para o _code point_ do seu primeiro caractere, ou zero se a string for vazia. \pause Ou ainda, somar todos os _code point_ de todos os caracteres. \pause

Qual o problema dessas formas de mapeamento? \pause Geram muitas colisões! \pause

Mas não vamos nos preocupar com isso por enquanto, basta sabermos que é possível mapear _qualquer_ tipo de valor para um número inteiro.


## Revisão

Vimos que, se as chaves são inteiros em um intervalo de 0 a $M - 1$, então podemos implementar um dicionário usando endereçamento direto, onde as operações de busca, inserção e remoção tem complexidade de tempo de $O(1)$. \pause

Vimos as limitações do endereçamento direto e discutimos estratégias de como superá-las. \pause O que essas estratégias tinham em comum? \pause

- O mapeamento da chave para uma posição de um arranjo com tamanho conhecido

\pause

Em outras palavras, a estratégia é a mesma!


## Tabelas de dispersão

Chamamos a função que mapeia as chaves para posições de um arranjo de **função de dispersão** ou **função hash**. \pause

Uma **tabela de dispersão** ou **tabela hash** é uma estrutura de dados que usa uma função de dispersão para calcular índices em um arranjo que fornece uma forma de armazenar pares de chave-valor.

\pause

Existem dois desafios no projeto e implementação de uma tabela de dispersão: \pause

- A função de dispersão \pause

- O tratamento de colisões


## Função de dispersão

Criar uma boa função de dispersão, isto é, uma função que gere poucas colisões, requer conhecimentos avançados de probabilidade e estatística, por isso não vamos tratar desse assunto. \pause

Como função de dispersão, vamos combinar a função `hash`{.python}, pré-definida em Python, com o resto da divisão. \pause Para uma chave $k$, vamos representar o resultado da função de dispersão por $h(k)$. \pause

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

Considerando um tabela (arranjo) de $m = 10$ posições, calcule $h(k) = k \mod m$ para cada chave $k$ listada anteriormente. \pause

Proponha uma forma de lidar com as colisões, isto é, uma maneira de armazenar, buscar, inserir e remover os pares chave-valor na tabela.


## Encadeamento separado

Podemos armazenar todos os pares chave-valor cuja chave gerou o mesmo índice em um coleção: \pause

- Arranjo dinâmico \pause
- Lista encadeada \pause
- Árvore AVL \pause
- Outra tabela de dispersão! 

\pause

Quando usamos uma lista encadeada em cada posição, chamamos a estratégia **encadeamento separado**.


## Encadeamento separado

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


## Encadeamento separado

<div class="columns">
<div class="column" width="45%">

Como definir os tipos para implementar um dicionário usando uma tabela de dispersão com encadeamento? \pause

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
<div class="column" width="52%">
Como implementar o método `busca`?

\pause

\scriptsize

```python
def busca(self, chave: str) -> int | None:
    # procurar por chave em self.tabela[h(chave)]
```

\pause

\normalsize

Como implementar `associa`?

\pause

\scriptsize

```python
def associa(self, chave: str, valor: int):
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

\ \

\pause

\normalsize


Qual é a complexidade de tempo de `busca`, `associa` e `remove`? \pause Depende da quantidade de itens no encadeamento...

</div>
</div>


## Fator de carga e complexidade de tempo

Para discutirmos a complexidade de tempo, precisamos de uma definição. \pause

Chamamos de **fator de carga** $\alpha$ de uma tabela de dispersão $T$ o valor $n / m$, onde $m$ é a quantidade de posições na tabela e $n$ é a quantidade de elementos em $T$. \pause

Qual é o pior caso para as operações? \pause Todos os $n$ elementos estão na mesma posição da tabela. \pause Nesse caso, o tempo das operações é $O(n)$. \pause

E o caso médio? \pause Qual é o tamanho médio de cada lista encadeada? \pause $n / m = \alpha$ \pause, ou seja, no caso médio, o tempo das operações é $O(1 + \alpha)$. \pause

Se mantivermos $n = O(m)$, então $\alpha = n / m = O(m) / m = O(1)$, e o tempo médio das operações fica $O(1)$.


## Redispersão

Para manter o tempo médio em $O(1)$, temos que manter um fator de carga pequeno. \pause Mas não muito pequeno para não desperdiçar memória. \pause

Sedgewick recomenda um valor entre 5 e 10. \pause

Então, quando $\alpha$ fica maior que 10, temos que alocar uma tabela _maior_ e fazer a redispersão das chaves. \pause

Quando $\alpha$ fica menor que 5, temos que alocar uma tabela _menor_ e fazer a redispersão das chaves.


## Endereçamento aberto

**Endereçamento aberto** é uma técnica de resolução de colisão baseado em **sondagem**. \pause

Nessa técnica, todos os pares chave-valor são armazenados na própria tabela. \pause

Quando um novo par chave-valor precisa ser inserido na tabela e a posição já está ocupada, outras posições são sondadas até que uma posição livre seja encontra. \pause

A busca e a remoção devem usar o mesmo processo de sondagem.


## Sondagem linear

A forma mais simples de sondagem é a linear. Nesse esquema, quando há colisão na posição $i$, as posições são testadas na ordem $(i + j) \mod m$ para $j = 1, 2, \dots, ... m$. \pause

A sondagem para quando uma posição que nunca foi ocupada é encontrada. \pause

Veremos que para esse esquema funcionar, a remoção deve marcar a posição de forma especial.


## Sondagem linear - inserção

Mostre passo a passo a inserção das chaves 734, 84, 236, 554, 141 em uma tabela com $m = 8$. \pause

<div class="columns">
<div class="column" width="22%">

\uncover<2->{$734 \rightarrow 6$}

\uncover<3->{$84 \rightarrow 4$}

\uncover<4->{$236 \rightarrow 4, 5$}

\uncover<5->{$554 \rightarrow 2$}

\uncover<6->{$31 \rightarrow 7$}

\uncover<7->{$141 \rightarrow 5, 6, 7, 0$}

\pause

</div>
<div class="column" width="13%">

\scriptsize

```
  +---+
0 |   |
  +---+
1 |   |
  +---+
2 |   |
  +---+
3 |   |
  +---+
4 |   |
  +---+
5 |   |
  +---+
6 |734|
  +---+
7 |   |
  +---+
```
\pause
</div>
<div class="column" width="13%">

\scriptsize

```
  +---+
0 |   |
  +---+
1 |   |
  +---+
2 |   |
  +---+
3 |   |
  +---+
4 |84 |
  +---+
5 |   |
  +---+
6 |734|
  +---+
7 |   |
  +---+
```

\pause
</div>
<div class="column" width="13%">

\scriptsize

```
  +---+
0 |   |
  +---+
1 |   |
  +---+
2 |   |
  +---+
3 |   |
  +---+
4 |84 |
  +---+
5 |236|
  +---+
6 |734|
  +---+
7 |   |
  +---+
```

\pause
</div>
<div class="column" width="13%">

\scriptsize

```
  +---+
0 |   |
  +---+
1 |   |
  +---+
2 |554|
  +---+
3 |   |
  +---+
4 |84 |
  +---+
5 |236|
  +---+
6 |734|
  +---+
7 |   |
  +---+
```

\pause
</div>
<div class="column" width="13%">

\scriptsize

```
  +---+
0 |   |
  +---+
1 |   |
  +---+
2 |554|
  +---+
3 |   |
  +---+
4 |84 |
  +---+
5 |236|
  +---+
6 |734|
  +---+
7 |31 |
  +---+
```

\pause
</div>
<div class="column" width="13%">

\scriptsize

```
  +---+
0 |141|
  +---+
1 |   |
  +---+
2 |554|
  +---+
3 |   |
  +---+
4 |84 |
  +---+
5 |236|
  +---+
6 |734|
  +---+
7 |31 |
  +---+
```

</div>
</div>


## Sondagem linear - remoção e busca

Mostre passo a passo para a remoção da chave 236, e a busca das chaves 742 e 141?.

<div class="columns">
<div class="column" width="15%">
\scriptsize

```
  +---+
0 |141|
  +---+
1 |   |
  +---+
2 |554|
  +---+
3 |   |
  +---+
4 |84 |
  +---+
5 |236|
  +---+
6 |734|
  +---+
7 |31 |
  +---+
```

\pause
</div>
<div class="column" width="22%">
Remoção do $236 \rightarrow 4, 5$.

A posição de remoção deve ser marcada de forma especial.

\pause
</div>
<div class="column" width="3%">
</div>
<div class="column" width="15%">
\scriptsize

```
  +---+
0 |141|
  +---+
1 |   |
  +---+
2 |554|
  +---+
3 |   |
  +---+
4 |84 |
  +---+
5 | \ |
  +---+
6 |734|
  +---+
7 |31 |
  +---+
```

\pause
</div>
<div class="column" width="22%">

Busca do $742 \rightarrow 6, 7, 0, 1$. \pause

Não encontrado. \pause

</div>
<div class="column" width="22%">

Busca do $141 \rightarrow 5, 6, 7, 0$. \pause

Encontrado.

</div>
</div>


## Sondagem linear

<div class="columns">
<div class="column" width="48%">
Defina os tipos de dados para um dicionário implementado usando tabelas de dispersão com sondagem.

\pause

\scriptsize

```python

@dataclass
class Removido:
    pass

@dataclass
class Presente:
    chave: str
    valor: int

class Dicionario:
    tabela: list[None | Removido | Presente]
    # Qtd de itens Presente na tabela.
    num_itens: int
    # Qtd de itens Removido na tabela.
    num_removidos: int
```

\pause

</div>
<div class="column" width="48%">
Implemente o método `Dicionario.busca`. \pause

\scriptsize

```python

def busca(self, chave: str) -> None | int:
    p = hash(chave) % len(self.tabela)
    while self.tabela[p] is not None:
        if isinstance(self.tabela[p], Presente):
            if self.tabela[p].chave == chave:
                return self.tabela[p].valor
        p = (p + 1) % len(self.tabela)
    return None
```

\ \

\pause

\normalsize

Note que para a busca parar no caso em que a chave não é encontrada é preciso que exista pelo menos uma posição com `None`{.python}, ou seja, a quantidade de itens presentes mais os removidos deve ser menor que o tamanho da tabela.

</div>
</div>


## Sondagem linear

Qual é o tempo de execução das operações de busca, inserção e remoção? \pause

No pior caso, $O(n)$. \pause

Mas se o fator de carga for mantido menor do que $0.7$, a complexidade de tempo no caso médio é $O(1)$.


## Referências

Capítulo 11 - Seção Estratégias de hashing - Fundamentos de Python: Estruturas de dados. Kenneth A. Lambert. (Disponível na Minha Biblioteca na UEM).

Capítulo 11 - Tabelas de Dispersão - Algoritmos: Teoria e Prática, 3a. edição, Cormen, T. et al.

Capítulo 5 - Hash Tables - [Open Data Structures](https://opendatastructures.org/ods-python.pdf).

Funções [`hash`](https://docs.python.org/3/library/functions.html#hash) e [`object.__hash__`](https://docs.python.org/3/reference/datamodel.html#object.__hash__) do Python.
