"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
nome = 'Marcus Oliveira'  # str
idade = 25  # int
altura = 1.78  # float
e_maior = idade > 18  # bool
data_atual = 2022  # int
peso = 80
imc = peso / (altura ** 2)

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior : ', e_maior)

print(idade * altura)

print(nome, ' tem', idade, 'anos de idade e seu imc é ', imc)