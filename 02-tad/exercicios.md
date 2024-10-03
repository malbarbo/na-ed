---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Estrutura de dados
       | Tipos abstratos de dados
numbersections: false
urlcolor: Blue
---

O código inicial dos exercícios está disponível na página <https://malbarbo.pro.br/ensino/2024/6884/>.

## Começando

@) O que é um tipo concreto de dado?

@) O que é um tipo abstrato de dado?

@) O tipo `int` do Python é um TAD? Explique.

@) Qual é a diferença na forma que TAD é manipulado por que implementa e por quem usa o TAD?

@) Qual são as vantagens e desvantagens dos TAD's?

@) Como definimos TAD's em Python?

@) O que é um construtor?


## Praticando

@) Considere o TAD `Contador` especificado no arquivo `contador_tad.py` e:

    a) Faça uma cópia do arquivo `contador_tad.py` chamada `contador_int.py` e implemente o TAD usando um inteiro para armazenar o valor do contador.

    a) Faça uma cópia do arquivo `contador_tad.py` chamada `contador_alt.py` e implemente o TAD usando uma representação interna diferente da do exercício anterior, não use operações aritméticas na implementação.

    a) Compare as duas implementações e discuta qual é a mais adequada.


@) Considere o TAD `Dias` especificado no arquivo `dias_tad.py` e:

    a) Faça uma cópia do arquivo `dias_tad.py` chamada `dias_bools.py` e implemente o TAD usando 7 campos booleanos, cada um indicado se um dia está no conjunto de dias ou não.

    a) Faça uma cópia do arquivo `dias_tad.py` chamada `dias_alt.py` e implemente o TAD usando uma representação interna diferente da do exercício anterior.

    a) Compare as duas implementações e discuta qual é a mais adequada.


@) Considere o TAD `Selecao` especificado no arquivo `selecao_tad.py` e:

    a) Faça uma cópia do arquivo `selecao_tad.py` chamada `selecao_inicio_fim.py` e implemente o TAD usando três campos: a célula inicial, o início e o fim do intervalo.

    a) Faça uma cópia do arquivo `selecao_tad.py` chamada `selecao_alt.py` e implemente o TAD usando uma representação interna diferente da do exercício anterior.

    a) Compare as duas implementações e discuta qual é a mais adequada.


## Avançando

@) Seu amigo disse que não é possível implementar a classe `Robo` de forma diferente da que vimos em sala. Mostre que ele está errado fazendo uma implementação que usa apenas um campo do tipo string que armazena a info (nome seguido da posição entre parênteses) do robô. Crie uma cópia do arquivo `robo_tad.py` chamada `robo_info.py` e escreva a implementação nesse novo arquivo. Compare essa implementação coma feita em sala e discuta qual é a mais adequada.

@) Em alguns empresas é comum o uso de um banco de horas, que é um esquema de compensação de horas extras. Quando um funcionário trabalha além da sua jornada normal, as horas e minutos extras trabalhados são "depositados" em um banco de horas. Posteriormente o funcionário pode usar o saldo no banco de horas para se ausentar do trabalho.

    a) Projete um TAD `BancoHoras` com operações para depósito de horas e minutos, "saque" de horas e minutos (o saldo deve ser suficiente) e consulta de saldo (que deve gerar uma string no formato HH:MM). Em qualquer operação a quantidade de minutos não podem ser maior que 60.

    a) Faça uma implementação do TAD usando um campo para armazenar o saldo em minutos.

    a) Faça uma implementação do TAD usando dois campos, uma para horas e outro para minutos.

    a) Compare as duas implementações e discuta qual é a mais adequada.
