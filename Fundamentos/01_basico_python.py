# ==========================================================
# PYTHON BÁSICO - GUIA PARA INICIANTES
# ==========================================================
# Este arquivo contém os principais conceitos que um
# iniciante aprende ao começar Python.
# ==========================================================


# ----------------------------------------------------------
# 1. VARIÁVEIS E TIPOS DE DADOS
# ----------------------------------------------------------

nome = "Elisson"     # String (texto)
idade = 28           # Integer (número inteiro)
altura = 1.75        # Float (número decimal)
ativo = True         # Boolean (True ou False)

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Ativo:", ativo)


# ----------------------------------------------------------
# 2. OPERADORES MATEMÁTICOS
# ----------------------------------------------------------

a = 10
b = 3

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Divisão inteira:", a // b)
print("Resto:", a % b)
print("Potência:", a ** b)


# ----------------------------------------------------------
# 3. CONDICIONAIS (IF, ELIF, ELSE)
# ----------------------------------------------------------

numero = 15

if numero > 10:
    print("Número maior que 10")
elif numero == 10:
    print("Número igual a 10")
else:
    print("Número menor que 10")


# ----------------------------------------------------------
# 4. LISTAS
# ----------------------------------------------------------

numeros = [10, 20, 30, 40]

print("Lista completa:", numeros)
print("Primeiro elemento:", numeros[0])

numeros.append(50)        # Adiciona elemento
numeros.remove(20)        # Remove elemento
print("Lista atualizada:", numeros)
print("Tamanho da lista:", len(numeros))


# ----------------------------------------------------------
# 5. LOOP FOR
# ----------------------------------------------------------

for numero in numeros:
    print("Valor da lista:", numero)


# ----------------------------------------------------------
# 6. LOOP WHILE
# ----------------------------------------------------------

contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1


# ----------------------------------------------------------
# 7. FUNÇÕES
# ----------------------------------------------------------

def saudacao(nome):
    return f"Olá, {nome}!"


print(saudacao("Python"))


# ----------------------------------------------------------
# 8. DICIONÁRIOS
# ----------------------------------------------------------

pessoa = {
    "nome": "Elisson",
    "idade": 28,
    "profissao": "Dev"
}

print("Dicionário:", pessoa)
print("Nome:", pessoa["nome"])

# Percorrendo dicionário
for chave, valor in pessoa.items():
    print(chave, ":", valor)


# ----------------------------------------------------------
# 9. TRATAMENTO DE ERROS (TRY / EXCEPT)
# ----------------------------------------------------------

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")


# ----------------------------------------------------------
# 10. ESTRUTURA PRINCIPAL DO ARQUIVO
# ----------------------------------------------------------

if __name__ == "__main__":
    print("Arquivo executado diretamente.")