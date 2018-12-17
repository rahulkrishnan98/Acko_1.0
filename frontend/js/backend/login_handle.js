$(document).ready(function() {
  if (getCookie("token")) {
    location.href = "index.html";
  }
  $("#login").click(function() {
    console.log("this is a sample");
    $(this).disabled = true;
    $(this).text(" loading... please wait");
    var formData = new FormData($("#login-form")[0]);
    $.post(
      "http://127.0.0.1:8000/accounts/login/",
      {
        user: $("#user").val(),
        password: $("#password").val()
      },
      function(data) {
        if (data.hasOwnProperty("token")) {
          // redirect to logged-in page
          setCookie("token", data.token, 7);
          location.href = "index.html";
        }
      }
    ).fail(function(data) {
      if (data.responseJSON.hasOwnProperty("error")) {
        alert(data.responseJSON.message);
      } else {
        if (data.responseJSON.hasOwnProperty("user")) {
          alert("Username:" + data.responseJSON.user);
        } else if (data.responseJSON.hasOwnProperty("password")) {
          alert("Password: " + data.responseJSON.password);
        }

        $("#login").text("login");
        $(this).disabled = false;
      }
    });
  });

  function setCookie(name, value, days) {
    var expires = "";
    if (days) {
      var date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
  }

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
});
