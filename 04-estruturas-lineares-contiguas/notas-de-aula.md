---
# vim: set spell spelllang=pt_br:
title: Estruturas de dados lineares
subtitle: Alocação contígua
linkcolor: Black
urlcolor: Blue
---

## Introdução

Uma **estrutura de dados** é uma forma de organizar e armazenar dados para facilitar a sua manipulação (operações). \pause

Usamos estruturas de dados para implementar TADs.


## Estrutura de dados lineares

Em uma **estruturas de dados linear**, os elementos são organizados de forma sequencial, um após o outro. \pause Cada elemento possui no máximo um predecessor e um sucessor.\pause

A estrutura de dados linear mais comum é o **arranjo**.


## Arranjos

As duas principais características dos arranjos são: \pause

- Os elementos são armazenados de forma contígua na memória, ou seja, em posições consecutivas. \pause

- Cada elemento do arranjo pode ser acessado diretamente em tempo constante. \pause

Os arranjos podem ser: \pause

- Estáticos: a quantidade de elementos não muda.

- Dinâmicos: a quantidade de elementos pode mudar.


## Arranjos estáticos em Python

O tipo `list`{.python} do Python é de fato um arranjo dinâmico. \pause

Diferente de outras linguagens, o Python não oferece um tipo pré-defino para arranjos estáticos. \pause

Por hora não vamos mais utilizar o tipo `list`{.python}, e sim o tipo `array`{.py}, que "simula" um arranjo de tamanho fixo. \pause

O tipo arranjo está definido na biblioteca `ed`, que está disponível para download na página da disciplina.


## Arranjos estáticos em Python

<div class="columns">
<div class="column" width="40%">
\scriptsize

```python
>>> from ed import array
>>> # Cria um arranjo com 5 zeros
>>> x: array[int] = array(5, 0)
>>> x
array([0, 0, 0, 0, 0])
>>> x[0] = 10
>>> x[4] = 2
>>> x
array([10, 0, 0, 0, 2])
>>> len(x)
5
>>> x[5]
Traceback (most recent call last):
...
IndexError: list index out of range
```

\pause

</div>
<div class="column" width="58%">

\scriptsize

```python
>>> # cria um arranjo a partir de uma lista
>>> x = array([5, 1, 3, 8])
>>> soma = 0
>>> for v in x:
...     soma = soma + v
>>> soma
17
```

\pause

```python
>>> x.append(10)
Traceback (most recent call last):
...
AttributeError: 'array' object has no attribute 'append'
>>> x.pop()
Traceback (most recent call last):
...
AttributeError: 'array' object has no attribute 'pop'
```

</div>
</div>


## Conteúdo

A seguir veremos três TADs e como eles podem ser implementados usando arranjos.


## Exemplo parênteses

Projete uma função que verifique se os parênteses em uma expressão aritmética (representada por uma string) estão corretos, isso é: \pause

- Cada `'('`{.python} tem um `')'`{.python} correspondente \pause

- Um `')'`{.python} não pode aparecer antes do `'('`{.python} correspondente


## Projeto

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def parenteses_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses de *expr*
    estão corretos, False caso contrário.
    '''
```

\pause

```python
    '''
    Exemplos:
    >>> parenteses_corretos('()')
    True
    >>> parenteses_corretos('(')
    False
    >>> parenteses_corretos(')')
    False
    >>> parenteses_corretos('())')
    False
    >>> parenteses_corretos('((a)*(b-c)-10)*((4-2)/8)')
    True
    '''
```

\pause

</div>
<div class="column" width="50%">

Ideia da implementação:

- Analisar a string um caractere por vez.
- Manter um contador de parênteses que foram abertos mas ainda não foram fechados.
- Incrementar o contador a cada abre parênteses e decrementar a cada fecha parênteses (o contador não pode ficar negativo).
- No final, se o contador for 0 e não ficou negativo, os parênteses estão corretos.

</div>
</div>


## Projeto

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def parenteses_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses de *expr*
    estão corretos, False caso contrário.
    '''
```


```python
    '''
    Exemplos:
    >>> parenteses_corretos('()')
    True
    >>> parenteses_corretos('(')
    False
    >>> parenteses_corretos(')')
    False
    >>> parenteses_corretos('())')
    False
    >>> parenteses_corretos('((a)*(b-c)-10)*((4-2)/8)')
    True
    '''
