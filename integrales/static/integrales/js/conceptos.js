// Configurar gráfico inicial
const ctx = document.getElementById('grafica').getContext('2d');

function generarDatos(limiteB) {
    let x = [];
    let y = [];
    for (let i = 0; i <= limiteB * 10; i++) {
        let xi = i / 10;
        x.push(xi);
        y.push(xi * xi); // f(x) = x^2
    }
    return { x, y };
}

let limiteB = 5;
let datos = generarDatos(limiteB);

let chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: datos.x,
        datasets: [{
            label: 'f(x) = x²',
            data: datos.y,
            borderColor: '#4e73df',
            borderWidth: 2,
            fill: true,
            backgroundColor: 'rgba(78, 115, 223, 0.2)',
            tension: 0.2
        }]
    },
    options: {
        scales: {
            x: { title: { display: true, text: 'x' } },
            y: { title: { display: true, text: 'f(x)' } }
        }
    }
});

// Controlar el rango del límite superior
const slider = document.getElementById('limiteB');
const valorB = document.getElementById('valorB');

slider.addEventListener('input', () => {
    limiteB = parseFloat(slider.value);
    valorB.textContent = limiteB;
    datos = generarDatos(limiteB);
    chart.data.labels = datos.x;
    chart.data.datasets[0].data = datos.y;
    chart.update();
});
