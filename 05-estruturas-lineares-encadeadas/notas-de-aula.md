---
# vim: set spell spelllang=pt_br:
title: Estruturas de dados lineares
subtitle: Alocação encadeada
linkcolor: Black
urlcolor: Blue
# TODO: Use None para retorno de desempilha e desenfileira? Ou exercício?
# TODO: Falar exatamente o que o is e o is not fazem
# TODO: trocar os exemplos de lista de pessoas para exemplos de mulher com mãe, ou inscrito com quem indicou?
# TODO: adicionar discussão vantagens e desvantagens do uso de sentinela (ver o cormen)
# TODO: destacar operações de inserção e remoção do início/fim?
# TODO: destacar a necessidade de criar funções para facilitar os testes (str, str_fim_inicio)
---


## Introdução

Como podemos implementar os TAD's Pilha, Fila, Fila Dupla e Lista sem usar arranjos? \pause

Como podemos representar uma quantidade arbitrária de dados sem arranjos? \pause

É isso que vamos ver agora! \pause

Mas antes, vamos falar de valores opcionais.


## Valores opcionais

Queremos representar uma pessoa com um nome e uma idade, sendo que a idade é opcional. Também queremos fazer uma função `faz_aniversario` que aumenta a idade de uma pessoa, se a idade está presente, em 1 ano. \pause

\scriptsize

```python
@dataclass
class Pessoa:
    nome: str
    idade: int
```

\pause

\normalsize

Como representar a ausência da idade? \pause Uma opção é usar um valor inválido para a idade. \pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
>>> NENHUMA = -1
>>> p1 = Pessoa('Joao', 21)
>>> p2 = Pessoa('Maria', NENHUMA)
>>> p1
Pessoa(nome='Joao', idade=21)
>>> p2
Pessoa(nome='Maria', idade=-1)
```

\pause

</div>
<div class="column" width="48%">
Agora temos que projetar a função `faz_aniversario`.
</div>
</div>


## Valores opcionais

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
def faz_aniversario(p: Pessoa):
    '''
    Aumenta a idade da pessoa *p* em
    1 ano e a idade está presente.

    Exemplos
    >>> p1 = Pessoa('Joao', 21)
    >>> faz_aniversario(p1)
    >>> p1
    Pessoa(nome='Joao', idade=22)
    >>> p2 = Pessoa('Maria', NENHUMA)
    >>> faz_aniversario(p2)
    >>> p2
    Pessoa(nome='Maria', idade=-1)
    '''
```

\pause

```python
    if p.idade != NENHUMA:
        p.idade += 1
```

\pause

</div>
<div class="column" width="48%">

\small

Qual é o problema em usar `NENHUMA` para representar a ausência de idade? \pause

Sempre que precisamos da idade, temos que fazer uma verificação. \pause O que acontece se esquecermos de fazer a verificação? \pause No melhor dos casos, descobrimos o erro na fase de teste, \pause no pior caso, o programa geraria resultados incorretos para o usuário. \pause

Note que se a idade é opcional, sempre precisamos verificar se ele está presente ou não, a questão é como fazemos isso.

</div>
</div>


## Valores opcionais

O que permite o programar executar sem verificar se a idade está presente? \pause

O ponto é que estamos usando um valor do mesmo tipo para representar a ausência de valor, então, qualquer operação válida para os valores do tipo também é válida para o valor que representa a ausência de valor! \pause

Existe mais algum problema com essa estratégia? \pause

Sim, o leitor vê a definição `idade: int`{.python} e supõe que a idade é requerida, só entendendo que é opcional se isso estiver escrito como comentário. \pause

Podemos fazer melhor? \pause Sim!


## Valores opcionais

Em Python existe um valor especial chamado `None`{.python} (do tipo `None`{.python} -- sim, o tipo e o valor do tipo tem o mesmo nome!), que fica armazenado em uma célula de memória específica, que é usado para representar a ausência de um valor. \pause

Para que uma variável possa referenciar o valor `None`{.python}, é preciso informar isso na declaração do tipo da variável, por exemplo `a: int | None`{.python}. Está declaração está dizendo que variável `a` pode referenciar uma célula com um inteiro ou com `None`{.python}. \pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
>>> # a pode referenciar um inteiro ou None
>>> a: int | None = 20
>>> a
20
>>> a is None
False
>>> a is not None
True
```

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python

>>> a = None
>>> a
>>> # nada é exibido, None representa nada!
>>> a is None
True
>>> a is not None
False
```