```

</div>
<div class="column" width="50%">

\scriptsize

```python
def parenteses_corretos(expr: str) -> bool:
    abertos = 0
    corretos = True
    i = 0
    while i < len(expr) and corretos:
        if expr[i] == '(':
            abertos = abertos + 1
        elif expr[i] == ')':
            abertos = abertos - 1
            if abertos < 0:
                corretos = False
        i = i + 1
    return abertos == 0 and corretos
```

</div>
</div>


## Exemplo agrupamento

Projete uma função que verifique se os parênteses, colchetes e chaves em uma expressão aritmética (representada por uma string) estão corretos.


## Projeto

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def grupos_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses,
    colchetes e chaves de *expr*
    estão corretos, False caso contrário.

    Exemplos:
    >>> parenteses_corretos('([{}])')
    True
    >>> parenteses_corretos('[](){}')
    True
    >>> parenteses_corretos('({)}')
    False
    >>> parenteses_corretos('(2*[3*{5+2]})')
    False
    >>> parenteses_corretos('([a]*{b-c}-[10])*({(4-2)/8})')
    True
    '''
```

\pause

</div>
<div class="column" width="50%">

Usar um contador (ou mais) não é suficiente. Precisamos saber não apenas quantos "grupos" foram abertos e ainda não foram fechados, mas também qual é a ordem e o tipo do grupo (parênteses, colchetes ou chaves).
</div>
</div>


## Projeto

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def grupos_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses,
    colchetes e chaves de *expr*
    estão corretos, False caso contrário.

    Exemplos:
    >>> parenteses_corretos('([{}])')
    True
    >>> parenteses_corretos('[](){}')
    True
    >>> parenteses_corretos('({)}')
    False
    >>> parenteses_corretos('(2*[3*{5+2]})')
    False
    >>> parenteses_corretos('([a*{(b)-c}]-[10])')
    True
    '''
```

</div>
<div class="column" width="50%">

Ideia da implementação: \pause

- Analisar a string um caractere por vez.
- Manter uma coleção com as ocorrências dos grupos que foram abertos mas ainda não foram fechados.
- Quando um caractere de início de grupo é encontrado ele é _adicionado_ na coleção.
- Quando um caractere de fim de grupo é encontrado ele precisa fechar (_remover_ da coleção) o grupo _mais recentemente aberto_ que ainda não foi fechado.
- No final, se todos os grupos foram abertos e fechados corretamente, a expressão está correta.

</div>
</div>


## Observando a necessidade de um TAD

A ideia de implementação que acabamos de ver requer o uso de uma coleção de valores que tem operações específicas. \pause

Note que no momento não estamos interessados em _como_ implementar essas operações. Nós queremos _utilizar_ essas operações para resolver o problema em questão. \pause

Então podemos definir um TAD com essas operações, resolver o problema que estamos interessados e implementar o TAD depois. \pause

De fato, o TAD que precisamos já é conhecido e é chamado de pilha.


## Pilha

Uma **pilha** (_stack_ em inglês) é tipo abstrato de dados que representa uma coleção de itens que é mantida de acordo com a regra: \pause

- O elemento mais _recentemente inserido_ é o primeiro a ser removido. \pause

Em inglês essa política é chamada de LIFO (_Last In_, _First Out_).


## Pilha

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
class Pilha:
    '''Uma coleção de strings que segue a
    política LIFO: o elemento mais recente-
    mente inserido é o primeiro a ser
    removido.'''

    def empilha(self, item: str):
        '''Adiciona o *item* na pilha.'''

    def desempilha(self) -> str:
        '''Devolve o elemento mais
        recentemente adicionado
        da pilha.
        Requer que a pilha não esteja vazia.'''

    def vazia(self) -> bool:
        '''Devolve True se a pilha está vazia,
        False caso contrário.'''
```

\pause

</div>
<div class="column" width="50%">

![](imagens/stack.pdf)

\small

O método empilha é chamado de _push_ em inglês.

O método desempilha é chamado de _pop_ em inglês.

</div>
</div>


## Pilha

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
class Pilha:
    '''Uma coleção de strings que segue a
    política LIFO: o elemento mais recente-
    mente inserido é o primeiro a ser
    removido.'''

    def empilha(self, item: str):
        '''Adiciona o *item* na pilha.'''

    def desempilha(self) -> str:
        '''Devolve o elemento mais
        recentemente adicionado
        da pilha.
        Requer que a pilha não esteja vazia.'''

    def vazia(self) -> bool:
        '''Devolve True se a pilha está vazia,
        False caso contrário.'''
```

</div>
<div class="column" width="50%">
\scriptsize

```python
>>> p = Pilha()
>>> p.vazia()
True
>>> p.empilha('O')
>>> p.empilha('que')
>>> p.empilha('escrever?')
>>> p.vazia()
False
```

\pause

```python
>>> f.desempilha()
```

\pause

```python
'escrever?'
```

\pause

```python
>>> p.empilha('fazer')
>>> p.empilha('agora?')
>>> while not p.vazia():
...    p.desempilha()
```

\pause

```python
'agora?'
'fazer'
'que'
'O'
```

</div>
</div>


## Exemplo agrupamento

O arquivo `pilha.py`, disponível na página da disciplina, contém uma implementação para `Pilha`.

Faça o download do arquivo e use uma pilha para fazer a implementação da função que verifica se os parênteses, colchetes e chaves em uma expressão aritmética estão corretos.


## Exemplo agrupamento

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def grupos_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses,
    colchetes e chaves de *expr*
    estão corretos, False caso contrário.

    Exemplos:
    >>> parenteses_corretos('([{}])')
    True
    >>> parenteses_corretos('[](){}')
    True
    >>> parenteses_corretos('({)}')
    False
    >>> parenteses_corretos('(2*[3*{5+2]})')
    False
    >>> parenteses_corretos('([a*{(b)-c}]-[10])')
    True
    '''
