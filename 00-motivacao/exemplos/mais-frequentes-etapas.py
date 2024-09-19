from __future__ import annotations
from dataclasses import dataclass
from time import time
import sys


def main() -> None:
    if len(sys.argv) != 4:
        print(f'Modo de usar: python {sys.argv[0]} m n arquivo')
        print('  m - quantidade de palavras na saída')
        print('  n - quantidade de palavras para serem lidas do arquivo de entrada')
        sys.exit(1)

    m = int(sys.argv[1])

    n = int(sys.argv[2])

    palavras = list(open(sys.argv[3]).read().split())[:n]

    inicio = time()
    mais_frequentes = encontra_mais_frequentes(palavras, m)
    duracao = time() - inicio

    print('Palavras mais frequentes:')
    for c in mais_frequentes:
        print(c.palavra, c.vezes)

    print('Tempo de execução:', round(duracao, 2), 'segundos')


@dataclass
class PalavraVezes:
    '''
    Representa uma palavra e a quantidade de vezes que ela aparece em um corpus.
    '''
    palavra: str
    vezes: int

    def __lt__(self, outra: PalavraVezes) -> bool:
        '''
        Produz True se *self* aparece menos vezes que *outra* ou se aparece o
        mesmo número de vezes mas vem depois em ordem alfabética.
        Exemplos
        >>> PalavraVezes('casa', 3) < PalavraVezes('caso', 4)
        True
        >>> PalavraVezes('casa', 3) < PalavraVezes('caso', 3)
        False
        '''
        return self.vezes < outra.vezes or \
            self.vezes == outra.vezes and self.palavra > outra.palavra


def encontra_mais_frequentes(palavras: list[str], m: int) -> list[PalavraVezes]:
    '''
    Encontra as *m* palavras mais frequentes em *palavras*.
    Se a frequência de duas palavras for a mesma, então a
    que vem primeiro em ordem alfabética aparece primeiro.

    Se *m* for maior que a quantidade de palavras distintas,
    então devolve a frequência de todas as palavras.

    Requer que m > 0.

    Exemplos
    >>> encontra_mais_frequentes(['casa', 'de', 'a', 'ti', 'de', 'a', 'casa', 'a', 'de'], 3)
    [PalavraVezes(palavra='a', vezes=3), PalavraVezes(palavra='de', vezes=3), PalavraVezes(palavra='casa', vezes=2)]
    '''
    # Calcula a frequência de cada palavra
    contagem: list[PalavraVezes] = []
    for p in palavras:
        # Procura o índice i de p na contagem
        i = 0
        while i < len(contagem) and contagem[i].palavra != p:
            i = i + 1

        # Encontrou o índice de p? Ou seja, p está na contagem?
        if i < len(contagem):
            contagem[i].vezes = contagem[i].vezes + 1
        else:
            contagem.append(PalavraVezes(p, 1))

    # Ordena por maior frequência
    for i in range(len(contagem)):
        imax = i
        for j in range(i + 1, len(contagem)):
            if contagem[imax] < contagem[j]:
                imax = j
        troca(contagem, i, imax)

    return contagem[:m]


def troca(lst: list, i: int, j: int) -> None:
    '''
    Move o elemento da posição *i* de *lst* para a posição *j* e vice-versa.

    Requer que *i* e *j* sejam posições valídas de *lst*.

    Exemplos
    >>> lst = [5, 1, 6, 8, 2]
    >>> troca(lst, 2, 4)
    >>> lst
    [5, 1, 2, 8, 6]
    '''
    lst[i], lst[j] = lst[j], lst[i]


if __name__ == "__main__":
    main()