</div>
</div>


## Valores opcionais

Note que é possível declarar uma variável apenas do tipo `None`{.python}, por exemplo `a: None`{.python}, mas isso não faz muito sentido pois o único valor válido para `a` seria `None`{.python}! \pause

\scriptsize

```python
>>> # a só pode referenciar o valor None!
>>> a: None = None
>>> a
```


## Valores opcionais

<div class="columns">
<div class="column" width="48%">
Como o uso do `None`{.python} muda o código? \pause

\scriptsize

```python
@dataclass
class Pessoa:
    nome: str
    idade: int | None
```

\normalsize

A intenção está clara, `idade` pode ser um inteiro ou `None`{.python}.

</div>
<div class="column" width="48%">

\pause

\scriptsize

```python
>>> p1 = Pessoa('Joao', 21)
>>> faz_aniversario(p1)
>>> p1
Pessoa(nome='Joao', idade=22)
>>> p2 = Pessoa('Maria', None)
>>> faz_aniversario(p2)
>>> p2
Pessoa(nome='Maria', idade=None)
```

\normalsize

Os exemplos também ficam mais claros.

</div>
</div>


## Valores opcionais

\scriptsize

```python
def faz_aniversario(p: Pessoa):
    if p.idade is not None:
        p.idade += 1
```

\pause

\normalsize

O que aconteceria se esquecêssemos de fazer a verificação sem a idade está presente? \pause

O `python` geraria um erro de execução:

\scriptsize

```
TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
```

\pause

\normalsize

O `mypy` iria gerar um erro:

\scriptsize

```
pessoa.py:23: error: Unsupported operand types for + ("None" and "int")  [operator]
pessoa.py:23: note: Left operand is of type "int | None"
Found 1 error in 1 file (checked 1 source file)
```


## Valores opcionais

O que ganhamos com isso? \pause

Antes era possível que o programa continuasse a execução mesmo se a verificação da idade, agora isso não é mais possível! \pause

Além disso, com o uso do `mypy`, podemos detectar o erro estaticamente, sem precisar executar o programa.


## Encadeamento

Vamos voltar a uma das questões iniciais. \pause

Como podemos representar uma quantidade arbitrária de dados sem arranjos? \pause

Suponha que queremos representar uma coleção de nomes de pessoas. \pause Podemos fazer isso usando estruturas. \pause A ideia é criar um **encadeamento** de instância de estruturas. \pause

A estrutura têm um nome de uma pessoa e uma referência para outra instância da mesma estrutura, que contém o nome da próxima pessoa e uma referência para outra instância da mesma estrutura...


## Encadeamento

\scriptsize

```python
from __future__ import annotations

@dataclass
class Seq:
    nome: str
    proximo: Seq
```

\pause

\normalsize

Como representar a coleção com os nomes "Joao", "Pedro" e "Ana"?

\pause

\scriptsize

```python
seq = Seq('Joao', Seq('Pedro', Seq('Ana', ...)))
```

\pause

\ \

![](imagens/seq-sem-fim.pdf)

\pause

\normalsize

O que está faltando? \pause Uma forma de encerrar a sequência! \pause Vamos tornar o próximo opcional usando `None`{.python}.


## Encadeamento

\scriptsize

```python
@dataclass
class Seq:
    nome: str
    proximo: Seq | None
```

\pause

\scriptsize

```python
>>> seq = Seq('Joao', Seq('Pedro', Seq('Ana', None)))
```

\pause

\ \

![](imagens/seq-com-fim.pdf)

\pause

\normalsize

Note que na representação gráfica podemos utilizar `/` para indicar uma referência para `None`{.python}. \pause

O que têm de diferente na declaração de `Seq` em relação as classes que definimos anteriormente? \pause  Uma **autorreferência**, ou seja, a utilização da classe em sua própria definição.


## Encadeamento

Os tipos com autorreferência (ou recursivos) permitem a representação de uma quantidade de dados arbitrárias pelo **encadeamento** de instâncias do tipo. \pause Usamos `None`{.python} para representar o fim do encadeamento. \pause

