def linha(tamanho=1):
    print( '-' * tamanho)

def cabeçalho(texto):
    linha(len(texto) + 4)
    print(f'  {texto}')
    linha(len(texto) + 4)

def real(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')

def dollar(valor=0, moeda='US$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')

def euro(valor=0, moeda='€'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')