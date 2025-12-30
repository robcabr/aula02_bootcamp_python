# %%
import math

from datetime import datetime 

####################################
# Inteiros 
#%%
# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

primeiro_numero = int(input('Digite o seu primeiro numero: '))

segundo_numero = int(input('Digite o seu segundo numero: '))

soma = primeiro_numero + segundo_numero

print(f'O valor total de {primeiro_numero} + {segundo_numero} é {soma}')


#%%
# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5. 

numero_modulo = int(input("Digite o seu número: "))

modulo = numero_modulo % 5

print(f'O resto de {numero_modulo} por 5 é {modulo}')

#%%
# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

primeiro_multiplicacao = int(input('Digite o seu primeiro numero: '))

segundo_multiplicacao = int(input('Digite o seu segundo numero: '))

multiplicacao = primeiro_multiplicacao * segundo_multiplicacao

print(f'O valor total de {primeiro_multiplicacao} X {segundo_multiplicacao} é {multiplicacao}')

#%%
# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

primeiro_divisao = int(input('Digite o seu primeiro numero: '))

segundo_divisao = int(input('Digite o seu segundo numero: '))

divisao_inteira = primeiro_divisao // segundo_divisao

print(f'A divisao inteira de {primeiro_divisao} por {segundo_divisao} = {divisao_inteira}')


#%%

# 5 - -Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero_quadrado = int(input("Insira o valor a ser elevado ao quadrado: "))

quadrado = numero_quadrado **2

print(f"{numero_quadrado} elevado ao quadrado é {quadrado}")

####################################
# Float
#%%

# 6 - Escreva um programa que receba dois números flutuantes e realize sua adição.

primeiro_float = float(input('Primeiro numero a ser adicionado: '))

segundo_float = float(input('Segundo numero a ser adicionado: '))

soma_float = primeiro_float + segundo_float

print(f'A soma de {primeiro_float} com {segundo_float} resulta em {soma_float}')
# %%

# 7 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

valor_media_primeiro = float(input('Valor a ser somado: '))

valor_media_segundo = float(input('Valor a ser somado: '))

media = (valor_media_primeiro + valor_media_segundo) / 2

print(f'A média de {valor_media_primeiro} e {valor_media_segundo} é {media}')

# %%

# 8 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

valor_potencial_01 = float(input("Adicione a base da potencia: "))

valor_potencial_02 = float(input("Adicione o expoente da potencia: "))

potencial = valor_potencial_01 ** valor_potencial_02

print(f'A potencial de {valor_potencial_01} elevado a {valor_potencial_02} é {potencial}')

# %%

# 9 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.

temperatura_c = float(input('Temperatura em Celsius: '))

fahrenheit = (temperatura_c * 1.8) + 32

print(f'A conversao de {temperatura_c} para F resulta em {fahrenheit}')

# %%

# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input('Adicione o raio: '))

circulo_area = math.pi * (raio**2)

print(f'O raio de {raio} resulta em {circulo_area:.2f}')

####################################
# String

# %%

# 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

input_string = input("Adicione a string a ser transformada")

string_maiuscula = input_string.upper()

print(string_maiuscula)


# %%

# 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_completo = input("Insira o seu nome completo: ")

nome_minusculo = nome_completo.lower()

print(nome_minusculo)

# %%

# 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase_completa = input("Insira uma frase completa: ")

frase_corrigida = frase_completa.strip()

print(frase_corrigida)

# %%

# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_input = input("Digite uma data no formato DD/MM/AAAA: ")

#data_corrigida = data_input.split("/")

#print(f"{data_input}: Dia - {data_corrigida[0]}; Mes - {data_corrigida[1]}; Ano - {data_corrigida[2]}")

data_date_format = datetime.strptime(data_input, "%d/%m/%Y")

print(f"A {data_input}, ppssui os seguintes elementos: Dia - {data_date_format.day}; Mes - {data_date_format.month}; Ano - {data_date_format.year}")

# %%

# 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.

primeira_string = input("Forneca uma frase: ") 

segunda_string = input("Forneca uma frase: ") 

print(primeira_string + " " + segunda_string)

# #### Booleanos 

#%%
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# Ja que não é possível fazer a conversao de True e False para booleanos, ja que a funcao bool apenas avalia se a string é vazia ou não, estou comparando com true retornar um booleano

expressao_1 = input("Adicione uma expressão booleana: True or False").lower() == "true"
expressao_2 = input("Adicione outra expressão booleana: True or False").lower() == "true"

resultado_and = expressao_1 and expressao_2

print(resultado_and)

#%%
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# Ja que não é possível fazer a conversao de True e False para booleanos, ja que a funcao bool apenas avalia se a string é vazia ou não, estou comparando com true retornar um booleano

expressao_1 = input("Adicione uma expressão booleana: True or False").lower() == "true"
expressao_2 = input("Adicione outra expressão booleana: True or False").lower() == "true"

resultado_or = expressao_1 or expressao_2
print(resultado_or)

#%%
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

expressao_bool = input("Adicione uma expressão booleana: True or False").lower() == "true"

expressao_invertida = not(expressao_bool)

print(expressao_bool, expressao_invertida)


#%%
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

valor_1 = int(input("Adicione um valor numérico: "))
valor_2 = int(input("Adicione outro valor numérico: "))

print(f' O valor de {valor_1} é igual a {valor_2}? {valor_1 == valor_2}')


#%%
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

valor_1 = int(input("Adicione um valor numérico: "))
valor_2 = int(input("Adicione outro valor numérico: "))

print(f' O valor de {valor_1} é diferente de {valor_2}? {valor_1 != valor_2}')


#%%
# #### try-except e if

# 21: Conversor de Temperatura




#%%
# 22: Verificador de Palíndromo




#%%
# 23: Calculadora Simples





#%%
# 24: Classificador de Números



#%%
# 25: Conversão de Tipo com Validação



