nome = 'Marcus Oliveira'  # str
idade = 25  # int
altura = 1.80  # float
e_maior = idade > 18  # bool
data_atual = 2022  # int
peso = 80
imc = peso / (altura ** 2)

print(nome, ' tem', idade, 'anos de idade e seu imc é ', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))

print('{2} {0} {0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))

print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))