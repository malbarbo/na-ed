---
# vim: set spell spelllang=pt_br:
title: Busca e árvores
linkcolor: Black
urlcolor: Blue
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

Podemos melhor o tempo das operações de alteração? \pause Sim! \pause Mas antes de vermos como, precisamos fazer uma revisão de recursividade.
