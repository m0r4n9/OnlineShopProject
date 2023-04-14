let modal = document.getElementById('myModalReport');
let modalBtn = document.getElementById("modalBtn");
let closeBtn = document.getElementsByClassName("close")[0];

// Показываем модальное окно через 1 секунду после загрузки страницы
window.onload = function () {
  modal.style.opacity = "1";
  setTimeout(function () {
    modal.style.opacity = "0";
  }, 5000); // модальное окно исчезнет через 5 секунд
};


$(document).ready(function () {
  $('.dropdown').hover(function () {
    $(this).find('.dropdown-menu').toggleClass('show');
  });
});


$(document).ready(function() {
  // При клике на кнопку "Открыть модальное окно"
  $("#open-modal").click(function() {
    // Показываем модальное окно
    $("#modalReview").show();
  });

  // При клике на крестик (закрытие модального окна)
  $(".close-review").click(function() {
    // Скрываем модальное окно
    $("#modalReview").hide();
  });
});

$(document).ready(function() {
  // При клике на кнопку "Открыть модальное окно"
  $("#open-listReview").click(function() {
    // Показываем модальное окно
    $("#listReview").show();
  });

  // При клике на крестик (закрытие модального окна)
  $(".close-listReview").click(function() {
    // Скрываем модальное окно
    $("#listReview").hide();
  });
});