```

</div>
<div class="column" width="50%">

\scriptsize

```python
def grupos_corretos(expr: str) -> bool:
    p = Pilha()
    corretos = True
    i = 0
    while i < len(expr) and corretos:
        if expr[i] in '([{':
            p.empilha(expr[i])
        elif expr[i] in ')]}':
            if p.vazia() or \
                    not par(p.desempilha(), expr[i]):
                corretos = False
        i = i + 1
    return p.vazia() and corretos

def par(a: str, b: str) -> bool:
    return a == '(' and b == ')' or \
            a == '[' and b == ']' or \
            a == '{' and b == '}'
```

</div>
</div>


## Comparação parênteses e agrupamento

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def parenteses_corretos(expr: str) -> bool:
    abertos = 0
    corretos = True
    i = 0
    while i < len(expr) and corretos:
        if expr[i] == '(':
            abertos = abertos + 1
        elif expr[i] == ')':
            abertos = abertos - 1
            if abertos < 0:
                corretos = False
        i = i + 1
    return abertos == 0 and corretos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
def grupos_corretos(expr: str) -> bool:
    p = Pilha()
    corretos = True
    i = 0
    while i < len(expr) and corretos:
        if expr[i] in '([{':
            p.empilha(expr[i])
        elif expr[i] in ')]}':
            if p.vazia() or \
                    not par(p.desempilha(), expr[i]):
                corretos = False
        i = i + 1
    return p.vazia() and corretos
```

</div>
</div>


## Implementação de Pilha usando arranjo estático

Como implementar uma pilha usando um arranjo estáticos? \pause

Usamos um inteiro para armazenar o `topo` da pilha, isso é, o índice no arranjo do último elemento que foi inserido na pilha: \pause

- Construtor: inicializa o arranjo e o `topo` com `-1`{.python} \pause
- Vazia: verifica se `topo == -1`{.python} \pause
- Empilha: incrementa `topo` e armazena o item na posição `topo` \pause
- Desempilha: devolve o item na posição `topo` e decrementa `topo`


## Implementação de Pilha usando arranjo estático

<div class="columns">
<div class="column" width="50%">
\scriptsize

```python
CAPACIDADE = 100
class Pilha:
    valores: array[str]
    # O índice do elemento que está no topo
    # da pilha, -1 para pilha vazia.
    topo: int

    def __init__(self):
        '''Cria uma nova pilha com capacidade
        para armazenar CAPACIDADE elementos.'''
        self.valores = array(CAPACIDADE, '')
        self.topo = -1
```

\small

Qual é a complexidade de tempo da função `Pilha.__init__`{.python}? \pause

$O($CAPACIDADE$)$, \pause cada um dos `CAPACIDADE` elementos deve ser inicializado com `''`{.python} (o que é feito pela função `array`).