O tipo utilizado no encadeamento é comumente chamado de `No`, dessa forma, usamos um encadeamento de nós para criar uma coleção de valores. \pause

<div class="columns">
<div class="column" width="35%">
\scriptsize

```python
@dataclass
class No:
    item: int
    prox: No | None

```

</div>
<div class="column" width="65%">
\scriptsize

```python
>>> p = No('Joao', No('Pedro', No('Ana', None)))
```

</div>
</div>

\pause

\normalsize

\ \

Antes de prosseguirmos, vamos revisar o uso de múltiplas referências para a mesma célula de memória.


## Múltiplas referências

Vimos que em Python toda variável referencia uma célula de memória. Em algumas situações, como quando atribuímos uma variável para outra ou passamos uma variável como parâmetro, temos mais de uma variável referenciando a mesma célula de memória. \pause

Essa situação pode gerar alguns dificuldades para a escrita e entendimento do código, mas é necessária para manipulação de encadeamentos. \pause

Vamos usar o [Python Tutor](https://pythontutor.com/) para visualizar algumas situações de múltiplas referências. \pause

O Python Tutor não aceita o uso de `@dataclass`{.python}, então vamos definir uma classe "normal" e definir um construtor manualmente.


## Múltiplas referências

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
@dataclass
class Ponto:
    x: int
    y: int

@dataclass
class Retangulo:
    canto: Ponto
    largura: int
    altura: int
```

</div>
<div class="column" width="48%">
\scriptsize

```python
class Ponto:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, canto: Ponto,
                       largura: int,
                       altura: int):
        self.canto = canto
        self.largura = largura
        self.altura = altura
```
</div>
</div>

Acesse esse exemplos no [Python Tutor](https://pythontutor.com/render.html#code=class%20Ponto%3A%0A%20%20%20%20def%20__init__%28self,%20x%3A%20int,%20y%3A%20int%29%3A%0A%20%20%20%20%20%20%20%20self.x%20%3D%20x%0A%20%20%20%20%20%20%20%20self.y%20%3D%20y%0A%0Aclass%20Retangulo%3A%0A%20%20%20%20def%20__init__%28self,%20canto%3A%20Ponto,%20largura%3A%20int,%20altura%3A%20int%29%3A%0A%20%20%20%20%20%20%20%20self.canto%20%3D%20canto%0A%20%20%20%20%20%20%20%20self.largura%20%3D%20largura%0A%20%20%20%20%20%20%20%20self.altura%20%3D%20altura%0A%0Ap%20%3D%20Ponto%2810,%2050%29%0Al%20%3D%20200%0Aa%20%3D%20450%0A%0Ar1%20%3D%20Retangulo%28p,%20l,%20a%29%0Ar2%20%3D%20Retangulo%28p,%20l,%20a%29%0A%0A%23%20Quais%20valores%20ser%C3%A3o%20exibidos%3F%0Al%20%3D%20300%0Aprint%28r1.largura%29%0Aprint%28r2.largura%29%0A%0A%23%20Quais%20valores%20ser%C3%A3o%20exibidos%3F%0Ap.x%20%3D%2020%0Aprint%28r1.canto.x,%20r1.canto.y%29%0Aprint%28r2.canto.x,%20r2.canto.y%29%0A%0A%23%20Quais%20valores%20ser%C3%A3o%20exibidos%3F%0Ar1.canto.y%20%3D%2070%0Aprint%28p.x,%20p.y%29%0Aprint%28r2.canto.x,%20r2.canto.y%29%0A%0A%23%20Quais%20valores%20ser%C3%A3o%20exibidos%3F%0Ar2.canto%20%3D%20Ponto%283,%2017%29%0Aprint%28p.x,%20p.y%29%0Aprint%28r1.canto.x,%20r1.canto.y%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false).


## Múltiplas referências

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
class Ponto:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, canto: Ponto,
                       largura: int,
                       altura: int):
        self.canto = canto
        self.largura = largura
        self.altura = altura

p = Ponto(10, 50)
l = 200
a = 450

r1 = Retangulo(p, l, a)
r2 = Retangulo(p, l, a)
```

</div>
<div class="column" width="48%">

\scriptsize

```python
# Quais valores serão exibidos?
l = 300
print(r1.largura)
print(r2.largura)
```

