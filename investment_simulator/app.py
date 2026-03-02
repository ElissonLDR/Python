from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def calcular_investimento(valor_inicial, aporte_mensal, taxa_juros, meses):
    historico = []
    saldo = valor_inicial

    for mes in range(1, meses + 1):
        juros = saldo * taxa_juros
        saldo += juros + aporte_mensal

        historico.append({
            "mes": mes,
            "saldo": round(saldo, 2),
            "juros": round(juros, 2)
        })

    return {
        "saldo_final": round(saldo, 2),
        "historico": historico
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    dados = request.get_json()

    valor_inicial = float(dados["valor_inicial"])
    aporte_mensal = float(dados["aporte_mensal"])
    taxa_juros = float(dados["taxa_juros"]) / 100
    meses = int(dados["meses"])

    resultado = calcular_investimento(
        valor_inicial,
        aporte_mensal,
        taxa_juros,
        meses
    )

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)