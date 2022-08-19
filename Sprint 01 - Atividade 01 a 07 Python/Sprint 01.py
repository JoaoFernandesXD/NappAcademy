#Crie um programa que declare duas variáveis. Essas variáveis devem permitir o input de dois números inteiros.
#Por fim, o programa deve retornar uma mensagem com os dois números e a soma deles conforme exemplo:
#'A soma entre <numero1> e <numero2> vale <soma>.'

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

print(f'A soma entre {numero1} e {numero2} vale {numero1 + numero2}.')

##################################################################################################################################################################

#Faça um programa que rebeça alguma informação e devolva se ele é:

#É um número? <True/False>.
#É texto? <True/False>.
#É um valor alphanúmerico? <True/False>.

numero = input('Digite algo: ')

print(f'É um número? {numero.isdigit()}.')
print(f'É texto? {numero.isalpha()}.')
print(f'É um valor alphanúmerico? {numero.isalnum()}.')

##################################################################################################################################################################

#Faça um programa que receba um input de um número inteiro e mostre na tela o seu sucessor. 
#Conforme a mensagem baixo:
#Informado: <número inteiro>
#Sucessor: <número sucessor>

numero = int(input('Informe um valor: '))
sucessor = numero + 1
print(f'Informado: {numero}')
print(f'Sucessor: {sucessor}')

##################################################################################################################################################################

#Crie um algoritmo que leia e receba um número e mostre o seu drobro,
#triplo e raiz quadrada com duas casa decimais. Conforme mensagem abaixo:
#Dobro: <dobro do número>
#Triplo: <triplo do número>
#Raiz Quadrada: <raiz quadrada do número>

numero = int(input('Informe um valor: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print(f'Dobro: {dobro}')
print(f'Triplo: {triplo}')
print(f'Raiz Quadrada: {raiz:.2f} ')

##################################################################################################################################################################

#Desenvolva um programa que receba as duas notas de um aluno, calcule e mostre a sua média com uma casa decimal. 
#Conforme exemplo abaixo:

     #Informe a primeira nota: <primeira nota>
     #Informe a segunda nota: <segunda nota>
     #Média: <valor da média>

nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))
#calcular media do aluno
media = (nota1 + nota2) / 2

print(f'Média: {media:.1f}')

##################################################################################################################################################################

#Escreva um programa que receba um número inteiro em metros e o exiba convertido em 
#centímetros e milímetros, conforme o exemplo abaixo:

    #Centrimento: <centimetro> cm
    #Milimetro: <milimetro> mm
metros = int(input('Informe o valor em metro(s): '))
#calcular centimetros
centimetros = (metros * 100)
#calcular milimetros
milimetros = (metros * 1000)

print(f'Centimetro: {centimetros} cm')
print(f'Milimetro: {milimetros} mm')

##################################################################################################################################################################

#Crie um programa que receba quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares (valor do dolar R$5.22) ela pode comprar.
#Por fim, mostre a seguinte mensagem:
#Com R$ <valor em real> você pode comprar $ <valor em dolar>

# valor em carteira
valor_reais = float(input('Informe seu dinheiro: R$ '))
# cotação do dolar atual
dolar_atual = 5.22
# conversão de reais pra dolar
conversor = (valor_reais / dolar_atual)

print(f'Com R$ {valor_reais:.2f} você pode comprar $ {conversor:.2f}')



##################################################################################################################################################################




