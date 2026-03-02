# ==========================================================
# FUNÇÕES E MÉTODOS MAIS USADOS NO PYTHON
# ==========================================================
# Este arquivo mostra funções nativas (built-in) e métodos
# muito usados no dia a dia.
# ==========================================================


# ----------------------------------------------------------
# 1. len() → Retorna o tamanho
# ----------------------------------------------------------

lista = [10, 20, 30]
texto = "Python"

print("Tamanho da lista:", len(lista))
print("Tamanho do texto:", len(texto))


# ----------------------------------------------------------
# 2. type() → Mostra o tipo da variável
# ----------------------------------------------------------

numero = 10
print("Tipo:", type(numero))


# ----------------------------------------------------------
# 3. int(), float(), str() → Conversão de tipos
# ----------------------------------------------------------

numero_string = "25"

numero_int = int(numero_string)
numero_float = float(numero_string)
numero_texto = str(numero_int)

print(numero_int, type(numero_int))
print(numero_float, type(numero_float))
print(numero_texto, type(numero_texto))


# ----------------------------------------------------------
# 4. max() e min() → Maior e menor valor
# ----------------------------------------------------------

numeros = [5, 2, 9, 1]
print("Maior:", max(numeros))
print("Menor:", min(numeros))


# ----------------------------------------------------------
# 5. sum() → Soma de valores
# ----------------------------------------------------------

print("Soma:", sum(numeros))


# ----------------------------------------------------------
# 6. sorted() → Ordena lista (não altera original)
# ----------------------------------------------------------

print("Ordenado:", sorted(numeros))


# ----------------------------------------------------------
# 7. Métodos de String
# ----------------------------------------------------------

texto = "python é poderoso"

print(texto.upper())        # Tudo maiúsculo
print(texto.lower())        # Tudo minúsculo
print(texto.capitalize())   # Primeira letra maiúscula
print(texto.replace("python", "Python"))
print(texto.split())        # Divide em lista


# ----------------------------------------------------------
# 8. Métodos de Lista
# ----------------------------------------------------------

valores = [1, 2, 3]

valores.append(4)      # Adiciona elemento
valores.insert(0, 0)   # Insere na posição
valores.remove(2)      # Remove valor específico
valores.pop()          # Remove último elemento

print("Lista final:", valores)


# ----------------------------------------------------------
# 9. range() → Gera sequência numérica
# ----------------------------------------------------------

for i in range(5):
    print("Número:", i)


# ----------------------------------------------------------
# 10. enumerate() → Índice + valor
# ----------------------------------------------------------

nomes = ["Ana", "Carlos", "João"]

for indice, nome in enumerate(nomes):
    print(indice, "-", nome)


# ----------------------------------------------------------
# 11. zip() → Junta listas
# ----------------------------------------------------------

idades = [25, 30, 35]

for nome, idade in zip(nomes, idades):
    print(nome, "tem", idade, "anos")


# ----------------------------------------------------------
# 12. any() e all()
# ----------------------------------------------------------

lista_booleana = [True, True, False]

print("Algum True?", any(lista_booleana))
print("Todos True?", all(lista_booleana))


# ----------------------------------------------------------
# 13. map() → Aplica função a cada elemento
# ----------------------------------------------------------

numeros = [1, 2, 3, 4]

dobrados = list(map(lambda x: x * 2, numeros))
print("Dobrados:", dobrados)


# ----------------------------------------------------------
# 14. filter() → Filtra valores
# ----------------------------------------------------------

pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

# ----------------------------------------------------------
# FIM
# ----------------------------------------------------------

print("\nArquivo finalizado com sucesso.")