function bargraph(data, param) {
  var points = [];
  for (i in data) {
    points.push({ y: data[i], label: i });
  }

  console.log(points);
  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    theme: "light1", // "light1", "light2", "dark1", "dark2"
    title: {
      text: "Complaint Count over Registered Products"
    },
    data: [
      {
        click: function(e) {
          if (param == 1) {
            graph1(e.dataPoint.label);
          } else if (param == 2) {
            graph2(e.dataPoint.label);
          } else if (param == 3) {
            graph3(e.dataPoint.label);
          }
        },
        type: "column",
        dataPoints: points
      }
    ]
  });
  chart.render();
}

function graph1(prod) {
  $("#myModal").modal("toggle");
  prod = prod.split(" ").join("_");
  $.get("http://127.0.01:8000/accounts/sub_product/" + prod + "/", {}, function(
    data
  ) {
    $("#myModal").modal("toggle");
    if (data.message) {
      alert(data.message);
    } else {
      bargraph(data, 2);
    }
  }).fail(function(data) {
    location.href = "login.html";
  });
}

function graph2(prod) {
  //   make the secon click graph here
  document.getElementById("sub").value = prod;
  $("#myModal").modal("toggle");
  $("#companies").show();
  $("#chartContainer").hide();
  $("#myModal").modal("toggle");
}

function graph3(company) {
  $("#myModal").modal("toggle");
  $.post(
    "http://127.0.0.1:8000/accounts/product_dispute/",
    {
      company: company
    },
    function(data) {
      piechart(data, company);
      $("#myModal").modal("toggle");
    }
  ).fail(function(data) {
    console.log(data);
    //   location.href = "login.html";
  });
}
