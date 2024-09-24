---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Estrutura de dados
       | Revisão de fundamentos de algoritmos
numbersections: false
urlcolor: Blue
---

# Conceitos básicos

@) Veja o material sobre conceitos básicos na página \url{https://malbarbo.pro.br/ensino/2024/6879/}. Instale o Python, o mypy e o vscode conforme os passos a seguir e teste os exemplos do material.

    a) Faça o download e instale a última versão do [Python](https://www.python.org/). Se você estiver usando o Windows marque a opção "Add python.exe to PATH" na janela inicial de instalação.

    a) Abra o Idle (ambiente de desenvolvimento que é instalado junto com o Python), crie um novo arquivo (File $\rightarrow$ New File), digite o programa abaixo e salve o arquivo (File $\rightarrow$ Save) com o nome `quadrado.py` (crie um diretório C:\\projetos e salve o arquivo dentro dele).

        ```python
        def quadrado(x: int) -> int:
            '''
            Calcula o quadrado de *x*.
            Exemplos
            >>> quadrado(3)
            9
            >>> quadrado(-2)
            4
            '''
            return x * x
        ```

        Execute o arquivo (Run $\rightarrow$ Run Module) e teste a função na janela de interações:

        ```python
        >>> quadrado(3)
        9
        >>> quadrado(-2)
        4
        ```

    a) Verifique se o Python foi adicionado corretamente no PATH abrindo o terminal de comandos (cmd ou PowerShell) e digitando o comando `python` (seguido do enter). Você deve ver o _prompt_ `>>>`. Digite `exit()`.

    a) Mude para o diretório onde o arquivo `quadrado.py` foi salvo com o comando `cd c:\projetos`. Execute os exemplos com o comando `python -m doctest -v quadrado.py`.

    a) Instale o mypy com o comando `pip install mypy`.

    a) Verifique se o mypy foi instalado corretamente com o comando `mypy quadrado.py`.

    a) Instale o [Visual Studio Code](https://code.visualstudio.com/). Inicie o vscode e abra o diretório `c:\projetos`. Instale a extensão de suporte ao Python (o vscode deve sugerir isso).


\LARGE Para todos os programas que você escrever, execute o `mypy` e o `doctest`!

\LARGE Veja a solução de alguns exercícios na página da disciplina (os nomes dos arquivos estão no final desse documento).

\normalsize

\newpage


# Projeto de programas / Prática

**Veja o material** na página \url{https://malbarbo.pro.br/ensino/2024/6879/}.

@) Implemente a função de acordo com a especificação a seguir. Corrija a especificação se necessário.

    ```python
    def isento_tarifa(idade: int) -> bool:
        '''
        Produz True se uma pessoa de *idade* anos é isento da tarifa de transporte
        público, isto é, tem menos que 18 anos ou 65 ou mais. Produz False caso
        contrário.

        Exemplos
        >>> isento_tarifa(17)
        True
        >>> isento_tarifa(18)
        True
        >>> isento_tarifa(50)
        False
        >>> isento_tarifa(65)
        True
        >>> isento_tarifa(70)
        True
        '''
        return False
    ```

@) Escreva os exemplos e implemente a função de acordo com a assinatura e o propósito a seguir.

    ```python
    def dma_para_amd(data: str) -> str:
        '''
        Transforma *data*, que deve estar no formato "dia/mes/ano",
        onde dia e mes tem dois dígitos e ano tem quatro dígitos,
        para o formato "ano/mes/dia".
        '''
        return ''
    ```


# Projeto de programas / Problemas

@) Você está fazendo um programa e precisa verificar se um texto digitado pelo usuário está de acordo com algumas regras. A regra “sem espaços extras” requer que o texto não comece e não termine com espaços. Projete uma função que verifique se um texto qualquer está de acordo com a regra “sem espaços extras”.


# Seleção / Prática

**Veja o material** na página \url{https://malbarbo.pro.br/ensino/2024/6879/}.

@) Projete uma função que determine o sinal de um número, produzindo `-1`{.python} para valores negativos, `1`{.python} para valores positivos e `0`{.python} para o `0`{.python}.

