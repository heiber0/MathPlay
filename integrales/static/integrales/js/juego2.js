const items = document.querySelectorAll('.item');
const dropzones = document.querySelectorAll('.dropzone');
const resultado = document.getElementById('resultado');
const reiniciar = document.getElementById('reiniciar');

let aciertos = 0;

items.forEach(item => {
    item.addEventListener('dragstart', e => {
        e.dataTransfer.setData('match', item.dataset.match);
        item.classList.add('dragging');
    });

    item.addEventListener('dragend', () => {
        item.classList.remove('dragging');
    });
});

dropzones.forEach(zone => {
    zone.addEventListener('dragover', e => e.preventDefault());

    zone.addEventListener('drop', e => {
        const match = e.dataTransfer.getData('match');

        if (zone.dataset.match === match && !zone.classList.contains('matched')) {
            zone.classList.add('matched');
            zone.style.background = '#55efc4';
            zone.innerHTML += ' ✅';
            aciertos++;
            resultado.textContent = `Correcto: ${aciertos}/4`;

            if (aciertos === 4) {
                resultado.textContent = '🎉 ¡Excelente! Has emparejado todas las funciones correctamente.';
            }
        } else {
            zone.style.background = '#fab1a0';
            resultado.textContent = '❌ Esa no es la integral correcta.';
            setTimeout(() => zone.style.background = '', 800);
        }
    });
});

reiniciar.addEventListener('click', () => {
    location.reload();
});
