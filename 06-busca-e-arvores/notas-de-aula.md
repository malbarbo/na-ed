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

Podemos melhor o tempo das operações de alteração? \pause Sim! \pause Mas antes precisamos revisar recursividade.


## Recursividade

Uma função é **recursiva** quando ela chama a si mesmo de forma direta ou indireta. \pause

A recursividade é uma técnica muito poderosa e bastante utilizada na Computação e Matemática. \pause

De certa a forma a recursividade é um caso especial da decomposição de problemas. \pause

De forma geral podemos resolver um problema decompondo-o em subproblemas mais simples, resolvendo os subproblemas e combinado as soluções para obter a solução do problema inicial. \pause

A recursividade surge quando decompomos um problema em subproblemas do _mesmo tipo_, pois nesses casos podemos utilizar _o mesmo processo_ para resolver o problema inicial e os subproblemas. \pause Note que para que o processo funciona, devemos definir situações limites em que o problema seja resolvido diretamente, sem precisar ser decomposto, que são os casos bases.


## Recursividade

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
                |   \_________________/
         primeiro    contem(resto, v)
               10         True

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
                |   \_________________/
         primeiro    contem(resto, v)
               10         True

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
                |   \_________________/
         primeiro    contem(resto, v)
               10         True

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
                |   \_________________/
         primeiro    contem(resto, v)
               10         True

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

Projete uma função que modifique uma lista somando 1 em cada elemento da lista.


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

No entanto, se fizermos a decomposição estrutural, isto é, decompor o problema conforme o dado que descrevo o problema é composto, então o projeto de funções recursivas se torna um processo mais sistemático. \pause

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

Projete uma função que crie um arranjo $[1, 2, ..., n]$. \pause

\scriptsize

```python
def lista_n(n: int) -> int:
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

Projete uma função que crie um arranjo $[1, 2, ..., n]$.

\scriptsize

```python
def lista_n(n: int) -> int:
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

Tentar definir um arranjo com autorreferência pode ser um pouco confuso... \pause Mas podemos pensar que um arranjo é vazio, ou tem um primeiro elemento e o restante dos elementos. \pause

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

Qual o problema com essa estratégia? \pause O _slice_ cria uma cópia do arranjo, o que é custoso. \pause
Podemos fazer melhor? \pause Sim!
</div>
</div>


## Recursão com arranjos

<div class="columns">
<div class="column" width="48%">

Ao invés de "diminuir" o arranjo do início, vamos diminuir do fim usando um "tamanho virtual". \pause

Junto com o arranjo passamos também um valor $n$, que representa quantos elementos a partir do início do arranjo devem ser considerados. \pause Na chamada recursiva, passamos o arranjo inalterado e o valor $n - 1$, que representa a diminuição do arranjo. \pause O modelo ficaria:

\scriptsize

```python
def fn_para_array(lst: list[int], n: int) -> ...:
    if n == 0:
        return ...
    else:
        return lst[n - 1] ... fn_para_array(lst, n - 1)

```

</div>
<div class="column" width="48%">

\pause

Projete uma função que some todos os elementos de um arranjo.

\pause

\scriptsize

```python
def soma(lst: list[int], n: int) -> int:
    '''
    Soma os primeiros *n* elementos de *lst*.
    Requer que 0 <= n <= len(lst)
    Exemplo
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
</div>
</div>


## Criando uma árvore de busca {.b}

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


## Criando uma árvore de busca {.b}

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


## Criando uma árvore de busca {.b}

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


## Criando uma árvore de busca {.b}

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