@) Projete uma função que transforme uma string para que ela tenha uma quantidade $n$ caracteres. Se a string tem mais caracteres que $n$, os caracteres excedentes do final devem ser removidos. Se a string tem menos caracteres que $n$, espaços em branco deve ser adicionados no final.


# Seleção / Problemas

@) Cada cidadão de um país, cuja moeda chama dinheiro, tem que pagar imposto sobre a sua renda. Cidadãos que recebem até 1000 dinheiros pagam 5% de imposto. Cidadãos que recebem entre 1000 e 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros e 10% sobre o que passar de 1000. Cidadãos que recebem mais do 5000 dinheiros pagam 5% de imposto sobre 1000 dinheiros, 10% de imposto sobre 4000 dinheiros e 20% sobre o que passar de 5000. Projete uma função que calcule o imposto que um cidadão deve pagar dado a sua renda.

@) Em um determinado jogo os jogadores são classificados em níveis de 0 a 25 e este nível é atualizado semanalmente baseado na quantidade de horas que o jogador jogou o jogo. Os jogadores que jogaram entre 4 e 5 horas permanecem no mesmo nível. Os jogadores que jogaram menos que 4 horas diminuem um nível a cada 1 hora que faltou para alcançar as 4 horas. Os jogadores que jogaram mais de 5 horas aumentam um nível a cada hora jogada além das 5 horas respeitando o limite máximo de 7 níveis. Projete uma função que recebe o nível atual do jogador e a quantidade de horas jogadas em uma semana e calcule o novo nível do jogador.


# Enumeração e estrutura / Prática

**Veja o material** na página \url{https://malbarbo.pro.br/ensino/2024/6879/}.

@) Projete uma enumeração para representar as direções norte, leste, sul e oeste. Em seguida,

    a) Projete uma função que indique a direção oposta de uma direção.

    a) Projete uma função que indique qual é direção que está a 90 graus no sentido horário de outra direção.

    a) Projete uma função que indique qual é direção que está a 90 graus no sentido anti-horário de outra direção. Use a função do item b para fazer a implementação (não use seleção nem operações aritméticas nessa implementação).

@) Projete um estrutura para representar uma data com dia, ano e mês. Em seguida

    a) Projete uma função que verifique se uma data é o último dia do ano.

    a) Projete uma função que receba duas datas e produza verdadeiro se a primeira vem antes que a segunda.


# Enumeração e estrutura / Problemas

@) O Brasil institui há algum tempo um sistema de bandeira tarifária para sinalizar ao consumidores os custos reais de geração de energia. Nesse sistema, a bandeira verde indica condições favoráveis de geração de energia e a tarifa não sofre acréscimo. Já a bandeira amarela indica condições menor favoráveis e por isso a tarifa sofre um acréscimo de R$ 0,01874 para cada quilowatt-hora. A bandeira vermelha - patamar 1 indica condições mais custosas de geração e o acréscimo na tarifa é de R$ 0,03971 para cada quilowatt-hora consumido. Por fim, a bandeira vermelha - patamar 2 indica condições ainda mais custosas e o acréscimo na tarifa é de R$ 0,09492 para cada quilowatt-hora consumido. Projete uma função que determine o valor final que o consumidor tem que pagar dado o seu consumo em quilowatt-hora, a tarifa básica do quilowatt-hora e a bandeira tarifária.

@) O desempenho de um time de futebol em um determinado campeonato é dado pelo número de pontos, número   de vitórias e saldo de gols (diferenças entre todos os gols marcados e sofridos), nessa ordem. Caso dois times empatem nesse critérios, a ordem alfabética dos nomes é usado para desempate.

    a) Projete uma função que determine qual de dois times tem o melhor desempenho.

    b) Considerando que cada jogo ganho pelo time dá 3 pontos e empate 1 ponto, projete uma função que atualize o desempenho de um time dado o resultado de um jogo.

@) Considere um jogo onde o personagem está em um tabuleiro (semelhante a um tabuleiro de jogo de xadrez). As linhas e colunas do tabuleiro são enumeradas de 1 a 10, dessa forma, é possível representar a posição (casa) do personagem pelo número da linha e da coluna que ele se encontra. O personagem fica virado para uma das direções: norte, sul, leste ou oeste. O jogador pode avançar o seu personagem qualquer número de casas na direção que ele está virado, mas é claro, não pode sair do tabuleiro. Projete uma função que indique a partir das informações do personagem, qual é o número máximo de casas que ele pode avançar na direção que ele está virado.


