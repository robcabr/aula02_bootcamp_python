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

num = int(input("Insira o valor a ser elevado ao quadrado: "))

quadrado = num **2

print(f"{num} elevado ao quadrado é {quadrado}")

####################################
# Float
#%%

# 6 - Escreva um programa que receba dois números flutuantes e realize sua adição.

primeiro_float = float(input('Primeiro numero a ser adicionado: '))

segundo_float = float(input('Segundo numero a ser adicionado: '))

soma_float = primeiro_float + segundo_float

print(f'A soma de {primeiro_float} + {segundo_float} resulta em {soma_float}')
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

print(f'A conversao de {temperatura_c} para Fahrenheit resulta em {fahrenheit}')

# %%

# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input('Adicione o raio: '))

circulo_area = math.pi * (raio**2)

print(f'O raio de {raio} resulta em uma área e circulo de: {circulo_area:.2f}')

####################################
# String

# %%

# 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

input_string = input("Adicione a string a ser transformada")

string_maiuscula = input_string.upper()

print(f'Texto em maiusculo: {string_maiuscula}')


# %%

# 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_completo = input("Insira o seu nome completo: ")

nome_minusculo = nome_completo.lower()

print(f'Nome em minusculo: {nome_minusculo}')

# %%

# 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase_completa = input("Insira uma frase completa: ")

frase_corrigida = frase_completa.strip()

print(f'Frase completa sem espaço: {frase_corrigida}')

# %%

# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_input = input("Digite uma data no formato DD/MM/AAAA: ")

#data_corrigida = data_input.split("/")

#print(f"{data_input}: Dia - {data_corrigida[0]}; Mes - {data_corrigida[1]}; Ano - {data_corrigida[2]}")

data_datetime_format = datetime.strptime(data_input, "%d/%m/%Y")

print(f"A {data_input}, ppssui os seguintes elementos: Dia - {data_datetime_format.day}; Mes - {data_datetime_format.month}; Ano - {data_datetime_format.year}")

# %%

# 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.

primeira_string = input("Forneca uma frase: ") 

segunda_string = input("Forneca uma frase: ") 

string_concatenado = primeira_string + " " + segunda_string

print(f'Texto concatenado = {string_concatenado}')

# #### Booleanos 

#%%
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# Ja que não é possível fazer a conversao de True e False para booleanos, ja que a funcao bool apenas avalia se a string é vazia ou não, estou comparando com true retornar um booleano

expressao_1 = input("Adicione uma expressão booleana: True or False").lower() == "true"
expressao_2 = input("Adicione outra expressão booleana: True or False").lower() == "true"

resultado_and = expressao_1 and expressao_2

print(f'Resultado and logico: {resultado_and}')

#%%
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# Ja que não é possível fazer a conversao de True e False para booleanos, ja que a funcao bool apenas avalia se a string é vazia ou não, estou comparando com true retornar um booleano

expressao_1 = input("Adicione uma expressão booleana: True or False").lower() == "true"
expressao_2 = input("Adicione outra expressão booleana: True or False").lower() == "true"

resultado_or = expressao_1 or expressao_2

print(f'Resultado or logico: {resultado_or}')

#%%
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

expressao_bool = input("Adicione uma expressão booleana: True or False").lower() == "true"

expressao_invertida = not(expressao_bool)

print(f'Resultado not logico: {expressao_invertida}')


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

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando `try-except`, garantir que a entrada seja numérica, tratando qualquer `ValueError`. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
  temperatura = float(input("Qual a temperatura a ser convertida? "))
  temperatura_convertida = (temperatura * 9/5) + 32
  print(f"A conversão de {temperatura} Celsius resulta em {temperatura_convertida:.2f} Fahrenheit ")
except ValueError:
  print("Valor inserido invalido. Insira um valor numérico. ")



#%%
# 22: Verificador de Palíndromo

frase = input("Por favor adicione uma frase: ")
if isinstance(frase, str):
  frase_formatada = frase.replace(" ", "").lower()
  if frase_formatada == frase_formatada[::-1]:
    print("As duas frases são identicas. Palindromo detectado.")
  else:
    print("As duas frases são diferentes.")
else:
  print("Entrada Incorreta. Digite uma palavra ou frase válida.")

#%%
# 23: Calculadora Simples

try:
  valor_1 = float(input("Adicione um valor numérico"))
  valor_2 = float(input("Adicione outro valor numérico"))
  operacao = input("Qual operação gostaria de realizar? +, -, / ou *? Selecione apenas uma.").lower()
  if operacao == '+':
    resultado = valor_1 + valor_2
  elif operacao == '-':
    resultado = valor_1 - valor_2
  elif operacao == '/':
    resultado = valor_1/valor_2
  elif operacao == '*':
    resultado = valor_1 * valor_2
  else: 
    print("Operação não reconhecida. Escolha uma das opções.")
  print(f"O resultado de {valor_1} {operacao} {valor_2} resultou em = {resultado}")
except ZeroDivisionError:
  print("Divisão por Zero. Por favor selecione outro valor.")
except ValueError:
  print("Valor não numérico. Insira um valor válido.")



#%%
# 24: Classificador de Números

# Escreva um programa que solicite ao usuário para digitar um número. Utilize `try-except` para assegurar que a entrada seja numérica e utilize `if-elif-else` para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
  numero = int(input("Adicione o valor a ser verificado: "))
  if numero < 0:
    print("O valor é negativo")
  elif numero > 0:
    print("O valor é posítivo")
  else:
    print("O valor é exatamente zero.")
  if numero % 2 == 0:
    print("Par")
  else:
    print("ímpar")
except ValueError:
  print("Adicione um valor numérico inteiro.")

#%%
# 25: Conversão de Tipo com Validação

# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize `try-except` para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

lista_usuario = input("Adicione uma lista de numeros separados por virgula")

try:
  lista_int = [int(valor.strip()) for valor in lista_usuario.split(sep=",")]
  print(f"Lista de Inteiros Convertida: {lista_int}")
except ValueError:
  print("Valor invalido inserido. Certifique-se de inserir apenas numeros inteiros.")

# %%
