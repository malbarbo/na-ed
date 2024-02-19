# Notas de aula de estruturas de dados

Para gerar os pdfs execute o comando `make pdf`. Os arquivos pdfs serão gerados no diretório `target/`.

Este comando irá baixar e executar os programas [pandoc](https://pandoc.org/) e [tectonic](http://tectonic-typesetting.github.io/).

Se preferir, veja os pdfs [aqui](https://malbarbo.pro.br/ensino/2023/6884/).


## Tipos abstratos de dados

- [Pilha](04-estruturas-lineares-contiguas/exemplos/pilha_tad.py)
  - Arranjo estático e topo ([`pilha_arranjo.py`](/04-estruturas-lineares-contiguas/exemplos/pilha_arranjo.py))
  - Encadeamento ([`pilha_encadeada.py`](/05-estruturas-lineares-encadeadas/exemplos/pilha_encadeada.py))
- [Fila](04-estruturas-lineares-contiguas/exemplos/fila_tad.py)
  - Arranjo estático e fim ([`fila_arranjo_fim.py`](04-estruturas-lineares-contiguas/exemplos/fila_arranjo_fim.py))
  - Arranjo estático, início e fim ([`fila_arranjo_inicio_fim.py`](04-estruturas-lineares-contiguas/exemplos/fila_arranjo_inicio_fim.py))
  - Arranjo estático circular ([`fila_arranjo_circular.py`](04-estruturas-lineares-contiguas/exemplos/fila_arranjo_circular.py))
  - Encadeamento e referência para o início ([`fila_encadeada_inicio.py`](/05-estruturas-lineares-encadeadas/exemplos/fila_encadeada_inicio.py))
  - Encadeamento e referência para o início e fim ([`fila_encadeada_inicio_fim.py`](/05-estruturas-lineares-encadeadas/exemplos/fila_encadeada_inicio_fim.py))
- [Fila Dupla](04-estruturas-lineares-contiguas/pratica-solucoes/fila_dupla_tad.py)
  - Encadeamento simples ([`fila_dupla_encadeamento_simples.py`](05-estruturas-lineares-encadeadas/exemplos/fila_dupla_encadeamento_simples.py))
  - Encadeamento duplo ([`fila_dupla_encadeamento_duplo_direta.py`](05-estruturas-lineares-encadeadas/exemplos/fila_dupla_encadeamento_duplo_direta.py))
  - Encadeamento duplo com sentinela ([`fila_dupla_encadeamento_duplo_sentinela.py`](05-estruturas-lineares-encadeadas/exemplos/fila_dupla_encadeamento_duplo_sentinela.py))
- [Lista](04-estruturas-lineares-contiguas/exemplos/lista_tad.py)
  - Arranjo estático com redimensionamento ([`lista_arranjo.py`](04-estruturas-lineares-contiguas/exemplos/lista_arranjo.py))
  - Encadeamento simples ([`lista_encadeamento_simples.py`](05-estruturas-lineares-encadeadas/pratica-solucoes/lista_encadeamento_simples.py))
- [Dicionário](07-busca-e-arvores/exemplos/dicionario_tad.py)
  - Encadeamento simples ([`dicionario_encadeamento.py`](07-busca-e-arvores/exemplos/dicionario_encadeamento.py))
  - Arranjo ([`dicionario_arranjo.py`](07-busca-e-arvores/exemplos/dicionario_arranjo.py))
  - Arranjo ordenado e busca binária ([`dicionario_arranjo_ordenado.py`](07-busca-e-arvores/pratica-solucoes/dicionario_arranjo_ordenado.py))
  - Árvore AVL (em breve)
  - Tabela de dispersão (em breve)


## Busca e ordenação

- Busca binária
  - Iterativa ([`busca_binaria.py`](07-busca-e-arvores/exemplos/busca_binaria.py))
  - Recursiva ([`busca_binaria.py`](06-recursividade/pratica-solucoes/busca_binaria.py))


# Licença

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
  <img alt="Licença Creative Commons" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a>
<br />
<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">
Notas de aula de estruturas de dados</span> de
<a xmlns:cc="http://creativecommons.org/ns#" href="http://malbarbo.pro.br" property="cc:attributionName" rel="cc:attributionURL">
Marco A L Barbosa</a>
está licenciado com uma Licença
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
Creative Commons - Atribuição-CompartilhaIgual 4.0 Internacional</a>.

<!-- % vim: set spell spelllang=pt_br: -->