\pause

```python
# Quais valores serão exibidos?
p.x = 20
print(r1.canto.x, r1.canto.y)
print(r2.canto.x, r2.canto.y)
```

\pause

```python
# Quais valores serão exibidos?
r1.canto.y = 70
print(p.x, p.y)
print(r2.canto.x, r2.canto.y)
```

\pause

```python
# Quais valores serão exibidos?
r2.canto = Ponto(3, 17)
print(p.x, p.y)
print(r1.canto.x, r1.canto.y)
```

</div>
</div>


## Manipulação de encadeamento

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
@dataclass
class No:
    item: int
    prox: No | None
```

\pause

\small

Defina uma variável `p` com um encadeamento de nós com os valores 10, 4, 1.

\pause

\scriptsize

```python
>>> p = No(10, No(4, No(1, None)))
```

\pause

\small

Escreva expressões para acessar o primeiro, o segundo e o terceiro item do encadeamento.

\pause

\scriptsize

```python
>>> p.item
10
>>> p.prox.item
4
>>> p.prox.prox.item
1
```

\pause

</div>
<div class="column" width="48%">

\small

Modifique o segundo item para 7.

\pause

\scriptsize

```python
>>> p.prox.item = 7
```

\pause

\small

Adicione um `No` com o item 2 no início.

\scriptsize

\pause

```python
>>> p = No(2, p)
```

\pause

\small

Adicione um `No` com o item 20 no final.

\scriptsize

\pause

```python
>>> p.prox.prox.prox.prox = No(20, None)
```

\pause

\small

Usando repetição!

\scriptsize

\pause

```python
>>> # q começa no início do encademaneto
>>> q = p
>>> # avançamos q enquanto podemos
>>> while q.prox is not None:
...     q = q.prox
>>> # agora q referencia o último nó
>>> q.prox = No(20, None)
```

</div>
</div>


## Implementação de pilha

<div class="columns">
<div class="column" width="48%">
Como podemos implementar uma pilha usando um encadeamento de nós? \pause

Usamos uma variável `topo` para armazenar o primeiro nó do encadeamento ou `None`{.python} se a pilha estiver vazia: \pause

- Construtor: \pause inicializa `topo` com `None`{.python} \pause
- Vazia: \pause verifica se `topo` é `None`{.python} \pause
- Empilha: \pause insere um novo nó com o item no início do encadeamento e muda `topo` para o novo início \pause
- Desempilha: \pause remove o primeiro nó do encadeamento e muda `topo` para o novo início \pause

</div>
<div class="column" width="48%">
\scriptsize

```python
class Pilha:
    topo: No | None

    def empilha(self, item: str):
        self.topo = No(item, self.topo)

    def desempilha(self) -> str:
        if self.topo is None:
            raise ValueError('pilha vazia')
        item = self.topo.item
        self.topo = self.topo.prox
        return item
```

\pause

\normalsize

Qual a complexidade de tempo de `empilha` e `desempilha`? \pause $O(1)$.

</div>
</div>


## Implementação de Fila

<div class="columns">
<div class="column" width="48%">
Como podemos implementar uma fila usando um encadeamento de nós? \pause

Usamos uma variável `inicio` para armazenar o primeiro nó do encadeamento ou `None`{.python} se a fila estiver vazia: \pause

- Construtor: \pause inicializa `inicio` com `None`{.python} \pause
- Vazia: \pause verifica se `inicio` é `None`{.python} \pause
- Enfileira: \pause insere um novo nó com o item no final do encadeamento \pause
- Desenfileira: \pause remove o primeiro nó do encadeamento e muda `inicio` para o novo início \pause

</div>
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    inicio: No | None

    def enfileira(self, item: str):
        if self.inicio is None:
            self.inicio = No(item, None)
        else:
            # Encontra o último nó
            p = self.inicio
            while p.prox is not None:
                p = p.prox
            # Coloca item após o último nó
            p.prox = No(item, None)

    def desenfileira(self) -> str:
        if self.inicio is None:
            raise ValueError('fila vazia')
        item = self.inicio.item
        self.inicio = self.inicio.prox
        return item
```

</div>
</div>