# Arranjos / Prática

**Veja o material** na página \url{https://malbarbo.pro.br/ensino/2024/6879/}.

@) Projete uma função que concatene todos os elementos de uma lista de strings.

@) Projete uma função que conte quantas vezes o valor mínimo de uma lista de inteiros não vazia aparece na lista.

    a) Esboce uma solução em duas etapas e depois implemente a função.

    a) Faça uma implementação alternativa que use apenas uma repetição.

    a) Avalie qual das implementações é mais simples.

@) Projete uma função que receba como entrada uma lista `lst` de números e crie uma nova lista colocando os valores negativos de `lst` antes dos positivos.

@) Projete uma função que encontre as posições de todas as ocorrências de um nome em uma lista de nomes.

@) Projete uma função que receba como entrada uma lista de números, uma posição $i$ e um número $n$ e devolva uma nova lista com $n$ adicionado na posição $i$ da lista de entrada.

    a) Esboce uma solução em três etapas e depois implemente a função (não use operações de sublista).

    a) Faça uma implementação alternativa que use apenas uma repetição (não use operações de sublista).

    a) Faça uma implementação que use operações de sublista e não use repetição.

    a) Avalia e classifique as implementações em ordem de simples.


# Arranjos / Problemas

@) A Láurea Acadêmica é uma homenagem prestada a alunos que tiveram elevado nível de aproveitamento no curso de graduação. Na UEM, todos os alunos que tiveram mais do que 2/3 das notas finais das disciplinas maiores do que 9,0 recebem esta homenagem. Projete um programa que receba as notas finais de um aluno e determine se ele receberá a Láurea Acadêmica.

@) Você acaba de ser contratado por um empresa que está desenvolvendo um sistema de gerenciamento de campeonatos amadores de futebol. A sua primeira tarefa é projetar uma função que calcule o desempenho de um time, que consiste no número de pontos, número de vitórias e saldo de gols (diferenças entre os gols feitos e sofridos) de um time a partir dos resultados das partitas que ele jogou. Cada vitória gera três pontos e cada empate um ponto. Por exemplo, se os resultados para um determinado time foram $5 \times 1$, $0 \times 2$ e $1 \times 1$, onde o primeiro número são os gols feitos e o segundo os gols sofridos, então o time fez 4 pontos, obteve 1 vitória e saldo de gols de 2.

@) Uma eleição é realizada com apenas dois candidatos. Cada eleitor pode votar ou no primeiro candidato, ou no segundo candidato, ou ainda, votar em branco. O candidato que tiver mais votos ganha a eleição. Se os votos em branco forem mais do que 50% do total de votos, novas eleições devem ser convocadas. Projete uma função que receba como entrada uma lista não vazia de votos e determine qual foi o resultado da eleição. Dica: projete uma função auxilar que conte votos de um tipo especificado por parâmetro.


# Repetição com "enquanto" / Prática

**Veja o material** na página \url{https://malbarbo.pro.br/ensino/2024/6879/}.

@) Projete uma função que verifique se uma lista de número é dobrada, isto é, pode ser obtida pela concatenação de duas listas iguais (não use operações de sublista).

@) Projete uma função que determine qual é a menor quantidade de elementos de uma lista que precisam ser somados (a partir do início da lista) para que a soma seja maior que um dado valor. Se não for possível atingir a soma desejada, a função deve devolver -1.


# Repetição com "enquanto" / Problemas

@) A empresa que você trabalha sofreu um falta de energia e agora é preciso recuperar os dados do backup. O primeiro passo é determinar o código dos clientes afetados. Em um primeiro momento foi obtido um arquivo (string) com o código de todos os clientes separados por vírgula. O seu trabalho agora é projetar uma função que gere uma lista dos códigos a partir dessa string. Por exemplo, para a string `"512,12,145"`{.python} a sua função deve gerar como resposta a lista `[512, 12, 145]`{.python}. Dica: você pode usar a expressão `c in s`{.python} para verificar se a string `c` está em `s` e o método `s.index(c)`{.python} para encontrar o índice da primeira ocorrência da string `c` em `s`.

