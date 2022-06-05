def result(num, vezes):
    if vezes < 10:
        print('{} ^ {:2} = {}'.format(num,vezes,pow(num, vezes)))
    else:
        print('{} ^ {} = {}'.format(num,vezes,pow(num, vezes)))

def main():
    print('Olá! Sou um programa para calcular a tabela de potenciação de qualquer número inteiro que você inserir.\nPs: Não use vírgulas comigo! Ao invés disso, use pontos!')
    num = int(input('Digite o número de sua escolha: '))
    print('-'*15)
    for i in range(21):
        result(num, i)
    print('-'*15)

if __name__ == '__main__':
    main()
