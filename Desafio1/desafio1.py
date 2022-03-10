nome = 'Marcus'
idade = 25
altura = 1.77
peso = 85.0
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print('{} tem {} anos, {} de altura e pesa {} KG'.format(nome, idade, altura, peso))
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')