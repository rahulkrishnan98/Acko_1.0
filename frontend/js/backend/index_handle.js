$(document).ready(function() {
  var cookie = getCookie("token");
  if (cookie == null) {
    location.href = "login.html";
  }
  $("#companies").hide();

  graph0();

  function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(";");
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == " ") c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }

  $("#but_complaint").click(function() {
    if ($.length == 0) {
      alert("please select a company!!");
    } else {
      $("#myModal").modal("toggle");
      $.post(
        "http://127.0.0.1:8000/accounts/company_sub/",
        {
          companies: JSON.stringify($("#DDLActivites").val()),
          sub_product: $("#sub").val()
        },
        function(data) {
          console.log(data);
          bargraph(data);
          $("#myModal").modal("toggle");
          $("#chartContainer").show();
        }
      ).fail(function(data) {
        console.log(data);
      });
    }

    console.log($("#DDLActivites").val());
  });

  $("#logout").click(function() {
    console.log("logged out");
    delete_cookie("token");
    location.href = "login.html";
  });

  function delete_cookie(name) {
    document.cookie = name + "=;Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
  }

  $("#graph1").click(function() {
    graph0();
  });

  $("#graph3").click(function() {
    graph3();
  });

  $("#graph5").click(function() {
    graph5();
  });

  function graph0() {
    $("#companies").hide();
    $("#chartContainer").show();
    $("#myModal").modal("toggle");
    $.get("http://127.0.0.1:8000/accounts/product/", {}, function(data) {
      bargraph(data.message, 1);
      $("#myModal").modal("toggle");
    }).fail(function(data) {
      location.href = "login.html";
    });
  }

  function graph3() {
    $("#companies").hide();
    $("#chartContainer").show();
    $("#myModal").modal("toggle");
    $.get("http://127.0.0.1:8000/accounts/company_dispute/", {}, function(
      data
    ) {
      bargraph(data, 3);
      $("#myModal").modal("toggle");
    }).fail(function(data) {
      location.href = "login.html";
    });
  }

  function graph5() {
    $("#companies").hide();
    $("#chartContainer").show();
    $("#myModal").modal("toggle");
    $.post(
      "http://127.0.0.1:8000/accounts/performance/",
      {
        company: "Bank of America"
      },
      function(data) {
        console.log(data);
        var points = {};
        for (var k in data) {
          var company = k;
          points[data[k][0]] = 2012;
          points[data[k][1]] = 2013;
          points[data[k][2]] = 2014;
          points[data[k][3]] = 2015;
          break;
        }
        var rv = [];
        bar(points);
      }
    ).fail(function(data) {
      console.log(data);
    });
  }

  function bar(data) {
    var points = [];
    for (i in data) {
      points.push({ x: data[i], y: parseInt(i) });
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
    $("#myModal").modal("toggle");
    chart.render();
  }
});
