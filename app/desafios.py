# Desafios não obrigatórios alura - 1
#
# Exercício 1
# print("Python na Escola de Programação da Alura")
# Exercício 2
# idade = int(input("Digite sua idade: "))
# nome = input("Digite seu nome: ")
# print(f"Meu nome é {nome} e tenho {idade} anos")
# Exercício 3
# print(*"ALURA", sep="\n")
# Exercício 4
# pi = 3.14159
# print(f"O valor arredondado de pi é: {pi:.2f}")

# Desafios não obrigatórios alura - 2
#
# Exercício 1
# numero = int(input("Digite um numero inteiro: "))
#
# if numero % 2 == 0:
#     print("Este número é par")
# else:
#     print("Este número é impar")
# Exercício 2
# idade = int(input("Qual a sua idade? "))
# if idade <= 12:
#     print("Criança")
# elif 13 <= idade <= 18:
#     print("Adolescente")
# else:
#     print("Adulto")
# Exercício 3
# def login():
#     usuario = "spanholi"
#     senha = "eita"
#     login_usuario = input("Digite seu nome de usuario: ")
#     login_senha = input("Digite sua senha: ")
#
#     if login_usuario == usuario and login_senha == senha:
#         print("Login validado")
#     else:
#         print("Login invalido")
#
# login()
# Exercício 4
# def plano_cartesiano():
#     x = float(input("Insira o valor de x: "))
#     y = float(input("Insira o valor de y: "))
#
#     if x > 0 and y > 0:
#         print("Primeiro Quadrante")
#     elif x < 0 and y > 0:
#         print("Segundo Quadrante")
#     elif x < 0 and y < 0:
#         print("Terceiro Quadrante")
#     elif x > 0 and y < 0:
#         print("Quarto Quadrante")
#     else:
#         print("Eixo")
#
# plano_cartesiano()

# Desafios não obrigatórios alura - 3
#
# Exercício 1
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nomes = ["Enzo", "Bernardo", "Pedro", "João"]
# anos = [2008, 2026]
# Exercício 2
# numeros = list(range(1,21)) # Mesma coisa que numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for numero in numeros:
#     print(numero)
# Exercício 3
# soma_numeros = 0
# for numero in range(1,11):
#     if numero % 2 != 0:
#         soma_numeros += numero
#
# print(soma_numeros)
# Exercício 4
# for numero in range(10, 0, -1):
#     print(numero)
# Exercício 5
# numero = int(input("Digite um numero inteiro: "))
#
# for multiplicador in range(1, 11):
#     resultado = numero *multiplicador
#     print(f"{numero} x {multiplicador} = {resultado}")
# Exercício 6
# lista = [1, 2, 3, 4, 5, 6]
# resultado = 0
#
# for numero in lista:
#     try:
#         resultado += numero
#     except Exception as erro:
#         print(erro)
#
# print(resultado)
# Exercício 6
# lista = list(range(1,21))
# try:
#     media = sum(lista)/len(lista)
#     print(media)
# except ZeroDivisionError:
#     print("Erro")
#
# Desafios não obrigatórios alura - 3
#
# Exercício 1
# informacoes = {"nome": "Bernardo", "idade": 19, "cidade": "São Paulo"}
# Exercício 2
# informacoes["idade"] = 20
# informacoes["profissao"] = "Desempregado"
# informacoes.pop("cidade")
# Exercício 3
# numeros = {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }
# Exercício 4
# informacoes = {"nome": "Bernardo", "idade": 19, "cidade": "São Paulo"}
# print("Existe") if "cidade" in informacoes else print("Não existe")
# Exercício 5
# frase = "python é legal python é poderoso"
#
# palavras = frase.split()
#
# frequencia = {}
#
# for palavra in palavras:
#     if palavra in frequencia:
#         frequencia[palavra] += 1
#     else:
#         frequencia[palavra] = 1
#
# print(frequencia)
app/desafios.py