@) Em um determinado jogo de construção de itens, cada item tem uma classe que varia de 1 a 10. Os item de classe 1 surgem conforme o jogador explorar os baús. Um item de classe 2 ou superior precisa ser construídos unindo dois itens da classe anterior. Por exemplo, para construir um item de classe 2 é necessário unir dois item de classe 1. Para construir um item de classe 10 é necessário unir dois item de classe 9. Projete uma função que receba como entrada um número $n$ (de 1 a 10), e determine quantos itens de classe 1 são necessário para construir um item de classe $n$. Suponha que a únicas operações aritméticas disponíveis seja a soma e a multiplicação.


# Memória e passagem de parâmetros / Prática

**Veja o material** na página \url{https://malbarbo.pro.br/ensino/2024/6879/}.

@) Projete uma função que receba como parâmetros uma lista e um índice `i` e modifique a lista removendo o elemento do índice `i`.

    ```python
    >>> lst = [7, 1, 8, 9]
    >>> remove_indice(lst, 2);
    >>> lst
    [7, 1, 9]
    # Escreva mais exemplos!
    ```

    Dica: mova o elemento do índice `i` até o final e depois use `list.pop`{.python} para removê-lo. A função `list.pop`{.python} funciona da seguinte forma

    ```python
    >>> lst = [3, 9, 1, 2]
    >>> lst.pop()
    2
    >>> lst
    [3, 9, 1]
    ```

@) Ordenação por seleção é um algoritmo para ordenar uma lista de valores. A ideia do algoritmo é selecionar um valor mínimo da lista a partir da posição 0 e colocá-lo na posição 0, depois encontrar um valor mínimo da lista a partir da posição 1 e colocá-lo na posição 1, depois encontrar um valor mínimo da lista a partir da posição 2 ... e assim por diante. Por exemplo, vamos considerar a lista `[8, 5, 4, 1, 2]`{.python}.

    O valor mínimo a partir da posição 0 é 1 (que está no índice 3), colocando 1 na posição 0, obtemos `[1, 5, 4, 8, 2]`{.python}.

    O valor mínimo a partir da posição 1 é 2 (que está no índice 4), colocando 2 na posição 1, obtemos `[1, 2, 4, 8, 5]`{.python}.

    O valor mínimo a partir da posição 2 é 4 (que está no índice 2), colocando 4 na posição 2, obtemos `[1, 2, 4, 8, 5]`{.python}.

    O valor mínimo a partir da posição 3 é 5 (que está no índice 4), colocando 5 na posição 3, obtemos `[1, 2, 4, 5, 8]`{.python}.

    Baseado nesta descrição, projete uma função que faça a ordenação dos valores usando o algoritmo de ordenação por seleção.


# Recursividade / Prática

**Veja o material** na página \url{https://malbarbo.pro.br/ensino/2024/6879/}.

@) Projete uma função recursiva que concatene todas as strings de uma lista de strings.

@) Uma lista de números é chamada de lista binária se todos os seus elementos são 0 ou 1. Projete uma função recursiva que verifique se uma lista é binária.

@) Projete uma função recursiva que receba como entrada uma string e um número inteiro positivo $n$ e gere uma nova string adicionando $n$ vezes o símbolo de exclamação no final da string da entrada. Por exemplo, se a string for `'Gol'`{.python} e $n = 4$, a saída deve ser `'Gol!!!!'`{.python}. Não use o operador de repetição de string (`*`{.python})!.


# Soluções

A seguir os nomes dos arquivos de soluções de alguns exercícios.

2: `isento_tarifa.py`

3: `dma_para_amd.py`

4: `sem_espacos.py`

5: `sinal.py`

6: `muda_num_chars.py`

7: `imposto.py`

9: `direcao.py`

12: `futebol.py`

13: `maximo_casas.py`

16: `negativos_antes_positivos.py`

18: `insere_pos.py`

20: `campeonato.py`

22: `dobrada.py`

24: `string_ints.py`

26: `remove_indice.py`

28: `concatena.py`

30: `exclama.py`
