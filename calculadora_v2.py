saida = ''
def adicao():
    numero1 = eval(input("Digite o primeiro numero: ").replace(',', '.'))
    numero2 = eval(input("Digite o segundo numero: ").replace(',', '.'))
    print(numero1 + numero2)
def subtracao():
    numero1 = eval(input("Digite o primeiro numero: ").replace(',', '.'))
    numero2 = eval(input("Digite o segundo numero: ").replace(',', '.'))
    print(numero1 - numero2)
def multiplicacao():
    numero1 = eval(input("Digite o primeiro numero: ").replace(',', '.'))
    numero2 = eval(input("Digite o segundo numero: ").replace(',', '.'))
    print(numero1 * numero2)
def divisao():
    numero1 = eval(input("Digite o primeiro numero: ").replace(',', '.'))
    numero2 = eval(input("Digite o segundo numero: ").replace(',', '.'))
    div = numero1 / numero2
    if numero1 == 0:
        print('Não foi possível realizar a divisão por 0')
    else:
        print(div)

def calculadora():
    operacao = input('Digite a operação desejada (+, -, *, / ou adicao, subracao, multiplicacao, divisao): ')
    if operacao == '+' or operacao.lower() == 'adicao':
        adicao()
    elif operacao == '-' or operacao.lower() == 'subtracao':
        subtracao()
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        multiplicacao()
    elif operacao == '/' or operacao.lower() == 'divisao':
        divisao()
    else:
        print('Entrada inválida')

while saida.lower() != 'n':
    calculadora()
    saida = input('Deseja continuar? (S/N): ')