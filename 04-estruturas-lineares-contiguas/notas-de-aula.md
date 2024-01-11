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

Uma **pilha** (_stack_ em inglês) é uma coleção de itens que é mantida de acordo com a regra: \pause

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

Faça uma implementação de Pilha usando arranjo estático.


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

Qual a complexidade de tempo da função `Pilha.__init__`{.python}? \pause

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

Qual a complexidade de tempo das funções `empilha`, `desempinha` e `vazia`? \pause $O(1)$, \pause todas as operações dessas funções têm tempo constante.

</div>
</div>


## Limitações

Qual a limitação dessa implementação? \pause

- O TAD Pilha não tem capacidade máxima;
- A implementação tem capacidade fixa, o que gera um estouro da pilha (_stack overflow_) quando o usuário tenta empilhar um elemento e a pilha está cheia. \pause

Qual a limitação da definição do TAD pilha? \pause

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

Vimos que um pilha usa a política LIFO (_Last In_, _First out_).

Uma **fila** (_queue_ em inglês) é uma coleção de itens que é mantido de acordo com a política FIFO (_First in_, _First out_):

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

\pause

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
Qual a complexidade de tempo do método `enfileira`? \pause $O(1)$. \pause

Qual a complexidade de tempo do método `desenfileira`? \pause $O(n)$, onde $n$ é a quantidade de elementos da fila. \pause Os elementos das posições $1, 2, 3, \dots, n - 1$ são movidos para as posições $0, 1, 2, \dots, n - 2$. \pause

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
Qual a complexidade de tempo do método `enfileira`? \pause $O(1)$. \pause

Qual a complexidade de tempo do método `desenfileira`? \pause $O(1)$. \pause

Existe alguma limitação nessa implementação? \pause Sim, a fila pode estar cheia e vazia ao mesmo tempo! \pause

Podemos fazer melhor? \pause Sim!
</div>
</div>


<!--
## Primos

Projete uma função que encontre todos os números primos menores que um determinado valor.


## Primos

<div class="columns">
<div class="column" width="50%">
Especificação

\scriptsize

```python
def primos(lim: int) -> list[int]:
    '''
    Encontra todos os números primos
    menores que *lim*.

    Exemplos:
    >>> primos(2)
    []
    >>> primos(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    '''
```

\pause

</div>
<div class="column" width="50%">
Implementação

\scriptsize

```python
def primos(lim: int) -> list[int]:
    primos = []
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
</div>


## Arranjos dinâmicos

Para implementar a função `primos` utilizamos o tipo `list`{.python}, que é pré-definido em Python.

\pause

Apesar de chamar `list`{.python}, conceitualmente esse tipo representa um arranjo dinâmico.

\pause

Algumas linguagens, como a C, não tem arranjo dinâmico pré-definido, apenas arranjo de tamanho fixo.

\pause

Como implementar um arranjo dinâmico em uma linguagem que só oferece arranjo de tamanho fixo?


## Arranjo

Vamos supor que ao invés de oferecer o tipo `list`{.python}, o Python oferece um tipo `array` (arranjo de tamanho fixo) e funcionasse da seguinte forma: \pause

<div class="columns">
<div class="column" width="40%">
\scriptsize

```python
>>> # Cria um arranjo com 5 zeros
>>> x = array(5)
>>> x
array([0, 0, 0, 0, 0])
>>> x[0] = 10
>>> x[4] = 2
>>> x
array([10, 0, 0, 0, 2])
>>> len(x)
5
```

\pause

</div>
<div class="column" width="58%">

\scriptsize

```
>>> x.append(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    x.append(5)
    ^^^^^^^^
AttributeError: 'array' object has no attribute 'append'
>>> x.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    x.pop()
    ^^^^^
AttributeError: 'array' object has no attribute 'pop'
>>>
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```{.python .number-lines}
def primos(lim: int) -> list[int]:
    primos = []
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```
</div>
<div class="column" width="50%">

Quais operações de lista (arranjo dinâmico) são utilizadas na função `primos`? \pause

- Criação (2 - literal) \pause
- Quantidade de elementos (7 - função) \pause
- Acesso a uma posição (8 - indexação) \pause
- Acréscimo (13 - método) \pause

Essas operações usam formas diferentes, mas a ideia de operação é a mesma, calcular valores e/ou produzir efeitos colaterais a partir das entradas.

</div>
</div>


## Operações de arranjo dinâmico

Vamos reescrever o código da função `primo` considerando que o tipo `list` e suas operações não existam. \pause

Vamos considerar que queremos criar um novo tipo, chamado `ArranjoD` (arranjo dinâmico de inteiros), que tenha as mesmas quatro operações que identificamos, mas que use a forma de chamada de função.


## Operações de arranjo dinâmico

\scriptsize

```python
def primos(lim: int) -> list[int]:
    primos = []
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = []
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

\pause

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < arranjod_len(primos):
            if n % primos[i] == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

\pause

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < arranjod_len(primos):
            if n % arranjod_get(primos, i) == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            primos.append(n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

\pause

```python
def arranjod_get(a: ArranjoD, i: int) -> int:
    '''Devolve o elemento da posição *i* de *a*'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and \
              i < arranjod_len(primos):
            if n % arranjod_get(primos, i) == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            arranjod_acresceta(primos, n)

        n = n + 1
    return primos
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

```python
def arranjod_get(a: ArranjoD, i: int) -> int:
    '''Devolve o elemento da posição *i* de *a*'''
```

\pause

```python
def arranjod_acrescenta(a: ArranjoD, item: int):
    '''Acrescenta *item* no final *a*'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    '''
    Encontra todos os números primos
    menores que *lim*.

    Exemplos:
    >>> primos(2)
    []
    >>> primos(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    '''
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

```python
def arranjod_get(a: ArranjoD, i: int) -> int:
    '''Devolve o elemento da posição *i* de *a*'''
```

```python
def arranjod_acrescenta(a: ArranjoD, item: int):
    '''Acrescenta *item* no final *a*'''
```

</div>
</div>


## Operações de arranjo dinâmico

<div class="columns">
<div class="column" width="50%">

\scriptsize

```python
def primos(lim: int) -> ArranjoD:
    '''
    Encontra todos os números primos
    menores que *lim*.

    Exemplos:
    >>> a = primos(12)
    >>> arranjod_get(a, 0)
    2
    >>> arranjod_get(a, 1)
    3
    >>> arranjod_get(a, 2)
    5
    >>> arranjod_get(a, 3)
    7
    >>> arranjod_get(a, 4)
    11
    '''
```

</div>
<div class="column" width="50%">

\scriptsize

```python
@dataclass
class ArranjoD:
    ...
```

```python
def arranjod_vazio() -> ArranjoD:
    '''Cria um novo arranjo com zero elementos'''
```

```python
def arranjod_len(a: ArranjoD) -> int:
    '''Devolve a quantidade de elementos em *a*'''
```

```python
def arranjod_get(a: ArranjoD, i: int) -> int:
    '''Devolve o elemento da posição *i* de *a*'''
```

```python
def arranjod_acrescenta(a: ArranjoD, item: int):
    '''Acrescenta *item* no final *a*'''
```

</div>
</div>


## Atividade

Forme uma dupla e implemente a definição e operações do tipo `ArranjoD` e confira se a implementação funciona corretamente na função `primos`. \pause

Faça o download dos arquivos `array.pyc`, `arranjod.py` e `primos_arranjod.py` da página da disciplina.

-->
