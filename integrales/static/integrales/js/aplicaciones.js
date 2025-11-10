function graficar() {
    const expr = document.getElementById("funcion").value;
    const a = parseFloat(document.getElementById("a").value);
    const b = parseFloat(document.getElementById("b").value);

    const x = [];
    const y = [];

    // Generar puntos
    for (let i = a; i <= b; i += 0.01) {
        try {
            // Crear un contexto donde x = i
            const f = new Function("x", `return ${expr.replaceAll("^", "**")}`);
            const val = f(i);
            x.push(i);
            y.push(val);
        } catch (e) {
            alert("Error en la función. Usa una sintaxis válida, por ejemplo: x**2 o Math.sin(x)");
            return;
        }
    }

    const trace1 = {
        x: x,
        y: y,
        type: 'scatter',
        mode: 'lines',
        name: 'f(x)',
        line: { color: '#1f77b4', width: 2 }
    };

    const trace2 = {
        x: [...x, b, a],
        y: [...y, 0, 0],
        fill: 'toself',
        fillcolor: 'rgba(44, 160, 44, 0.3)',
        line: { color: 'transparent' },
        name: 'Área bajo la curva'
    };

    const layout = {
        title: `Gráfica de f(x) = ${expr}`,
        xaxis: { title: 'x', zeroline: true },
        yaxis: { title: 'f(x)', zeroline: true },
    };

    Plotly.newPlot("grafica", [trace1, trace2], layout);
}

function verificarRespuesta(valor) {
    const correcta = 2.67;
    const resultado = document.getElementById("resultado");
    if (Math.abs(valor - correcta) < 0.1) {
        resultado.innerHTML = "✅ ¡Correcto! El área es aproximadamente 2.67.";
        resultado.style.color = "green";
    } else {
        resultado.innerHTML = "❌ Incorrecto, inténtalo de nuevo.";
        resultado.style.color = "red";
    }
}
