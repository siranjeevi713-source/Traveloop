document.addEventListener('DOMContentLoaded', () => {
    initBudgetChart();
    initTripProgress();
});

function initBudgetChart() {
    const ctx = document.getElementById('budget-doughnut').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Transport', 'Stay', 'Food', 'Activities', 'Others'],
            datasets: [{
                data: [20000, 25000, 10000, 12000, 8000],
                backgroundColor: [
                    '#6c5ce7',
                    '#55efc4',
                    '#fdcb6e',
                    '#ff7675',
                    '#a29bfe'
                ],
                borderWidth: 0,
                cutout: '80%'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

function initTripProgress() {
    // Mini progress circles for trip cards
    const progressConfigs = [
        { id: 'progress-1', val: 60, color: '#6c5ce7' },
        { id: 'progress-2', val: 40, color: '#fab1a0' }
    ];

    progressConfigs.forEach(config => {
        const ctx = document.getElementById(config.id).getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [config.val, 100 - config.val],
                    backgroundColor: [config.color, 'rgba(0,0,0,0.05)'],
                    borderWidth: 0
                }]
            },
            options: {
                cutout: '70%',
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false }, tooltip: { enabled: false } }
            }
        });
    });
}
