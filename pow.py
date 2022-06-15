def result(num, vezes):
    if vezes < 10:
        print('{} ^ {:2} = {}'.format(num,vezes,pow(num, vezes)))
    else:
        print('{} ^ {} = {}'.format(num,vezes,pow(num, vezes)))

def main():
    print('Olá! Sou um programa para calcular a tabela de potenciação de qualquer número inteiro que você inserir.')
    num = int(input('Digite o número de sua escolha: '))
    print('-'*20)
    for i in range(-5, 21):
        result(num, i)
    print('-'*20)

if __name__ == '__main__':
    main()
