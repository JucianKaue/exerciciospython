def notas(* notas, sit=False):
    """
    ->> Lê varias notas e retorna um dicionário.
    :notas: notas a serem analizadas
    :return: Um dicionário com:
        - Quantidades de notas inseridas
        - A maior nota
        - A menor nota
        - A média da turma
        - A situação
    """
    q = len(notas)
    for cont, n in enumerate(notas):
        if cont == 0:
            mai = men = soma = n
        else:
            if n > mai:
                mai = n
            if n < men:
                men = n
            soma += n
    media = soma / q
    info = {'Quantidade de notas': q, 'Maior nota': mai, 'Menor nota': men, 'Média': media}
    if sit:
        if media < 7:
            info['situação'] = 'REPROVADO'
        elif media >= 7:
            info['situação'] = 'APROVADO'
    return info


for k, v in notas(6, 8, 3, 7, 9.6, sit=True).items():
    print(f'\033[33m{k:<20}\033[0m tem valor \033[33m{v}\033[0m')
print()
help(notas)
