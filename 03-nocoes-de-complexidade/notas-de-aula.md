---
# vim: set spell spelllang=pt_br:
title: Noções de complexidade de algoritmos
linkcolor: Black
urlcolor: Blue
# TODO: falar sobre análise experimental
# TODO: exemplo máximo de uma lista em ordem não decrescente
# TODO: falar de análise de um algoritmo particular vs uma classe de algoritmos
# TODO: destacar o propósito da notação assintótica e suas limitações
# TODO: adicionar resumo
# TODO: colocar o limite em casa exemplo?
---

## Introdução

Quando fazemos o projeto de uma função ou de um tipo de dado separamos a especificação (o que) da implementação (como). \pause

Isso trás diversos benefícios, entre eles: \pause

- Oculta a complexidade da implementação (abstração); \pause

- Permite o desenvolvimento independente; \pause

- Permite implementações alternativas.


## Complexidade de algoritmos

Se podemos fazer a implementação de diversas maneirais, quais critérios podemos utilizar para escolher uma implementação? \pause

- Simplicidade; \pause

- Consumo de recurso (tempo, memória, energia, etc).

\pause

Formalmente, o consumo de recurso de um algoritmo é chamada de **complexidade do algoritmo**.


## Análise de algoritmos

Para podermos determinar qual algoritmo é mais eficiente (tem menor complexidade), precisamos de: \pause

- Determinar a complexidade; \pause

- Expressar a complexidade; \pause

- Comparar a complexidade. \pause

O processo de determinar a complexidade de algoritmos é chamado de **análise de algoritmos**. \pause

Para expressar e comparar complexidades de algoritmos vamos utilizar a **notação assintótica**.


## Formas de análise

A análise de um algoritmo pode ser: \pause

- Experimental; \pause

- Teórica;\pause

A análise experimental é mais específica pois dependente da linguagem, do compilador / interpretador, do hardware, etc. \pause

A análise teórica (ou analítica) é mais geral e provê entendimento das propriedades e limitações inerentes ao algoritmo. \pause

As duas formas de análise são complementares. \pause

Nessa disciplina vamos focar na análise teórica.


## Análise teórica

Na **análise teórica** adotamos uma máquina teórica de computação e expressamos a complexidade de um algoritmo através de uma **função que relaciona o tamanho da entrada com o consumo de recurso** nessa máquina teórica. \pause

A máquina teórica que vamos adotar tem operações lógicas e aritméticas, cópia de dados e controle de fluxo, e tem as seguintes características: \pause

- As instruções são executadas uma por vez e em sequência; \pause

- Cada operação é executa em uma unidade de tempo.


## Análise teórica

Em geral, não estamos procurando uma função precisa para a complexidade de um algoritmo, mas uma que descreve de forma razoável como o consumo do recurso cresce em relação ao crescimento do tamanho da entrada, o que chamamos de **ordem de crescimento**. \pause Além disso, estamos interessados em entradas suficientemente grandes, para que o algoritmo demore algum tempo razoável para executar e não termine rapidamente. \pause

Por esse motivo, em alguns casos podemos fazer simplificações na análise, como por exemplo, levar em consideração apenas as **operações que são mais executadas**.


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
    max = lst[0]
    for i in range(1, len(lst)):
        if max < lst[i]:
            max = lst[i]
    return max
```
</div>
<div class="column" width="50%">

Vamos fazer a análise da função máximo para determinar a sua complexidade de tempo, isto é, determinar
como o tempo de execução ($T(n)$) está relacionado com o tamanho da entrada ($n$ - quantidade de elementos de `lst`). \pause

Quais são as operações mais executadas pela função? \pause O incremente e comparação de `i` (que estão implícitos) e a comparação de `max`. \pause

Quantas vezes a operação `<` é executada? \pause $n - 1$. \pause

Dessa forma, podemos dizer que a complexidade de tempo de `maximo` é $T(n) = n - 1$.
</div>
</div>


## Entrada específica

O tempo de execução de um algoritmo pode depender não apenas do tamanho da entrada, mas do valor específico da entrada. Em outras palavras, para um _mesmo tamanho de entrada_, o tempo de execução pode mudar de acordo com os _valores da entrada_.


## Exemplo contém

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def contem(lst: list[int], x: int) -> bool:
    '''
    Devolve True se *x* está em *lst*,
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
        if lst[i] == x:
            contem = True
        i = i + 1
    return contem
```

