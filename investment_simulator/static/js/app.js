let grafico = null;

document.getElementById("form-investimento")
    .addEventListener("submit", async function (e) {

        e.preventDefault();

        const valorInicial = parseFloat(document.getElementById("valor_inicial").value);
        const aporteMensal = parseFloat(document.getElementById("aporte_mensal").value);
        const taxaJuros = parseFloat(document.getElementById("taxa_juros").value);
        const meses = parseInt(document.getElementById("meses").value);

        const resposta = await fetch("/calcular", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                valor_inicial: valorInicial,
                aporte_mensal: aporteMensal,
                taxa_juros: taxaJuros,
                meses: meses
            })
        });

        const dados = await resposta.json();

        atualizarResultado(dados.saldo_final);
        atualizarGrafico(dados.historico);
    });


function atualizarResultado(saldoFinal) {
    document.getElementById("saldo_final").innerText =
        "R$ " + saldoFinal.toLocaleString("pt-BR");
}


function atualizarGrafico(historico) {

    const labels = historico.map(item => "Mês " + item.mes);
    const saldos = historico.map(item => item.saldo);

    const ctx = document.getElementById("graficoInvestimento").getContext("2d");

    if (grafico) {
        grafico.destroy();
    }

    grafico = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Evolução do Investimento",
                data: saldos,
                borderWidth: 2,
                tension: 0.2
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
}