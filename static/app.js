document.addEventListener('DOMContentLoaded', () => {
    const playButton = document.querySelector('.play-pause');
    if (playButton) {
        playButton.addEventListener('click', () => {
            const playing = playButton.getAttribute('data-playing') === 'true';
            playButton.setAttribute('data-playing', !playing);
            playButton.textContent = playing ? 'Play' : 'Pause';
        });
    }

    const trackRows = document.querySelectorAll('.track-row');
    trackRows.forEach((row) => {
        row.addEventListener('click', () => {
            trackRows.forEach((other) => other.classList.remove('is-active'));
            row.classList.add('is-active');
        });
    });
});
