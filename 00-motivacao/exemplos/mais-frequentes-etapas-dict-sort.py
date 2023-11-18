from __future__ import annotations
from dataclasses import dataclass
from time import time
import sys


def main():
    if len(sys.argv) != 4:
        print('Modo de usar: {} m n arquivo', sys.argv[0])
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

    print('Tempo de execução:', duracao, 'segundos')


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

    Se *m* for menor que a quantidade de palavras distintas,
    então devolve a frequência de todas as palavras.

    Requer que m > 0.

    Exemplos
    >>> encontra_mais_frequentes(['casa', 'de', 'a', 'ti', 'de', 'a', 'casa', 'a', 'de'], 3)
    [PalavraVezes(palavra='a', vezes=3), PalavraVezes(palavra='de', vezes=3), PalavraVezes(palavra='casa', vezes=2)]
    '''
    # Calcula a frequência de cada palavra
    contagem: dict[str, int] = {}
    for p in palavras:
        if p in contagem:
            contagem[p] = contagem[p] + 1
        else:
            contagem[p] = 1

    # Cria uma lista de PalavrasVezes
    freqs = []
    for p, vezes in contagem.items():
        freqs.append(PalavraVezes(p, vezes))

    # Ordena a lista
    freqs.sort(reverse=True)

    return freqs[:m]


if __name__ == "__main__":
    main()
