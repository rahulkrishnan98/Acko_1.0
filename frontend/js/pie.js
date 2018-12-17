  function piechart(data, company) {
  var points = [];
  for (i in data) {
    points.push({ y: data[i], label: i });
  }
  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    title: {
      text: "Hit ratio of products at " + company
    },
    data: [
      {
        type: "pie",
        startAngle: 240,
        yValueFormatString: '##0.00"%"',
        indexLabel: "{label} {y}",
        dataPoints: points
      }
    ]
  });
  chart.render();
}