</div>
<div class="column" width="50%">

\scriptsize

\pause

```python
    def empilha(self, item: str):
        assert self.topo < CAPACIDADE - 1
        self.topo = self.topo + 1
        self.valores[self.topo] = item

    def desempilha(self) -> str:
        assert not self.vazia()
        item = self.valores[self.topo]
        self.topo = self.topo - 1
        return item

    def vazia(self) -> bool:
        return self.topo == -1
```

\small

\pause

Qual é a complexidade de tempo das funções `empilha`, `desempilha` e `vazia`? \pause $O(1)$, \pause todas as operações dessas funções têm tempo constante.

</div>
</div>


## Limitações

Qual é a limitação dessa implementação? \pause

- O TAD Pilha não tem capacidade máxima;
- A implementação tem capacidade fixa, o que gera um estouro da pilha (_stack overflow_) quando o usuário tenta empilhar um elemento e a pilha está cheia. \pause

Qual é a limitação da definição do TAD pilha? \pause

- A possibilidade de estouro (negativo) da pilha (_stack underflow_), isso é, a tentativa de remover um elemento quando a pilha está vazia. \pause

Veremos posteriormente como superar essas limitações.


## Revisão

<div class="columns">
<div class="column" width="45%">
\scriptsize

```python
class Pilha:
    def empilha(self, item: str):
        assert self.topo < CAPACIDADE - 1
        self.topo = self.topo + 1
        self.valores[self.topo] = item

    def desempilha(self) -> str:
        assert not self.vazia()
        item = self.valores[self.topo]
        self.topo = self.topo - 1
        return item

    def vazia(self) -> bool:
        return self.topo == -1
```

</div>
<div class="column" width="55%">

\small

Podemos melhor o código? \pause

Em geral, usamos o `assert`{.python} para verificar condições que devem ser verdadeiras durante a execução do programa e cuja a correção depende apenas do projetista do código. Adicionamos o `assert`{.python} como uma rede de segurança, mas esperamos que ele não falhe. \pause

Para condições que devem ser verdadeiras mas a correção depende do usuário do código, usamos uma condicional para fazer a verificação e uma exceção para indicar erro. \pause

O resultado final das duas abordagens é semelhante: a falha do programa. No entanto, o uso de exceções torna claro que o erro é esperado e permite a recuperação e a continuação de execução do programa (não veremos como fazer isso).

</div>
</div>


## Revisão

<div class="columns">
<div class="column" width="55%">
\scriptsize

```python
class Pilha:
    def empilha(self, item: str):
        if self.topo >= CAPACIDADE - 1:
            raise ValueError('pilha cheia')
        self.topo = self.topo + 1
        self.valores[self.topo] = item

    def desempilha(self) -> str:
        if self.vazia():
            raise ValueError('pilha vazia')
        item = self.valores[self.topo]
        self.topo = self.topo - 1
        return item

    def vazia(self) -> bool:
        return self.topo == -1
```

</div>
<div class="column" width="43%">

\scriptsize

```python
>>> p = Pilha()
>>> p.desempilha()
Traceback (most recent call last):
...
ValueError: a pilha está vazia
```

\pause

\normalsize

Podemos fazer mais melhorias? \pause

Podemos escrever

\scriptsize

```python
self.topo += 1
```

\normalsize

Ao invés de

\scriptsize

```python
self.topo = self.topo + 1
```

\pause

\normalsize

Essa forma funciona para qualquer operador binário, mas qual é a vantagem?

</div>
</div>


## Fila

Uma **fila** (_queue_ em inglês) é uma estrutura de dados que representa uma coleção de itens que é mantida de acordo com a política FIFO (_First in_, _First out_):

- O primeiro elemento inserido é o primeiro a ser removido.


## Fila

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
class Fila:
    '''Uma coleção de strings que segue a
    política FIFO: o primeiro a ser
    inserido é o primeiro a ser removido'''

    def enfileira(self, item: str):
        '''Adiciona o *item* no final da
        fila.'''

    def desenfileira(self) -> str:
        '''Remove e devolve o primeiro
        elemento da fila.
        Requer que a fila não esteja
        vazia.'''

    def vazia(self) -> bool:
        '''Devolve True se a fila está
        vazia, False caso contrário.'''
