// confetti.js
function startConfetti() {
    const confettiElement = document.createElement('div');
    confettiElement.classList.add('confetti');
    document.body.appendChild(confettiElement);

    for (let i = 0; i < 100; i++) {
        const confettiPiece = document.createElement('div');
        confettiPiece.classList.add('confetti-piece');
        confettiPiece.style.left = `${Math.random() * 100}%`;
        confettiPiece.style.backgroundColor = getRandomColor();
        confettiPiece.style.animationDelay = `${Math.random() * 2}s`;
        confettiPiece.style.opacity = `${Math.random() + 0.5}`;
        confettiPiece.style.transform = `rotate(${Math.random() * 360}deg)`;
        confettiElement.appendChild(confettiPiece);
    }

    setTimeout(() => {
        confettiElement.remove();
    }, 6000);
}

function getRandomColor() {
    const colors = ['#f9c74f', '#f94144', '#90be6d', '#577590', '#f8961e', '#43aa8b', '#4d908e'];
    return colors[Math.floor(Math.random() * colors.length)];
}
