---
# vim: set spell spelllang=pt_br:
title: Estruturas de dados lineares
subtitle: Alocação encadeada
linkcolor: Black
urlcolor: Blue
# TODO: trocar os exemplos de lista de pessoas para exemplos de mulher com mãe, ou inscrito com quem indicou
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
    Se a idade está presente, aumenta
    a idade da pessoa *p* em 1 ano.

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

O que aconteceria se esquecêssemos de fazer a verificação se a idade está presente? \pause O teste iria falhar... \pause

E se não tivéssemos teste? \pause O programa executaria mas produziria resultados incorretos.
</div>
</div>


## Valores opcionais

Porque esse erro possível? \pause

Esse tipo de erro só é possível porque estamos usando um valor do mesmo tipo para representar a ausência de valor, então, qualquer operação válida para os valores do tipo também é válida para o valor que representa a ausência de valor! \pause

Existe mais algum problema com essa estratégia? \pause

Sim, o leitor vê a definição `idade: int`{.python} e supõe que a idade é requerida, só entendendo que é opcional se isso estiver escrito como comentário. \pause

Podemos fazer melhor? \pause Sim!


## Valores opcionais

Em Python existe um valor especial chamado `None`{.python} (do tipo `None`{.python} -- sim, o tipo e o valor do tipo tem o mesmo nome!), que fica armazenado em uma célula de memória específica, que é usado para representar a ausência de um valor. \pause

Para que uma variável possa referenciar o valor `None`{.python}, é preciso informar isso na declaração do tipo da variável, por exemplo `a: int | None`{.python}. Está declaração está dizendo que variável `a` pode referenciar uma célula com um inteiro ou com `None`{.python}. \pause

Note que é possível declarar uma variável apenas do tipo `None`{.python}, por exemplo `a: None`{.python}, mas isso não faz muito sentido pois o único valor válido para `a` seria `None`{.python}! \pause

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
>>> # a pode referenciar um inteiro ou None
>>> a: int | None = 20
>>> a
20
>>> a = None
>>> a
```

</div>
<div class="column" width="48%">
\scriptsize

```python
>>> a = 30
>>> a
30
>>> # b só pode referenciar o valor None!
>>> b: None = None
>>> b
```

</div>
</div>


## Valores opcionais

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


## Valores opcionais

\scriptsize

```python
def faz_aniversario(p: Pessoa):
    if p.idade is not None:
        p.idade += 1
```

\pause

\normalsize

O que aconteceria se esquecêssemos de fazer a verificação se a idade está presente? \pause

O `mypy` iria gerar um erro:

\scriptsize

```
pessoa.py:23: error: Unsupported operand types for + ("None" and "int")  [operator]
pessoa.py:23: note: Left operand is of type "int | None"
Found 1 error in 1 file (checked 1 source file)
```

\pause

\normalsize

O que ganhamos com isso? \pause

Antes era possível cometer um erro incrementando a idade quando ela não estivesse presente, agora isso não é mais possível! Além disso, a detecção do erro acontece de forma estática, sem precisar executar o programa (como é feito nos testes).

</div>
</div>


## Encadeamento

Como podemos representar uma quantidade arbitrária de dados sem arranjos? \pause

Suponha que queremos representar uma coleção de nomes de pessoas. \pause Podemos fazer isso usando estruturas. \pause A ideia é criar uma estrutura com um nome de uma pessoa e uma referência para outra instância da mesma estrutura, que conterá o nome da próxima pessoa e uma referência para outra instância da mesma estrutura...

\pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
from __future__ import annotations
@dataclass
class Seq:
    nome: str
    proximo: Seq
```

\pause

```python
>>> # Queremos representar a coleção
>>> # com os nomes 'Joao', 'Pedro' e 'Ana'.
>>> seq = Seq('Joao', Seq('Pedro', Seq('Ana', ...)))
```

</div>
<div class="column" width="48%">
![](imagens/seq-sem-fim.pdf)
</div>
</div>

\pause

O que está faltando? \pause Uma forma de encerrar a sequência!


## Encadeamento

<div class="columns">
<div class="column" width="35%">
\scriptsize

```python
@dataclass
class Seq:
    nome: str
    proximo: Seq | None
```

</div>
<div class="column" width="60%">

\pause

\scriptsize

```python
>>> # Queremos representar a coleção
>>> # com os nomes 'Joao', 'Pedro' e 'Ana'.
>>> seq = Seq('Joao', Seq('Pedro', Seq('Ana', None)))
```

</div>
</div>

\pause

\ 

Na representação gráfica podemos utilizar `/` para indicar uma referência para `None`{.python}

\ 

![](imagens/seq-com-fim.pdf)


\pause

O que têm de diferente na declaração de `Seq` em relação as classes que definimos anteriormente? \pause  Uma **autorreferência**, ou seja, a utilização da classe em sua própria definição.


## Encadeamento

Os tipos com autorreferência (ou recursivos) permitem a representação de quantidade de dados arbitrárias pelo **encadeamento** de instâncias do tipo. \pause Usamos `None`{.python} para representar o fim do encadeamento. \pause

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

\normalsize

Usando repetição!

\scriptsize

\pause

```python
>>> q = p
>>> while q.prox is not None:
...     q = q.prox
>>> q.prox = No(20, None)
```

</div>
</div>


## Implementação de pilha

<div class="columns">
<div class="column" width="48%">
Como podemos implementar uma pilha usando um encadeamento de nós? \pause

Usamos uma variável `topo` para armazenar o primeiro nó do encadeamento ou `None`{.python} se a pilha estiver vazia: \pause

- Construtor: inicializa `topo` com `None`{.python} \pause
- Vazia: verifica se `topo` é `None`{.python} \pause
- Empilha: insere um novo nó com o item no início do encadeamento e muda `topo` para o novo início \pause
- Desempilha: remove o primeiro nó do encadeamento e muda `topo` para o novo início \pause

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

- Construtor: inicializa `inicio` com `None`{.python} \pause
- Vazia: verifica se `inicio` é `None`{.python} \pause
- Enfileira: insere um novo nó com o item no final do encadeamento \pause
- Desenfileira: remove o primeiro nó do encadeamento e muda `inicio` para o novo início \pause

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
![](imagens/fila-simples.pdf){height=7cm}
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

Inserir no início: \pause $O(1)$ \pause (como `Pilha.empiha` -- atualiza `fim` se necessário) \pause

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

Podemos fazer melhor? Ou seja, podemo fazer uma implementação que a remoção do fim seja constante? \pause Sim! \pause

Precisamos de um encadeamento duplo. Cada nó mantém, além de uma referência opcional para o próximo,também uma referência opcional para o nó anterior no encadeamento. \pause

\scriptsize

```python
class No:
    prox: No | None
    item: str
    ante: No | None
```