```

\pause

</div>
<div class="column" width="50%">

![](imagens/queue.pdf){width=4cm}

\small

O método enfileira é chamado de _enqueue_ em inglês.

O método desenfileira é chamado de _dequeue_ em inglês.

</div>
</div>


## Fila

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
class Fila:
    '''Uma coleção de strings que segue a
    política FIFO: o primeiro a ser
    inserido é o primeiro a ser removido.'''

    def enfileira(self, item: str):
        '''Adiciona o *item* no final da
        fila.'''

    def desenfileira(self) -> str:
        '''Remove e devolve o primeiro
        elemento da fila.
        Requer que a fila não esteja
        vazia.'''

    def vazia(self) -> bool:
        '''Devolve True se a fila está
        vazia, False caso contrário.'''
```

</div>
<div class="column" width="50%">

\scriptsize

```python
>>> f = Fila()
>>> f.vazia()
True
>>> f.enfileira('Amanda')
>>> f.enfileira('Fernando')
>>> f.enfileira('Márcia')
>>> f.vazia()
False
```

\pause

```python
>>> p.desenfileira()
```

\pause

```python
'Amanda'
```

\pause

```python
>>> f.enfileira('Pedro')
>>> f.enfileira('Alberto')
>>> while not f.vazia():
...     f.desenfileira()
```

\pause

```python
'Fernando'
'Márcia'
'Pedro'
'Alberto'
```

</div>
</div>


## Implementação de fila usando arranjo estático

<div class="columns">
<div class="column" width="48%">
Como implementar uma fila usando um arranjo estático? \pause

Usando um inteiro para indicar o `fim` da fila: \pause

- Construtor: inicializa o arranjo e o `fim` com `-1`{.python}. \pause
- Vazia: verifica se `fim == -1`{.python} \pause
- Enfileira: incrementa `fim` e armazena o item na posição `fim`. \pause
- Desenfileira: devolve o item na posição 0, move os itens (1 $\rightarrow$ 0, 2 $\rightarrow$ 1, etc) e decrementa o `fim`. \pause
</div>
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    valores: array[str]
    fim: int

    def enfileira(self, item: str):
        if self.fim >= CAPACIDADE - 1:
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> str:
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[0]
        for i in range(1, self.fim + 1):
            self.valores[i - 1] = self.valores[i]
        self.fim -= 1
        return item
```
</div>
</div>


## Implementação de fila usando arranjo estático

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    valores: array[str]
    fim: int

    def enfileira(self, item: str):
        if self.fim >= CAPACIDADE - 1:
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> str:
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[0]
        for i in range(1, self.fim + 1):
            self.valores[i - 1] = self.valores[i]
        self.fim -= 1
        return item
```
</div>
<div class="column" width="48%">
Qual é a complexidade de tempo do método `enfileira`? \pause $O(1)$. \pause

Qual é a complexidade de tempo do método `desenfileira`? \pause $O(n)$, onde $n$ é a quantidade de elementos da fila. \pause Os elementos das posições $1, 2, 3, \dots, n - 1$ são movidos para as posições $0, 1, 2, \dots, n - 2$. \pause

Podemos fazer melhor? \pause Sim!

</div>
</div>


## Implementação de fila usando arranjo estático

<div class="columns">
<div class="column" width="48%">
Podemos usar inteiros para indicar o `inicio` e o `fim` da fila da seguinte maneira: \pause

- Construtor: inicializa o arranjo, `inicio` com 0 e `fim` com `-1`{.python}. \pause
- Vazia: verifica se `fim < inicio`{.python} \pause
- Enfileira: incrementa `fim` e armazena o item na posição `fim`. \pause
- Desenfileira: devolve o item na posição `inicio` e incrementa `inicio`. \pause
</div>
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    valores: array[str]
    # Indíce do último elemento da fila
    fim: int
    # Indíce do primeiro elemento da fila
    inicio: int

    def enfileira(self, item: str):
        if self.fim >= CAPACIDADE - 1:
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> str:
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        self.inicio += 1
        return item
```
</div>
</div>


## Implementação de fila usando arranjo estático

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    valores: array[str]
    # Indíce do último elemento da fila
    fim: int
    # Indíce do primeiro elemento da fila
    inicio: int

    def enfileira(self, item: str):
        if self.fim >= CAPACIDADE - 1:
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> str:
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        self.inicio += 1
        return item
```
</div>
<div class="column" width="48%">
Qual é a complexidade de tempo do método `enfileira`? \pause $O(1)$. \pause

