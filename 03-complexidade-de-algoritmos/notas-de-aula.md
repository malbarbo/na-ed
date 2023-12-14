---
# vim: set spell spelllang=pt_br:
title: Complexidade de algoritmos
linkcolor: Black
urlcolor: Blue
---


## Introdução

Quando fazemos o projeto de uma função ou de um tipo de dado separamos a especificação (o que) da implementação (como). \pause

Isso trás diversos benefícios, entre eles: \pause

- Oculta a complexidade da implementação (abstração) \pause

- Permite o desenvolvimento independente \pause

- Permite múltiplas implementações


## Complexidade de algoritmos

Se podemos fazer a implementação de diversas maneirais, quais critérios podemos utilizar para escolher uma implementação? \pause

- Simplicidade \pause

- Consumo de recurso (tempo, memória, energia, etc)

\pause

Formalmente, o consumo de recurso de um algoritmo é chamada de **complexidade do algoritmo**.


## Análise de algoritmos

Para podermos determinar qual implementação (algoritmo) é mais eficiente (tem menor complexidade), precisamos de: \pause

- Uma forma de determinar expressar a complexidade (consumo de recurso) \pause

- Uma forma de comparar a complexidade \pause

O processo de determinar a complexidade de algoritmos é chamado de **análise de algoritmos**.


## Formas de análise

A análise de um algoritmo pode ser: \pause

- Experimental \pause

- Teórica \pause

A análise experimental é mais específica pois dependente da linguagem, do compilador / interpretador, do hardware, etc. \pause

A análise teórica é mais geral e provê entendimento das propriedades e limitações inerentes ao algoritmo. \pause

A duas forma de análise são complementares.


## Crescimento assintótico

Usualmente a complexidade de um algoritmo é expressa através de uma função que relaciona o tamanho da entrada com o consumo do recurso. \pause

Em geral, na análise teórica, não estamos procurando a função precisa de complexidade, mas uma que descreve de forma razoável como o consumo do recurso cresce em relação ao crescimento do tamanho da entrada (ordem de crescimento). \pause

Além disso, estamos interessados em entradas suficientemente grandes, para que o algoritmo demore algum tempo para executar e não termine rapidamente.


## Crescimento assintótico

Quando olhamos para entradas suficientemente grandes e consideramos relevante apenas a ordem de crescimento, estamos estudando a **eficiência assintótica** do algoritmo em relação ao uso de algum recurso. \pause

Dessa forma, um algoritmo assintoticamente mais eficiente será a melhor escolha, exceto para entradas muito pequenas.


## Exemplo máximo

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def maximo(lst: list[int]) -> int:
    '''
    Encontra o valor máximo
    de *lst*.

    Requer que *lst* seja não vazia.

    Exemplos
    >>> maximo([4, 1, 6, 2])
    6
    '''
    assert len(lst) != 0
    m = lst[0]
    for x in range(1, len(lst)):
        if m < x:
            m = x
    return m
```
</div>
<div class="column" width="50%">
Como a quantidade de elementos de `lst` ($n$ - tamanho da entrada) está relacionada com o tempo de execução (complexidade de tempo) da função `maximo`? \pause

Quantas vezes a operação `<` é executada? \pause $n - 1$. \pause

Dessa forma, podemos dizer que o tempo de execução da função `maximo`, $T(n)$, tem a mesma ordem de crescimento de $n - 1$.
</div>
</div>


## Entrada específica

O tempo de execução de um algoritmo pode depender não apenas do tamanho da entrada, mas do valor específico da entrada. Em outras palavras, para um mesmo tamanho de entrada, o tempo de execução pode mudar de acordo com a entrada.


## Exemplo contem

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def contem(lst: list[int], n: int) -> Bool:
    '''
    Devolve True se *n* está em *lst*,
    False caso contrário.

    Exemplos
    >>> contem([4, 1, 2, 3], 1)
    True
    >>> contem([4, 1, 2, 3], 6)
    False
    '''
    contem = False
    i = 0
    while i < len(lst) and not contem:
        if lst[i] == n:
            contem = True
        i = i + 1
    return contem
```
</div>
<div class="column" width="50%">
Para uma entrada de tamanho $n$, quantas vezes a operação `==` é executada? \pause

Depende da entrada! \pause

- Melhor caso \pause

- Pior caso \pause

- Caso médio \pause

</div>
</div>


## Notação $O$ -- $O$ grande -- _Big-oh_

Para uma função $g(n)$, denotamos por $O(g(n))$ o conjunto de funções:

$O(g(n)) = \{f(n)$: existem constantes positivas $c$ e $n_0$ tal que $0 \le f(n) \le c g(n)$ para todo $n \ge n_0\}$