## Implementação de Fila

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    inicio: No | None

    def enfileira(self, item: str):
        if self.inicio is None:
            self.inicio = No(item, None)
        else:
            # Encontra o último nó
            p = self.inicio
            while p.prox is not None:
                p = p.prox
            # Coloca item após o último nó
            p.prox = No(item, None)

    def desenfileira(self) -> str:
        if self.inicio is None:
            raise ValueError('fila vazia')
        item = self.inicio.item
        self.inicio = self.inicio.prox
        return item
```

</div>
<div class="column" width="48%">

\pause

\normalsize

Qual a complexidade de tempo de `desenfileira`? \pause $O(1)$. \pause

Qual a complexidade de tempo de `enfileira`? \pause $O(n)$... \pause

Podemo fazer melhor? \pause Sim! \pause

Vamos manter uma variável `fim` que referencia o último nó do encadeamento ou é `None`{.python} se a fila estiver vazia. \pause Isso permite acessar o fim em tempo constante. \pause

Ambos `inicio` e `fim` são considerados em `enfileira` e `desenfileira`.

</div>
</div>


## Implementação de Fila

<div class="columns">
<div class="column" width="48%">
![](imagens/fila-simples.pdf){height=7.7cm}
\pause
</div>
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    inicio: No | None
    fim: No | None

    def enfileira(self, item: str):
        if self.fim is None:
            self.inicio = No(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = No(item, None)
            self.fim = self.fim.prox

    def desenfileira(self) -> str:
        if self.inicio is None:
            raise ValueError('fila vazia')
        item = self.inicio.item
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None
        return item
```
</div>
</div>

