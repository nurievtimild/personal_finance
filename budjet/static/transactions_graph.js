const ctx = document.getElementById('balance_change');
let day_balance_change = data.chartAmount;
day_balance_change = JSON.parse(day_balance_change);

new Chart(ctx, {
type: 'line',
data: {
  labels: ['Red', 'Blue', 'Yellow'],
  datasets: [{
    label: 'Изменение баланса по дням',
    data: day_balance_change,
    borderWidth: 1
  }]
},
options: {
  scales: {
    y: {
      beginAtZero: true
    }
  }
}
});