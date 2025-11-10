// Lista de funciones simples para generar ejercicios
const funciones = [
    { expr: "x**2", a: 0, b: 2 },
    { expr: "Math.sin(x)", a: 0, b: Math.PI },
    { expr: "x**3", a: 0, b: 1 },
    { expr: "2*x + 1", a: 0, b: 3 },
];

let areaCorrecta = 0;

function generarEjercicio() {
    // Elegir función aleatoria
    const f = funciones[Math.floor(Math.random() * funciones.length)];
    const { expr, a, b } = f;

    // Generar datos para la gráfica
    const x = [], y = [];
    const func = new Function("x", `return ${expr}`);
    for (let i = a; i <= b; i += 0.01) {
        x.push(i);
        y.push(func(i));
    }

    // Calcular área aproximada (trapecios)
    let area = 0;
    for (let i = 0; i < x.length - 1; i++) {
        area += ((y[i] + y[i + 1]) / 2) * (x[i + 1] - x[i]);
    }
    areaCorrecta = area;

    // Dibujar gráfica
    const trace1 = {
        x: x,
        y: y,
        type: 'scatter',
        mode: 'lines',
        name: `f(x) = ${expr}`,
        line: { color: '#1f77b4', width: 2 }
    };

    const trace2 = {
        x: [...x, b, a],
        y: [...y, 0, 0],
        fill: 'toself',
        fillcolor: 'rgba(0,128,0,0.3)',
        line: { color: 'transparent' },
        name: 'Área'
    };

    const layout = {
        title: `Gráfica de f(x) = ${expr}`,
        xaxis: { title: 'x' },
        yaxis: { title: 'f(x)' },
    };

    Plotly.newPlot("grafica", [trace1, trace2], layout);

    // Crear opciones aleatorias
    crearOpciones(area);
}

function crearOpciones(area) {
    const opciones = [];
    opciones.push(area);
    while (opciones.length < 3) {
        const error = (Math.random() * 2 - 1) * area * 0.3; // ±30%
        opciones.push(area + error);
    }

    // Mezclar opciones
    opciones.sort(() => Math.random() - 0.5);

    const div = document.getElementById("opciones");
    div.innerHTML = "";
    opciones.forEach(op => {
        const btn = document.createElement("button");
        btn.textContent = op.toFixed(2);
        btn.className = "bg-blue-500 text-white px-4 py-2 m-2 rounded hover:bg-blue-600";
        btn.onclick = () => verificarRespuesta(op);
        div.appendChild(btn);
    });

    document.getElementById("resultado").innerText = "";
}

function verificarRespuesta(opcion) {
    const resultado = document.getElementById("resultado");
    if (Math.abs(opcion - areaCorrecta) < 0.05 * areaCorrecta) {
        resultado.textContent = "✅ ¡Correcto! Muy bien.";
        resultado.style.color = "green";
    } else {
        resultado.textContent = "❌ Incorrecto. Intenta de nuevo.";
        resultado.style.color = "red";
    }
}

function nuevoJuego() {
    generarEjercicio();
}

window.onload = generarEjercicio;
