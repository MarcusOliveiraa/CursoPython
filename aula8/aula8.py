"""
Entrada de dados - Aula 8
"""
nome = input('Qual seu nome? ')
idade = input('Qual a sua idade? ')

numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

ano_nascimento = 2022 - int(idade)

print(f'O usuario digitou {nome} e o tipo da variavel é {type(nome)}')

print(f'{nome} tem {idade} anos')
print(f'{nome} nascem em {ano_nascimento}')

print(int(numero1) + int(numero2))

