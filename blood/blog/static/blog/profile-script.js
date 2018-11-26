var input = document.querySelectorAll("input");

function bigForm(){
  alert("You can edit Blood Group, Date of Birth and Last Donated date only ONCE.");
  var input = document.querySelectorAll("input");
  var form = document.getElementById("register-mid");
  var button = document.getElementById("fancy");
  button.style.display="none";
  form.style.display = "flex";
  input[5].checked= true;
}

function smallForm(){
  var input = document.querySelectorAll("input");
  var form = document.getElementById("register-mid");
  var button = document.getElementById("fancy");
  button.style.display="none";
  form.style.display = "flex";
  input[1].value = "{{ user.profile.mobile_number }}";
  input[2].value = "{{ user.profile.weight }}" ;
  input[3].checked= true;
}