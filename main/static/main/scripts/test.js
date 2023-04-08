let modal = document.getElementById('myModalReport');
let modalBtn = document.getElementById("modalBtn");
let closeBtn = document.getElementsByClassName("close")[0];

// Показываем модальное окно через 1 секунду после загрузки страницы
window.onload = function() {
  modal.style.opacity = "1";
  setTimeout(function() {
    modal.style.opacity = "0";
  }, 5000); // модальное окно исчезнет через 5 секунд
};

closeBtn.onclick = function() {
  modal.style.opacity = "0";
};
