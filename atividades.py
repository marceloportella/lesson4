# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# numeros : list = []

# for a in range(1,10):
#     numeros.append(a**2)
#     print(f" o valor de {a} elevado ao quadrado é {a**2}")

# print(numeros)


# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# linguagens : list = ["Python", "Java", "C++", "JavaScript"]
# print (linguagens)

# # linguagens[2]="Ruby"
# # print(linguagens)

# # or

# linguagens.remove("C++")
# linguagens.append("Ruby")
# print (linguagens)

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

# book :dict = {}

# book["titulo"]="Jornada das Estrelas"
# book["autor"]="Joao"
# book["Ano Publicacao"] = "2002"

# print(book)

# for k,v in book.items():
#     print(f"O {k} é {v}")

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))


# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# compras = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = 0

# for a in compras.values():
#     total += a

# print(total)


# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))


# print(emails_unicos)

# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# idades = [22, 15, 30, 17, 18]
# # maior=[]
# # for a in idades:
# #     if a >= 18:
# #         maior.append(a)
# # print(maior)

# # Or

# maior = [idade for idade in idades if idade >= 18]
# print(maior)

# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Carol", "idade": 25},
#     {"nome": "Bob", "idade": 20}
# ]


# pessoas.sort(key= lambda pessoas:pessoas["nome"])

# print(pessoas)

# Objetivo: Dado um conjunto de números, calcular a média.

# numeros = [10,20,14,13,43]
# total = sum(numeros)/len(numeros)
# print(total)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [par for par in valores if par % 2 == 0]
impares = [impar for impar in valores if impar%2 != 0]

print(pares)
print(impares)