\pause
</div>
<div class="column" width="50%">
Para uma entrada de tamanho $n$, quantas vezes a operação `==` é executada? \pause

Depende dos valores entrada! \pause

- Melhor caso: `x` é o primeiro de `lst`, 1 vez \pause

- Pior caso: `x` não está em `lst`, $n$ vezes \pause

- Caso médio: considerando que `x` está em `lst` e tem a mesma probabilidade de estar em qualquer posição, $\frac{n + 1}{2}$ vezes \pause

Portanto, para o caso geral, a complexidade de tempo da função é $T(n) = n$.

</div>
</div>


## Exemplo ordenação seleção

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def ordena_selecao(lst: list[int]):
    '''Ordena os elementos de *lst*
    em ordem não decrescente.
    Exemplos
    >>> lst = [8, 1, 6, 3, 1]
    >>> ordena(lst)
    >>> lst
    [1, 1, 3, 6, 8]
    '''
    for i in range(0, len(lst) - 1):
        # Encontra o mínimo
        # e coloca na posição i
        min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        t = lst[i]
        lst[i] = lst[min]
        lst[min] = t
```

\pause
</div>
<div class="column" width="50%">
\small

Para uma entrada de tamanho $n$, quantas vezes a operação `<` é executada? \pause

- Para $i = 0$, \pause $n - 1$ \pause
- Para $i = 1$, \pause $n - 2$ \pause
- Para $i = 2$, \pause $n - 3$ \pause
- $\dots$ \pause
- Para $i = n - 2$, \pause $1$ \pause

Portanto, o total de vezes que `<` é executado é

$\displaystyle \sum_{k = 1}^{n} (n - k)
\pause = \sum_{k = 1}^{n} n - \sum_{k = 1}^{n} k
\pause = n^2 - \frac{n(n - 1)}{2} \pause$

Portanto, a complexidade de tempo de `ordena_selecao` é $T(n) = \displaystyle \frac{n^2 - n}{2}$

</div>
</div>


## Notação assintótica


Para podermos determinar qual algoritmo é mais eficiente (tem menor complexidade), precisamos de: \pause

- Determinar a complexidade; \pause Feito; \pause

- Expressar a complexidade; \pause

- Comparar a complexidade. \pause

Agora vamos ver a **notação assintótica**, que permite expressar e comparar mais facilmente complexidades de tempos. \pause Vamos ver três notações:

- Notação $O$
- Notação $\Omega$
- Notação $\Theta$


## Notação $O$ -- $O$ grande -- _Big-oh_

A notação $O$ descreve um **limite assintótico superior** para uma função. \pause

Para uma função $g(n)$, denotamos por $O(g(n))$ o conjunto de funções $\{f(n)$: existem constantes positivas $c$ e $n_0$ tal que $0 \le f(n) \le c g(n)$ para todo $n \ge n_0\}$.

\includegraphics[trim=37cm 3cm 37cm 0pt,clip, width=4.5cm]{imagens/Fig-3-1.pdf}

\pause

\center $\displaystyle f(n) \in O(g(n)) \iff \lim_{n \to \infty}\frac{f(n)}{g(n)} = L, \pause 0 \leq L < \infty.$


## Notação $O$ -- $O$ grande -- _Big-oh_

Escrevemos $f(n) = O(g(n))$ para indicar que $f(n) \in O(g(n))$ \pause

Informalmente, dizemos que $f(n)$ cresce no máximo tão rapidamente quanto $g(n)$.


## Exemplos

$n = O(n^{3})$? \pause Sim. \pause

$10000n + 10000 = O(n)$? \pause Sim. \pause

$n^{3} + n^{2} + n = O(n^{3})$? \pause Sim. \pause

$n^3 = O(n^2)$? \pause Não. \pause

$n^3 = O(n^4)$? \pause Sim.


## Notação $\Omega$ -- $\Omega$ grande -- _Big-omega_

A notação $\Omega$ descreve um **limite assintótico inferior** para uma função. \pause

Para uma função $g(n)$, denotamos por $\Omega(g(n))$ o conjunto de funções $\{f(n)$: existem constantes positivas $c$ e $n_0$ tal que $0 \le c g(n) \le f(n)$ para todo $n \ge n_0\}$

\includegraphics[trim=79cm 3cm 0cm 0pt,clip, width=4.5cm]{imagens/Fig-3-1.pdf}

\pause

\center $\displaystyle f(n) \in \Omega(g(n)) \iff \lim_{n \to \infty}\frac{f(n)}{g(n)} = L, \pause 0 < L \le \infty.$


## Notação $\Omega$ -- $\Omega$ grande -- _Big-omega_

Informalmente, dizemos que $f(n)$ cresce no mínimo tão rapidamente quanto $g(n)$. \pause

A notação $\Omega$ é o oposto da notação $O$, isto é $f(n) = O(g(n)) \iff g(n) = \Omega(f(n))$.


## Exemplos

$n^3 \in \Omega(n^2)$? \pause Sim. \pause

$\sqrt n = \Omega(\lg n)$? \pause Sim. \pause

$n^2 + 10n = \Omega(n^2)$? \pause Sim. \pause

$n = \Omega(n^2)$? \pause Não. \pause

$n^2 = \Omega(n)$? \pause Sim.


## Notação $\Theta$

A notação $\Theta$ descreve um **limite assintótico restrito** (justo) para uma função. \pause

Para uma função $g(n)$, denotamos por $\Theta(g(n))$ o conjunto de funções $\{f(n)$: existem constantes positivas $c_1$, $c_2$ e $n_0$ tal que $0 \le c_1 g(n) \le f(n) \le c_2 g(n)$ para todo $n \ge n_0\}$

\includegraphics[trim=0cm 3cm 79cm 0pt,clip, width=4.5cm]{imagens/Fig-3-1.pdf}

\pause

\center $\displaystyle f(n) \in \Theta(g(n)) \iff \lim_{n \to \infty}\frac{f(n)}{g(n)} = L, \pause 0 < L < \infty.$


## Notação $\Theta$

Para duas funções quaisquer $f(n)$ e $g(n)$, temos que $f(n) = \Theta(g(n))$ se e somente se $f(n) = O(g(n))$ e $f(n) = \Omega(g(n))$.


## Exercícios

$100n^2 = \Theta(n^2)$? \pause Sim. \pause

$\frac{1}{2}n^2 -3n = \Theta(n^2)$? \pause Sim. \pause

$3n^2 + 20 = \Theta(n)$? \pause Não. \pause

$6n = \Theta(n^2)$? \pause Não. \pause

$720 = \Theta(1)$? \pause Sim.


## Resumo

Sejam $f(n)$ e $g(n)$ funções, então:

$$\begin{aligned}
f(n) \in O(g(n)) & \iff \lim_{n \to \infty}
\frac{f(n)}{g(n)} = L,  & 0 \leq L < \infty.\\
f(n) \in \Omega(g(n)) & \iff \lim_{n \to \infty}
  \frac{f(n)}{g(n)} = L, &  0 < L \leq \infty.\\
f(n) \in \Theta(g(n)) & \iff \lim_{n \to \infty}
  \frac{f(n)}{g(n)} = L, &  0 < L < \infty.\\
\end{aligned}$$

\pause

Analogia com números reais

\center

$f(n) = O(g(n))$ semelhante a $a \le b$

$f(n) = \Omega(g(n))$ semelhante a $a \ge b$

$f(n) = \Theta(g(n))$ semelhante a $a = b$


## Tempos de execução comuns

| Classe       | Descrição   |
|--------------|-------------|
| $O(1)$       | Constante   |
| $O(\lg n)$   | Logarítmico |
| $O(n)$       | Linear      |
| $O(n \lg n)$ | Log Linear  |
| $O(n^2)$     | Quadrático  |
| $O(n^3)$     | Cúbico      |
| $O(2^n)$     | Exponencial |
| $O(n!)$      | Fatorial    |


## Tempos de execução comuns

![Fonte: <https://www.geeksforgeeks.org/what-is-logarithmic-time-complexity/>](imagens/time-complexity.jpg){width=10cm}
