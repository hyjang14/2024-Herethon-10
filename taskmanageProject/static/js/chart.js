document.addEventListener('DOMContentLoaded', () => {
    const likedTeamData = JSON.parse(document.getElementById('liked-team-data').textContent);
    const otherTeamData = JSON.parse(document.getElementById('other-team-data').textContent);
    const TeamData = JSON.parse(document.getElementById('team_data').textContent);

    function createDoughnutChart(canvasId, data) {
        const hasCompletedTasks = data.some(d => d.completed_tasks > 0);
        const chartData = hasCompletedTasks ? data.map(d => d.completed_tasks) : [1];
        //const chartLabels = hasCompletedTasks ? data.map(d => d.username) : ['No completed tasks'];
        const chartColors = hasCompletedTasks ? ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"] : ["#C0C0C0"];

        new Chart(document.getElementById(canvasId), {
            type: 'doughnut',
            data: {
                //labels: chartLabels,  
                datasets: [{
                    backgroundColor: chartColors,
                    data: chartData
                }]
            },
            options: {
                tooltips: {
                    callbacks: {
                        label: function(tooltipItem, chartData) {
                            if (!hasCompletedTasks) {
                                return 'No completed tasks';
                            }
                            const dataset = chartData.datasets[tooltipItem.datasetIndex];
                            const label = chartData.labels[tooltipItem.index];
                            const value = dataset.data[tooltipItem.index];
                            return `${label}: ${value}`;
                        }
                    }
                }
            }
        });
    }

    for (const teamId in likedTeamData) {
        createDoughnutChart(`doughnut-chart-${teamId}`, likedTeamData[teamId]);
    }

    for (const teamId in otherTeamData) {
        createDoughnutChart(`doughnut-chart-${teamId}`, otherTeamData[teamId]);
    }
});

/*
// 차트 생성
new Chart(document.getElementById("doughnut-chart"), {
    type: 'doughnut',
    data: {
        datasets: [
            {
                backgroundColor: ["var(--gray)", "var(--gray)", "var(--gray)", "var(--gray)", "#C22370"],
                data: [10, 20, 10, 10, 50]
            }
        ]
    },
});
*/