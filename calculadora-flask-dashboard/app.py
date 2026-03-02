from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

inicio_servidor = time.time()
total_acessos = 0
total_calculos = 0
ultimo_tempo = 0
auditoria = []
ultimo_alerta = ""

maior_resultado = None
menor_resultado = None
maior_expressao = ""
ultima_expressao = ""

humor = "Iniciando"
padrao = "Nenhum"

@app.route("/")
def home():
    global total_acessos
    total_acessos += 1
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    global total_calculos, ultimo_tempo
    global maior_resultado, menor_resultado
    global maior_expressao, ultima_expressao
    global humor, padrao, ultimo_alerta

    inicio = time.time()
    data = request.get_json()
    expressao = data.get("expressao")

    try:
        resultado = eval(expressao)
        total_calculos += 1
        ultimo_tempo = round((time.time() - inicio) * 1000, 2)

        auditoria.append({
            "texto": f"{expressao} = {resultado}",
            "hora": time.strftime("%H:%M:%S")
        })

        if maior_resultado is None or resultado > maior_resultado:
            maior_resultado = resultado

        if menor_resultado is None or resultado < menor_resultado:
            menor_resultado = resultado

        if len(expressao) > len(maior_expressao):
            maior_expressao = expressao

        if total_calculos < 5:
            humor = "Aquecendo"
        elif total_calculos < 15:
            humor = "Ativo"
        else:
            humor = "Intenso"

        if ultima_expressao == expressao:
            padrao = "Repetição"
        elif expressao.count("*") >= 2:
            padrao = "Multiplicações"
        elif expressao.count("/") >= 2:
            padrao = "Divisões"
        else:
            padrao = "Normal"

        ultima_expressao = expressao

        if resultado < 0:
            ultimo_alerta = "Negativo"
        elif resultado > 100000:
            ultimo_alerta = "Muito alto"
        else:
            ultimo_alerta = "Ok"

        return jsonify({
            "expressao": expressao,
            "resultado": resultado
        })

    except:
        ultimo_alerta = "Erro"
        return jsonify({"erro": "Expressão inválida"}), 400


@app.route("/painel")
def painel():
    return jsonify({
        "tempo_online": round(time.time() - inicio_servidor),
        "total_acessos": total_acessos,
        "total_calculos": total_calculos,
        "ultimo_tempo": ultimo_tempo,
        "auditoria": auditoria[-5:],
        "ultimo_alerta": ultimo_alerta,
        "humor": humor,
        "padrao": padrao,
        "maior_resultado": maior_resultado,
        "menor_resultado": menor_resultado,
        "maior_expressao": maior_expressao
    })

if __name__ == "__main__":
    app.run(debug=True)