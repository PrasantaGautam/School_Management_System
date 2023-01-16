function openForm() {
  document.getElementById("myFormAdd").style.display = "block";
}

function closeForm() {
  document.getElementById("myFormAdd").style.display = "none";
}
function openFormEdit(id) {
  var token = id;
  window.location.href = '/tea_id/'+token;

}
  
function closeFormEdit() {
  let url = window.location.href;
  const urlarr = url.split("/");
  let clsTkn = urlarr[4].split("@")
  clsTkn = clsTkn[0]+'@cls'
  if (urlarr[3]=='std_id')
  {
    window.location.href = '/class_token/'+clsTkn;
  }
  if (urlarr[3]=='tea_id')
  {
    window.location.href = '/teachers/';
  }
}

function openstdFormEdit(id) {
  var token = id;
  window.location.href = '/std_id/'+token;
}