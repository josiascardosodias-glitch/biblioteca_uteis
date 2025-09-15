def linha(tamanho=1):
    print( '-' * tamanho)

def cabeçalho(texto):
    linha(len(texto) + 4)
    print(f'  {texto}')
    linha(len(texto) + 4)
    
def leiaInt(msg):
    valor = False
    while not valor:
        n = str(input(msg)).strip()
        if n.isnumeric():
            return int(n)
            break
        else:
            print(f'\033[1;31mERRO! o valor {n} não é um número inteiro, Digite novamente.\033[m')

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! o valor digitado não é um número real, Digite novamente.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def real(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')

def dollar(valor=0, moeda='US$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')

def aumentar(valor=0, taxa=0):
    return valor + (valor * taxa / 100)

def diminuir(valor=0, taxa=0):    return valor - (valor * taxa / 100)