\includegraphics[trim=37cm 3cm 37cm 0pt,clip, width=4.5cm]{imagens/Fig-3-1.pdf}

\pause

\center $\displaystyle f(n) \in O(g(n)) \iff \lim_{n \to \infty}\frac{f(n)}{g(n)} = L, \pause 0 \leq L < \infty.$


## Notação $O$ -- $O$ grande -- _Big-oh_

A notação $O$ descreve um **limite assintótico superior** para uma função

- Escrevemos $f(n) = O(g(n))$ para indicar que $f(n) \in O(g(n))$

- Informalmente, dizemos que $f(n)$ cresce no máximo tão rapidamente quanto $g(n)$.


## Exemplos

$n = O(n^{3})$? \pause Sim. \pause

$10000n + 10000 = O(n)$? \pause Sim. \pause

$n^{3} + n^{2} + n = O(n^{3})$? \pause Sim. \pause

$n^3 = O(n^2)$? \pause Não. \pause

$n^3 = O(n^4)$? \pause Sim.


## Notação $\Omega$ -- $\Omega$ grande -- _Big-omega_

Para uma função $g(n)$, denotamos por $\Omega(g(n))$ o conjunto de funções:

$\Omega(g(n)) = \{f(n)$: existem constantes positivas $c$ e $n_0$ tal que $0 \le c g(n) \le f(n)$ para todo $n \ge n_0\}$

\includegraphics[trim=79cm 3cm 0cm 0pt,clip, width=4.5cm]{imagens/Fig-3-1.pdf}

\pause

\center $\displaystyle f(n) \in \Omega(g(n)) \iff \lim_{n \to \infty}\frac{f(n)}{g(n)} = L, \pause 0 < L \le \infty.$


## Notação $\Omega$ -- $\Omega$ grande -- _Big-omega_

A notação $\Omega$ descreve um **limite assintótico inferior** para uma função

- Informalmente, dizemos que $f(n)$ cresce no mínimo tão vagarosamente quanto $g(n)$

- A notação $\Omega$ é o oposto da notação $O$, isto é $f(n) = O(g(n)) \iff g(n) = \Omega(f(n))$



## Exemplos

$n^3 \in \Omega(n^2)$? \pause Sim. \pause

$\sqrt n = \Omega(\lg n)$? \pause Sim. \pause

$n^2 + 10n = \Omega(n^2)$? \pause Sim. \pause

$n = \Omega(n^2)$? \pause Não. \pause

$n^2 = \Omega(n)$? \pause Sim.


## Notação $\Theta$

Para uma função $g(n)$, denotamos por $\Theta(g(n))$ o conjunto de funções:

$\Theta(g(n)) = \{f(n)$: existem constantes positivas $c_1$, $c_2$ e $n_0$ tal que $0 \le c_1 g(n) \le f(n) \le c_2 g(n)$ para todo $n \ge n_0\}$

\includegraphics[trim=0cm 3cm 79cm 0pt,clip, width=4.5cm]{imagens/Fig-3-1.pdf}

\pause

\center $\displaystyle f(n) \in \Theta(g(n)) \iff \lim_{n \to \infty}\frac{f(n)}{g(n)} = L, \pause 0 < L < \infty.$


## Notação $\Theta$

A notação $\Theta$ descreve um **limite assintótico restrito** (justo) para uma função

\pause

Para duas funções quaisquer $f(n)$ e $g(n)$, temos que $f(n) = \Theta(g(n))$ se e somente se $f(n) = O(g(n))$ e $f(n) = \Omega(g(n))$.


## Exercícios

$100n^2 = \Theta(n^2)$? \pause Sim. \pause

$\frac{1}{2}n^2 -3n = \Theta(n^2)$? \pause Sim. \pause

$3n^2 + 20 = \Theta(n)$? \pause Não. \pause

$6n = \Theta(n^2)$? \pause Não. \pause

$720 = \Theta(1)$? \pause Sim.


## Comparando crescimento de funções

Sejam $f(n)$ e $g(n)$ funções, então:

$$\begin{aligned}
f(n) \in O(g(n)) & \iff \lim_{n \to \infty}
\frac{f(n)}{g(n)} = L,  & 0 \leq L < \infty.\\
f(n) \in \Omega(g(n)) & \iff \lim_{n \to \infty}
  \frac{f(n)}{g(n)} = L, &  0 < L \leq \infty.\\
f(n) \in \Theta(g(n)) & \iff \lim_{n \to \infty}
  \frac{f(n)}{g(n)} = L, &  0 < L < \infty.\\
\end{aligned}$$


## Analogia com números reais

\center

$f(n) = O(g(n))$ semelhante a $a \le b$

$f(n) = \Omega(g(n))$ semelhante a $a \ge b$

$f(n) = \Theta(g(n))$ semelhante a $a = b$
