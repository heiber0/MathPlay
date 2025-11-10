// (Opcional) Podrías agregar efectos de sonido o mensajes al girar tarjetas
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        card.classList.toggle('flipped');
    });
});
