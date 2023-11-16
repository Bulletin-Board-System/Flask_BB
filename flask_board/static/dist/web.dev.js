"use strict";

var sign = document.querySelector("#sign");
var create = document.querySelector("#create");
var del = document.querySelector("#del");
var update = document.querySelector("#update");
sign.addEventListener("click", function () {
  $.ajax({
    type: 'POST',
    url: '/sign'
  }).fail(function (result) {
    alert(result);
  });
});
update.addEventListener("click", function () {
  $.ajax({
    type: 'UPDATE',
    url: '/update'
  }).fail(function (result) {
    alert(result);
  });
});
create.addEventListener("click", function () {
  $.ajax({
    type: 'POST',
    url: '/create'
  }).fail(function (result) {
    alert(result);
  });
});
del.addEventListener("click", function () {
  $.ajax({
    type: 'DELETE',
    url: '/delete'
  }).fail(function (result) {
    alert(result);
  });
});
//# sourceMappingURL=web.dev.js.map
