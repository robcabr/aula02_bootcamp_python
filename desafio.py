# Desafio

# Para resolver os bugs identificados — 
# tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, 
# você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.

# Constante bonus

CONSTANTE_BONUS = 1000

# Nome do usuario 


try:
  nome_usuario = input("Por favor digite o seu nome: ")
  if any(letra.isdigit() for letra in nome_usuario):
    print("Nome Invalido. Nome de Usuário não pode conter números.")
    exit()
  elif len(nome_usuario) == 0 or nome_usuario.isspace():
    print("Nome Invalido. Nao contêm qualquer caracter.")
    exit()
  else:
    print("Nome Válido.")
except ValueError:
  print('Valor Invalido. Adicione um nome válido.')

# Salario

try:
  salario = float(input("Adicione o seu salario: "))
  if salario < 0:
      print("Valor negativo não é aceito. Insira um valor positivo")
except ValueError:
  print("Valor incorreto. Adicione um valor numérico válido")
  exit()
# Bonus

try:
  bonus_usuario = float(input("Por favor digite o seu bonus: "))
  if bonus_usuario < 0:
      print("Valor negativo não é aceito. Insira um valor positivo")
except ValueError:
  print("Valor incorreto. Adicione um valor numérico válido")
  exit()

# Valor a receber

valor_do_bonus = CONSTANTE_BONUS + salario * bonus_usuario


# Imprima a mensagem personalizada incluindo o nome do usuario e o valor do bonus
print(f"Ola {nome_usuario}, o seu bonus será de {valor_do_bonus}")