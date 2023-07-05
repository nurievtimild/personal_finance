const data = document.currentScript.dataset;
let chart_amount = data.chartAmount;
chart_amount = JSON.parse(chart_amount);
var moneyChart = document.getElementById("moneyChart");
console.log(chart_amount);

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var moneyData = {
    labels: [
        "Расход",
        "Доход",
        "Перевод",
    ],
    datasets: [
        {
            data: chart_amount,
            backgroundColor: [
                "#FF6384",
                "#63FF84",
                "#611304",
            ]
        }]
};

var pieChart = new Chart(moneyChart, {
  type: 'pie',
  data: moneyData
});