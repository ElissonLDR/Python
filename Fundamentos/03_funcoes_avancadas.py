# ==========================================================
# PYTHON - NÍVEL INTERMEDIÁRIO
# Funções avançadas e conceitos importantes
# ==========================================================


# ----------------------------------------------------------
# 1. FUNÇÃO COMO OBJETO
# ----------------------------------------------------------

def saudacao(nome):
    return f"Olá, {nome}"

# Função pode ser armazenada em variável
funcao = saudacao

print(funcao("Elisson"))


# ----------------------------------------------------------
# 2. FUNÇÃO DENTRO DE FUNÇÃO (Função Aninhada)
# ----------------------------------------------------------

def calculadora(operacao):

    def soma(a, b):
        return a + b

    def multiplicacao(a, b):
        return a * b

    if operacao == "soma":
        return soma
    elif operacao == "multiplicacao":
        return multiplicacao


operacao_escolhida = calculadora("soma")
print("Resultado:", operacao_escolhida(10, 5))


# ----------------------------------------------------------
# 3. FUNÇÃO COMO PARÂMETRO (Higher Order Function)
# ----------------------------------------------------------

def executar(funcao, a, b):
    return funcao(a, b)

print("Executar soma:",
      executar(lambda x, y: x + y, 3, 7))


# ----------------------------------------------------------
# 4. DECORATOR SIMPLES
# ----------------------------------------------------------

def log_execucao(funcao):
    def wrapper():
        print("Executando função...")
        funcao()
        print("Finalizado.")
    return wrapper


@log_execucao
def mensagem():
    print("Olá mundo!")

mensagem()


# ----------------------------------------------------------
# 5. GERADORES (yield)
# ----------------------------------------------------------

def gerar_numeros(limite):
    for i in range(limite):
        yield i  # Retorna um valor por vez


for numero in gerar_numeros(5):
    print("Gerador:", numero)


# ----------------------------------------------------------
# 6. LIST COMPREHENSION AVANÇADA
# ----------------------------------------------------------

numeros = [1, 2, 3, 4, 5]

quadrados_pares = [x**2 for x in numeros if x % 2 == 0]
print("Quadrados pares:", quadrados_pares)


# ----------------------------------------------------------
# 7. DICIONÁRIO COMPREHENSION
# ----------------------------------------------------------

dicionario = {x: x**2 for x in range(5)}
print("Dicionário:", dicionario)


# ----------------------------------------------------------
# 8. TRY / EXCEPT COM ELSE E FINALLY
# ----------------------------------------------------------

try:
    valor = int("10")
except ValueError:
    print("Erro de conversão.")
else:
    print("Conversão bem sucedida:", valor)
finally:
    print("Bloco final executado.")


# ----------------------------------------------------------
# FIM
# ----------------------------------------------------------

print("\nArquivo intermediário executado com sucesso.")