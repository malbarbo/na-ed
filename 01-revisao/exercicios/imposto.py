# Análise
#
# Calcular o valor do imposto a partir da renda considerando que
#
# renda <= 1000, imposto de 5%
# renda <= 5000, imposto de 5% de 1000 (50) + 10% de (renda - 1000)
# renda > 5000, imposto de 5% de 1000 (50) + 10% de 4000 (400) + 20% de (renda - 5000)

# Tipos de dados
#
# A renda e o imposto serão representados por números positivos

def imposto(renda: float) -> float:
    '''
    Calcula o imposto que um cidadão com *renda* deve pagar.
    Se renda <= 1000, imposto de 5%.
    Se 1000 < renda <= 5000, imposto de 5% de 1000 (50) + 10% de (renda - 1000).
    Se renda > 5000, imposto de 5% de 1000 (50) + 10% de 4000 (400) + 20% de (renda - 5000).

    Exemplos
    >>> imposto(900.0) # 900.0 * 5.0 / 100.0
    45.0
    >>> imposto(1000.0)
    50.0
    >>> imposto(4000.0) # 50.0 + (4000.0 - 1000.0) * 10.0 / 100.0
    350.0
    >>> imposto(5000.0)
    450.0
    >>> imposto(6000.0) # 50.0 + 400.0 + (6000.0 - 5000.0) * 20.0 / 100.0
    650.0
    '''
    if renda <= 1000.0:
        imposto = renda * 5.0 / 100.0
    elif renda <= 5000.0:
        imposto = 50.0 + (renda - 1000.0) * 10.0 / 100.0
    else:
        imposto = 50.0 + 400.0 + (renda - 5000.0) * 20.0 / 100.0
    return imposto