Qual é a complexidade de tempo do método `desenfileira`? \pause $O(1)$. \pause

Existe alguma limitação nessa implementação? \pause Sim, a fila pode estar vazia e não ser possível enfileirar um novo item! \pause

Podemos fazer melhor? \pause Sim!
</div>
</div>


## Implementação de fila circular

Usamos índices `inicio` e `fim` que avançam de forma "circular", isto é, são incrementados até chegarem no final do arranjo e depois voltam para 0. O `fim` representa o índice onde o próximo elemento será inserido.

Para uma fila com capacidade $C$ alocamos um arranjo de tamanho $C + 1$. Isto permite diferenciar entre fila vazia (`inicio == fim`{.python}) e fila cheia (o próximo valor de `fim` é igual ao `inicio`.

## {.plain}

![](imagens/fila-circular.pdf)


## Implementação de fila circular

<div class="columns">
<div class="column" width="48%">
Descrição da implementação dos métodos

- Construtor: inicializa o arranjo, `inicio` e `fim` com `0`{.python}. \pause
- Vazia: verifica se `inicio == fim`{.python} \pause
- Enfileira: armazena o item na posição `fim` e avança `fim`. \pause
- Desenfileira: devolve o item na posição `inicio` e avança `inicio`. \pause
</div>
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    def enfileira(self, item: str):
        if self.cheia():
            raise ValueError('fila cheia')
        self.valores[self.fim] = item
        if self.fim == CAPACIDADE:
            self.fim = 0
        else:
            self.fim += 1

    def desenfileira(self) -> str:
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        if self.inicio == CAPACIDADE:
            self.inicio = 0
        else:
            self.inicio += 1
        return item
```
</div>
</div>


## Implementação de fila circular

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    def enfileira(self, item: str):
        if self.cheia():
            raise ValueError('fila cheia')
        self.valores[self.fim] = item
        if self.fim == CAPACIDADE:
            self.fim = 0
        else:
            self.fim += 1

    def desenfileira(self) -> str:
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        if self.inicio == CAPACIDADE:
            self.inicio = 0
        else:
            self.inicio += 1
        return item
```
</div>
<div class="column" width="48%">
\pause

Qual é a complexidade de tempo de `enfileira` e `desenfileira`? \pause $O(1)$.

\pause

A implementação "circular" de fila não tem as limitações das duas implementações anteriores, e por isso é bastante utilizada na prática, mas na forma de uma fila dupla.

</div>
</div>


## Fila dupla

Uma **fila dupla** (_double ended queue_ - _deque_ em inglês) é uma sequência linear onde os itens podem ser inseridos e removidos dos dois extremos, o que de certa forma é uma generalização de pilha e fila. \pause

Muitas linguagens não oferecem na biblioteca padrão uma implementação separada para pilha, fila e fila dupla, mas apenas uma implementação de fila dupla. Este é o caso do Python (`collections.deque`), do Rust (`std::collections::VecDeque`), entre outras. \pause

Como os termos início e fim podem parecer confusos para uma fila dupla, alguns autores usam os termos esquerda e direita.


## Lista

Uma **lista** é um tipo abstrato de dados que representa uma sequência de itens. \pause

Na pilha e fila a inserção e remoção dos elementos segue uma política específica, já em uma lista, os elementos podem ser inseridos e removidos sem restrições. \pause Além disso, os elementos de uma lista podem ser consultados sem serem removidos. \pause

Para uma lista que representa a sequência $x_0, x_1, ..., x_{n-1}$: \pause

- O tamanho da lista é $n$ \pause
- O elemento $x_i$ está na posição (índice) $i$ \pause
- Para $n > 0$, $x_0$ é o primeiro elemento e $x_{n-1}$ é o último elemento \pause
- $x_i$ precede (é o predecessor) de $x_{i+1}$ para $i = 0, 1, \dots, n - 2$ \pause
- $x_i$ sucede (é sucessor) $x_{i - 1}$ para $i = 1, 2, \dots, n - 1$


## Operações com lista

As definições de operações para o TAD lista dependem da aplicação, mas as seguintes operações são comuns: \pause

- Consulta da quantidade de itens \pause
- Acesso e modificação de um item de uma posição (indexação) \pause
- Inserção de um item em uma posição \pause
- Remoção de um item em uma posição \pause
- Remoção de um item pelo valor do item \pause
- Localização de um item \pause
- Geração de uma representação em string da lista


## Lista

\scriptsize

```python
class Lista:
    '''Uma sequência de números.'''

    def num_itens(self) -> int:
        '''Devolve a quantidade de itens da lista.'''

    def get(self, i: int) -> int:
        '''Devolve o item que está na posição *i* da lista.
        Requer que 0 <= i < self.num_itens().'''

    def set(self, i: int, item: int):
        '''Armazena *item* na posição **i** da lista.
        Requer que 0 <= i < self.num_itens().'''

    def insere(self, i: int, item: int):
        '''Insere *item* na posição *i* da lista. Os itens que estavam inicialmente
        nas posiçõe i, i+1, ..., passam a ficar nas posições i+1, i+2, ...
        Requer que 0 <= i <= self.num_itens().'''
```


## Lista

\scriptsize

```python
class Lista:
    def remove(self, i: int) ->:
        '''Remove e devolve o item na posição *i* da lista. Os itens que estavam
        inicialmente nas posições i, i+1, ..., passam a ficar nas posições
        i-1, i, ...
        Requer que 0 <= i < self.num_itens().'''

    def remove_item(self, item: int) ->:
        '''Remove a primeira ocorrência de *item* da lista. Se i é a posição do
        *item*, então os itens que estavam inicialmente nas posições i, i+1,
        ..., passam a ficar nas posições i-1, i, ...
        Requer que o item esteja na lista.'''

    def indice(self, item: int) -> int:
        '''Devolve a posição da primeira ocorrência de *item* na lista.
        Requer que *item* esteja presente na lista.'''

    def str(self) -> str:
        '''Gera uma representação em string da lista.'''
```


## Lista - Exemplos

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
>>> lst = Lista()
>>> lst.str()
'[]'
>>> lst.insere(0, 7)
>>> lst.insere(1, 20)
>>> lst.insere(2, 5)
>>> lst.get(0)
7
>>> lst.get(2)
5
>>> lst.num_itens()
3
>>> lst.str()
'[7, 20, 5]'
```

\pause

```python
>>> lst.set(0, 10)
>>> lst.str()
```

\pause

```python
'[10, 20, 5]'
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
>>> lst.insere(1, 8)
>>> lst.str()
```

\pause

```python
'[10, 8, 20, 5]'
```

\pause

```python
>>> lst.remove(2)
>>> lst.str()
```

\pause

```python
'[10, 8, 5]'
```

\pause

```python
>>> lst.insere(lst.num_itens(), 8)
>>> lst.str()
```

\pause

```python
'[10, 8, 5, 8]'
```

\pause

```python
>>> lst.indice(8)
```

\pause

```python
1
```

\pause

```python
>>> lst.remove_item(5)
>>> lst.str()
```

\pause

```python
'[10, 8, 8]'
```

</div>
</div>


## Lista

<div class="columns">
<div class="column" width="55%">
\small
Como implementar o TAD lista usando um arranjo estático? \pause

Além do arranjo armazenamos a quantidade de elementos na lista. \pause

As operações de tamanho, acesso e modificação em um posição, são diretas. \pause

Para inserção e remoção (em uma posição) é preciso deslocar os elementos de maneira semelhante ao que fizemos para a primeira implementação de fila. \pause

A busca por um elemento e a representação por string é feita com uma repetição pelos elementos da lista. \pause

Por fim, a remoção de um item pode ser feita com uma busca seguido da remoção por posição. \pause

</div>
<div class="column" width="43%">
![](imagens/arranjo.pdf){width=4cm}

\small

Vamos fazer implementação e determinar as complexidades de tempo juntos!

</div>
</div>


## Lista

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
class Lista:
    def insere(self, i: int, item: int):
        for j in range(self.tamanho, i, -1):
            self.valores[j] = self.valores[j - 1]
        self.valores[i] = item
        self.tamanho += 1

    def remove(self, i: int):
        for j in range(i + 1, self.tamanho):
            self.valores[j - 1] = self.valores[j]
        self.tamanho -= 1

    def str(self) -> str:
        s = '['
        if self.num_itens() != 0:
            s += str(self.valores[0])
            for i in range(1, self.num_itens()):
                s += ', ' + str(self.valores[i])
        return s + ']'
```

</div>
<div class="column" width="45%">

\small

Veja o código completo (e verificação dos erros!) no arquivo `lista.py`. \pause

A complexidade de tempo de `str`, `insere`, `remove`, `remove_item` e `indice` é $O(n)$. No caso especial de inserção e remoção por posição do final a complexidade é $O(1)$. As demais operações são constantes.
</div>
</div>


## Limitações das implementações com arranjos estáticos

Vimos como implementar os TADs Pilha, Fila, Fila Dupla e Lista usando arranjos estáticos. \pause

Também discutimos a principal limitação das implementações: a capacidade máxima de itens que podem ser armazenados. \pause

Agora vamos ver como superar essa limitação!


## Referências

As variáveis em Python são referências para células de memórias. Quando atribuímos uma instância de um arranjo estático para uma variável, a variável passa a referenciar o bloco de células de memória do arranjo. \pause

Apesar do bloco de memória reservado para o arranjo não poder mudar de tamanho, a variável que referencia o bloco de memória pode referenciar outro bloco de memória, com mais ou menos células.


## Referências

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
>>> from ed import array
>>> arr = array([3, 8, 2])
>>> len(array)
3
```
</div>
<div class="column" width="48%">
![](imagens/referencia-arranjo-1.pdf)
</div>
</div>

\pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
>>> arr = array([4, 2, 7, 8, 1, 7])
>>> len(arr)
6
```
</div>
<div class="column" width="48%">
![](imagens/referencia-arranjo-2.pdf)
</div>
</div>


## Arranjo dinâmico

Como podemos utilizar esse fato para superar a limitação de capacidade máxima de itens? \pause

Substituindo o arranjo por um com maior capacidade toda vez que a coleção ficar cheia! \pause

- Alocamos um arranjo maior \pause
- Copiamos os itens do arranjo cheio para o novo arranjo \pause
- Atribuímos o novo arranjo para a variável \pause

Veja a implementação dos métodos `Lista.insere` e `Lista.__cresce` do arquivo `lista.py`. \pause

Essa é a forma mais comum utilizada para implementar arranjos dinâmicos. Essa é a forma que `list`{.python} do Python é implementado!


## Arranjo dinâmico

Algumas perguntas: \pause

- Quanto maior? \pause Muitas implementações dobram o tamanho. \pause
- Como isso afeta a complexidade de tempo das operações? \pause Inserir no fim, que era constante, fica com tempo _amortizado_ de $O(1)$ (a maior parte das inserções no final é constante, mas algumas -- quanto o arranjo está cheio -- são $O(n)$). \pause
- E se a coleção ficar com poucos itens? \pause Podemos substituir o arranjo por um novo com menor capacidade! (veja a lista de exercícios)


## Revisão

Vimos 4 tipos abstratos de dados e como implementá-los usando arranjos: \pause

- Pilha (inserção e remoção do mesmo extremo) \pause
- Fila (inserção em um extremo e remoção do outro) \pause
- Fila Dupla (inserção e remoção dos dois extremos) \pause
- Lista (inserção e remoção em qualquer posição) \pause

Se usarmos arranjos estáticos, então é preciso definir uma capacidade máxima, o que pode não ser adequado para algumas aplicações.

Se usarmos arranjos dinâmicos, então a capacidade não é limitada mas o tempo de execução de algumas operações é alterada.


## Resumo

Estrutura / Operação | inserção | remoção
---------------------|----------|----------
Pilha                |  $O(1)$  | $O(1)$
Fila                 |  $O(1)$  | $O(1)$
Fila Dupla           |  $O(1)$  | $O(1)$
Lista                |  $O(n)$ -- $O(1)$ no fim  | $O(n)$ -- $O(1)$ no fim

\pause

Os tempos $O(1)$ são amortizados para as implementações com arranjos dinâmicos. \pause

Veremos a seguir como fazer as implementações desses TADs de maneira que o tempo de execução dessas operações sejam $O(1)$ no pior caso.

## Referências

Capítulo 7, 8, 9 - Pilhas, filas e listas - Fundamentos de Python: Estruturas de dados. Kenneth A. Lambert. (Disponível na Minha Biblioteca na UEM).

Seção 10.1 - Pilhas e filas - Algoritmos: Teoria e Prática, 3a. edição, Cormen, T. at all.
