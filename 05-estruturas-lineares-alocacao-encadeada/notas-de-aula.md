---
# vim: set spell spelllang=pt_br:
title: Estruturas de dados lineares
subtitle: Alocação encadeada
linkcolor: Black
urlcolor: Blue
---


## Introdução

Como podemos implementar os TAD's Pilha, Fila, Fila Dupla e Lista sem usar arranjos? \pause

Como podemos representar coleções de dados sem usar arranjos? \pause

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
<div class="column" width="40%">
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
<div class="column" width="58%">

\small

O que aconteceria se esquecêssemos de fazer a verificação se a idade está presente? \pause O teste iria falhar... \pause

E se não tivéssemos teste? \pause O programa executaria mas produziria resultados incorretos. \pause

Esse tipo de erro só é possível porque estamos usando um valor do mesmo tipo para representar a ausência de valor, então, qualquer operação válida para os valores do tipo também é válida para o valor que representa a ausência de valor! \pause

Note também que o leitor vê a definição `idade: int`{.python} e supõe que a idade é requerida, só entendendo que é opcional se isso estiver escrito como comentário. \pause

Podemos fazer melhor? \pause Sim!
</div>
</div>


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

Vamos voltar a questão inicial: como representar uma coleção de valores sem utilizar arranjos? \pause

Suponha que queremos representar uma coleção de nomes de pessoas. \pause Podemos fazer isso usando estruturas. \pause A ideia é criar uma estrutura com um nome de uma pessoa e uma referência para outra instância da mesma estrutura, que conterá o nome da próxima pessoa e uma referência para outra instância da mesma estrutura...

\pause

<div class="columns">
<div class="column" width="48%">
\scriptsize

```python
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

\scriptsize

```python
@dataclass
class Seq:
    nome: str
    proximo: Seq | None
```

\pause

```python
>>> # Queremos representar a coleção
>>> # com os nomes 'Joao', 'Pedro' e 'Ana'.
>>> seq = Seq('Joao', Seq('Pedro', Seq('Ana', None)))
```
