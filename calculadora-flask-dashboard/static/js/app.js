const display = document.getElementById("display");
const buttons = document.querySelectorAll(".btn");
const tooltip = document.getElementById("tooltip");

let expression = "";
let lastResult = null;
let justCalculated = false;

buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        const number = btn.dataset.number;
        const action = btn.dataset.action;

        const ops = {
            add: "+",
            subtract: "-",
            multiply: "*",
            divide: "/",
            percent: "/100"
        };

        if (number !== undefined) {
            if (justCalculated) {
                expression = number === "." ? "0." : number;
                justCalculated = false;
            } else {
                expression += number;
            }
            display.textContent = expression.replace(/\./g, ",");
            return;
        }

        if (action === "clear") {
            expression = "";
            display.textContent = "0";
            return;
        }

        if (ops[action]) {
            if (justCalculated && lastResult !== null) {
                expression = lastResult.toString();
                justCalculated = false;
            }
            expression += ops[action];
            display.textContent = expression.replace(/\./g, ",");
            return;
        }

        if (action === "equal") {
            fetch("/calcular", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ expressao: expression })
            })
            .then(res => res.json())
            .then(data => {
                if (data.resultado !== undefined) {
                    display.textContent = (data.expressao + " = " + data.resultado).replace(/\./g, ",");
                    lastResult = data.resultado;
                    expression = data.resultado.toString();
                    justCalculated = true;
                    atualizarPainel();
                }
            });
        }
    });
});

function atualizarPainel() {
    fetch("/painel")
    .then(res => res.json())
    .then(data => {

        document.getElementById("tempo_online").textContent = data.tempo_online;
        document.getElementById("total_acessos").textContent = data.total_acessos;
        document.getElementById("total_calculos").textContent = data.total_calculos;
        document.getElementById("ultimo_tempo").textContent = data.ultimo_tempo;
        document.getElementById("alerta").textContent = data.ultimo_alerta;

        document.getElementById("humor").textContent = data.humor;
        document.getElementById("padrao").textContent = data.padrao;
        document.getElementById("maior_resultado").textContent = data.maior_resultado ?? "-";
        document.getElementById("menor_resultado").textContent = data.menor_resultado ?? "-";
        document.getElementById("maior_expressao").textContent = data.maior_expressao || "-";

        const lista = document.getElementById("auditoria");
        lista.innerHTML = "";
        data.auditoria.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `${item.hora} - ${item.texto}`;
            lista.appendChild(li);
        });
    });
}

document.querySelectorAll(".info-icon").forEach(icon => {
    icon.addEventListener("mouseenter", e => {
        tooltip.textContent = icon.dataset.text;
        tooltip.style.display = "block";
        tooltip.style.top = (e.pageY + 10) + "px";
        tooltip.style.left = (e.pageX + 10) + "px";
    });
    icon.addEventListener("mouseleave", () => {
        tooltip.style.display = "none";
    });
});