## Implementação de Fila

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
class Fila:
    inicio: No | None
    fim: No | None

    def enfileira(self, item: str):
        if self.fim is None:
            self.inicio = No(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = No(item, None)
            self.fim = self.fim.prox

    def desenfileira(self) -> str:
        if self.inicio is None:
            raise ValueError('fila vazia')
        item = self.inicio.item
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None
        return item
```

</div>
<div class="column" width="48%">

\pause

\normalsize

Qual a complexidade de tempo de `desenfileira`? \pause $O(1)$. \pause

Qual a complexidade de tempo de `enfileira`? \pause $O(1)$.

</div>
</div>


## Implementação de Fila Dupla

<div class="columns">
<div class="column" width="55%">
\small
Como podemos implementar uma fila dupla usando um encadeamento de nós? \pause

Precisamos implementar inserção e remoção nos dois extremos. \pause

Mantendo `inicio` e `fim`, quais são as complexidades de tempos das operações? \pause

Inserir no início: \pause $O(1)$ \pause (como `Pilha.empilha` -- atualiza `fim` se necessário) \pause

Remover do início: \pause $O(1)$ \pause (como `Fila.desenfileira`) \pause

Inserir no fim: \pause $O(1)$ \pause (como `Fila.enfileira`) \pause

Remover do fim: \pause $O(n)$! \pause É preciso localizar, a partir do início, o predecessor do fim no encadeamento. \pause

</div>
<div class="column" width="42%">
\scriptsize

```python
def remove_fim(self) -> str:
    if self.fim is None:
        raise ValueError('fila vazia')

    # Salva o último elemento
    item = self.fim.item

    p = self.inicio
    assert p is not None
    if p.prox is None: # Único elemento?
        self.inicio = None
        self.fim = None
    else:
        # Encontra o penúltimo
        while p.prox is not self.fim:
            p = p.prox
        p.prox = None
        self.fim = p
    # Devolve o item
    return item
```

</div>
</div>


## Implementação de Fila Dupla

Podemos fazer melhor? Ou seja, podemos fazer uma implementação em que a remoção do fim seja constante? \pause Sim! \pause

Precisamos de um encadeamento duplo. Cada nó mantém, além de uma referência opcional para o próximo, uma referência opcional para o nó anterior no encadeamento. \pause Dessa forma é possível encontrar o antecessor de um nó em tempo constante. \pause


\scriptsize

```python
@dataclass
class No:
    ante: No | None
    item: str
    prox: No | None
```


## Encadeamento duplo

Trabalhar com encadeamento duplo requer ainda mais cuidado do que com encadeamento simples! Por isso é importante **fazer desenhos**! \pause

Escreva o código para criar o seguinte encadeamento

![](imagens/encadeamento-duplo.pdf)

\pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
>>> a = No(None, 'A', None)
>>> b = No(None, 'B', None)
>>> c = No(None, 'C', None)
>>> a.prox = b
>>> b.ante = a
>>> b.prox = c
>>> c.prev = b
>>> p = a
```

\pause

</div>
<div class="column" width="48%">
Note que, como o encadeamento tem ciclos, ele não pode ser criado todo de uma vez. A estratégia que usamos foi criar os nós separados e depois ligá-los.
</div>
</div>


## Encadeamento duplo

Na hora de exibir um encadeamento com ciclos, o Python usa `...` para evitar exibir o mesmo nó mais que uma vez.

\scriptsize

```python
>>> p
No(ante=None, item='A', prox=No(ante=..., item='B', prox=No(ante=..., item='C', prox=None)))
>>> b
No(ante=No(ante=None, item='A', prox=...), item='B', prox=No(ante=..., item='C', prox=None))
>>> c
No(ante=No(ante=No(ante=None, item='A', prox=...), item='B', prox=...), item='C', prox=None)
```

\pause

\normalsize

Agora vamos implementar uma fila dupla usando encadeamento duplo e mantendo referências para o início e fim do encadeamento.


## Fila dupla -  Inserção e remoção no início (versão didática)

<div class="columns">
<div class="column" width="45%">

![](imagens/inicio-insercao-remocao.pdf)

\ \

O nó azul está sendo inserido/removido.

\pause

</div>
<div class="column" width="52%">
\scriptsize

```python
def insere_inicio(self, item: str):
    if self.inicio is None:
        self.inicio = No(None, item, None)
        self.fim = self.inicio
    else:
        self.inicio.ante = No(None, item, self.inicio)
        self.inicio = self.inicio.ante
```

\ \

\pause

```python
def remove_inicio(self) -> str:
    if self.inicio is None:
        raise ValueError('fila vazia')
    item = self.inicio.item
    # Só tem um nó?
    if self.inicio.prox is None:
        self.inicio = None
        self.fim = None
    else:
        self.inicio = self.inicio.prox
        self.inicio.ante = None
    return item
```

</div>
</div>


## Fila dupla -  Inserção e remoção no início (versão direta)

<div class="columns">
<div class="column" width="45%">

![](imagens/inicio-insercao-remocao.pdf)

\ \

O nó azul está sendo inserido/removido.

</div>
<div class="column" width="52%">
\scriptsize

```python
def insere_inicio(self, item: str):
    self.inicio = No(None, item, self.inicio)
    if self.inicio.prox is None:
        self.fim = self.inicio
    else:
        self.inicio.prox.ante = self.inicio
```

\ \

```python
def remove_inicio(self) -> str:
    if self.inicio is None:
        raise ValueError('fila vazia')

    item = self.inicio.item

    self.inicio = self.inicio.prox
    if self.inicio is None:
        self.fim = None
    else:
        self.inicio.ante = None

    return item
```

</div>
</div>


## Fila dupla -  Inserção e remoção no fim (versão didática)

<div class="columns">
<div class="column" width="45%">

![](imagens/fim-insercao-remocao.pdf)

\ \

O nó azul está sendo inserido/removido.

\pause

</div>
<div class="column" width="52%">

\scriptsize

```python
def insere_fim(self, item: str):
    if self.fim is None:
        self.inicio = No(None, item, None)
        self.fim = self.inicio
    else:
        self.fim.prox = No(self.fim, item, None)
        self.fim = self.fim.prox
```

\pause

\ \

```python
def remove_fim(self) -> str:
    if self.fim is None:
        raise ValueError('fila vazia')
    item = self.fim.item
    # Só tem um nó?
    if self.fim.ante is None:
        self.inicio = None
        self.fim = None
    else:
        self.fim = self.fim.ante
        self.fim.prox = None
    return item
```

</div>
</div>


## Fila dupla -  Inserção e remoção no fim (versão direta)

<div class="columns">
<div class="column" width="45%">

![](imagens/fim-insercao-remocao.pdf)

\ \

O nó azul está sendo inserido/removido.

</div>
<div class="column" width="52%">

\scriptsize

```python
def insere_fim(self, item: str):
    self.fim = No(self.fim, item, None)
    if self.fim.ante is None:
        self.inicio = self.fim
    else:
        self.fim.ante.prox = self.fim
```

\ \

```python
def remove_fim(self) -> str:
    if self.fim is None:
        raise ValueError('fila vazia')

    item = self.fim.item

    self.fim = self.fim.ante
    if self.fim is None:
        self.inicio = None
    else:
        self.fim.prox = None

    return item
```

</div>
</div>


## Fila dupla

Com encadeamento duplo e referência para início e fim, os métodos do TAD de fila dupla têm complexidade de tempo de $O(1)$. \pause

No entanto, \pause a implementação parece complicada, cada um dos quadro métodos tem dois casos distintos. \pause

Podemos simplificar o código? \pause O que faz com que seja necessário dois casos? \pause

Vamos supor por um momento que todos os nós tenham antecessor e sucessor. \pause

Como remover um nó `p` sabendo que existe um antecessor e um sucessor de `p`? \pause

Como inserir um nó `novo` após um nó `p` sabendo que `p` tem um sucessor? \pause

Como inserir um nó `novo` antes de um nó `p` sabendo que `p` tem um antecessor?


## Fila dupla

<div class="columns">
<div class="column" width="48%">

![](imagens/insercao-remocao.pdf)

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
# p é o nó azul
def remove(p: No):
    p.prox.ante = p.ante
    p.ante.prox = p.prox
```

\ \

\pause

```python
# p é o nó mais a esquerda
# novo é o nó azul
def insere_depois(p: No, novo: No):
    novo.ante = p
    novo.prox = p.prox
    p.prox.ante = novo
    p.prox = novo
```

\ \

\pause

```python
# p é o nó mais a direita
# novo é o no azul
def insere_antes(p: No, novo: No):
    novo.ante = p.ante
    novo.prox = p
    p.ante.prox = novo
    p.ante = novo
```

</div>
</div>


## Fila dupla

<div class="columns">
<div class="column" width="48%">

![](imagens/insercao-remocao.pdf)

\ \

\normalsize

Não precisamos de dois métodos para inserir!

\scriptsize

\ \

```python
def insere_antes(p: No, novo: No):
    insere_depois(p.ante, novo)
```

</div>
<div class="column" width="48%">

\scriptsize

```python
# p é o nó azul
def remove(p: No):
    p.prox.ante = p.ante
    p.ante.prox = p.prox
```

\ \

```python
# p é o nó mais a esquerda
# novo é o nó azul
def insere_depois(p: No, novo: No):
    novo.ante = p
    novo.prox = p.prox
    p.prox.ante = novo
    p.prox = novo
```

\ \

```python
# p é o nó mais a direita
# novo é o no azul
def insere_antes(p: No, novo: No):
    novo.ante = p.ante
    novo.prox = p
    p.ante.prox = novo
    p.ante = novo
```


</div>
</div>


## Sentinela

Como podemos fazer para que cada nó tenha um antecessor e um sucessor? \pause

Usamos uma **sentinela**, um nó especial, que é usando onde o valor `None`{.python} seria usado normalmente. Ou seja, a sentinela fica entre o primeiro e o último nó do encadeamento. \pause

O resultado é comumente chamado de **lista circular duplamente encadeada com sentinela**! \pause Na figura abaixo `L` é o `self` e a sentinela é o `nil`. \pause

![](imagens/Fig-10-4.pdf){width=11cm}


## Fila Dupla com sentinela

<div class="columns">
<div class="column" width="48%">
\small

Como implementar o TAD de fila dupla com esse esquema? \pause

Nesse esquema o `ante` e o `prox` não podem ser `None`{.python}, então precisamos mudar a definição de `No`: \pause

\scriptsize

\ \

```python
@dataclass
class No:
    ante: No
    item: str
    prox: No
```

\pause

</div>
<div class="column" width="48%">

\small

Mas isso cria um problema, que é a impossibilidade de instanciar um `No`! \pause Conforme discutimos em sala, vamos usar uma inicialização em duas etapas, na primeira um `No` é criado com valores temporários `None`{.python} para `ante` e `prox` (usamos `# type: ignore`{.python} para que o `mypy` não indique o erro) e depois mudamos para os valores corretos.

\pause

</div>
</div>

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
    def __init__(self, item: str) -> None:
        # Após a criação de um nó temos a
        # responsabilidade de alterar ante e
        # prox para valores válidos!
        self.ante = None # type: ignore
        self.item = item
        self.prox = None # type: ignore
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python
class FilaDupla:
    sentinela: No
    def __init__(self) -> None:
        self.sentinela = No('')
        self.sentinela.ante = self.sentinela
        self.sentinela.prox = self.sentinela
```
</div>
</div>


## Fila Dupla com sentinela

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def remove(p: No) -> str:
    '''Remove *p* do seu encademaneto
       e devolve o item em *p*.'''
    p.prox.ante = p.ante
    p.ante.prox = p.prox
    return p.item
```

\ \

```python
def insere_depois(p: No, novo: No):
    '''Insere *novo* após *p* no
       encademaneto.'''
    novo.ante = p
    novo.prox = p.prox
    p.prox.ante = novo
    p.prox = novo
```

\ \

\small

Tendo as funções auxiliares de inserção e remoção de um nó, como podemos implementar inserção e remoção do início e fim de uma fila com sentinela?

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
class FilaDupla:
    sentinela: No
    def __init__(self) -> None:
        self.sentinela = No('')
        self.sentinela.ante = self.sentinela
        self.sentinela.prox = self.sentinela
    def vazia(self) -> bool:
        return self.sentinela.prox is self.sentinela
```

\pause

```python
    def insere_inicio(self, item: str):
```

\pause

```python
        insere_depois(self.sentinela, No(item))
```

\pause

```python
    def remove_inicio(self) -> str:
```

\pause

```python
        assert not self.vazia()
        return remove(self.sentinela.prox)
```

\pause

```python
    def insere_fim(self, item: str):
```

\pause

```python
        insere_depois(self.sentinela.ante, No(item))
```

\pause

```python
    def remove_fim(self) -> str:
```

\pause

```python
        assert not self.vazia()
        return remove(self.sentinela.ante)
```


</div>
</div>


## Lista

Como implementar o TAD Lista utilizando encadeamento? \pause

Devemos usar encadeamento simples ou duplo para implementar o TAD Lista? \pause

Se o TAD de Lista não define função específica para remoção do fim, então o encadeamento simples é suficiente. \pause

Qual o tempo de execução para operações de inserção e remoção em posição? \pause $O(n)$, pois é preciso seguir o encadeamento até a posição especificada, que pode ser a última. \pause

A implementação do TAD Lista fica como exercício!


## Revisão

Vimos quatro TAD's e como implementá-los usando arranjos (alocação contígua) e encadeamento de nós (alocação encadeada)

- Pilha
- Fila
- Fila Dupla
- Lista


## Revisão

Estrutura / Operação   | get/set | ins/rem início | ins/rem fim    | ins/rem       | busca |
-------------------------|---------|----------------|----------------|---------------|-------|
Encadeamento Simples   |  $O(n)$ | $O(1)$ / $O(1)$ | $O(1)$ / $O(n)$ | $O(n)$      | $O(n)$ |
Encadeamento Duplo     |  $O(n)$ | $O(1)$ / $O(1)$ | $O(1)$ / $O(1)$ | $O(n)$ -- $O(1)$ [^1] | $O(n)$ |
Arranjo Dinâmico       |  $O(1)$ | $O(n)$ / $O(n)$ | $O(1)$[^2] / $O(1)$ | $O(n)$  | $O(n)$ |

[^1]: Com a referência para o nó
[^2]: Amortizado


## Alocação contígua versus encadeada


| Característica            | Contígua                  | Encadeada
|---------------------------|---------------------------|---------------------------
| Implementação             | Simples                   | Elaborada
| Aumento                   | Realocação                | Criação de nó
| Diminuição                | Deslocamento / realocação | Remoção de nó
| Acesso aleatório          | Sim                       | Não


## Referências

Capítulo 7, 8, 9 - Pilhas, filas e listas - Fundamentos de Python: Estruturas de dados. Kenneth A. Lambert. (Disponível na [Minha Biblioteca da UEM](https://dliportal.zbra.com.br/Login.aspx?key=UEM))

Seção 10.2 - Listas ligadas - Algoritmos: Teoria e Prática, 3a. edição, Cormen, T. at all.

Capítulo 3 - Linked Lists - [Open Data Structures](https://opendatastructures.org/ods-python.pdf).
