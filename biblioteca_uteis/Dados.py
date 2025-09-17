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

def leiastr(msg):
    valor = False
    while not valor:
        n = str(input(msg)).strip()
        if n.isnumeric() or n == '':
            print(f'\033[1;31mERRO! o valor {n} não é uma string, Digite novamente.\033[m')
        else:
            return n
            break

def parouimpar(valor=0):
    if valor % 2 == 0:
        return 'PAR'
    else:
        return 'IMPAR'