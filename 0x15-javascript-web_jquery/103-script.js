$('document').ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    sayHello();
  });
  $('INPUT#language_code').on('focus', function () {
    $('INPUT#language_code').on('keydown', function (event) {
      if (event.which === 13) {
        sayHello();
      }
    });
  });
});

function sayHello () {
  const page = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const url = page + $('INPUT#language_code').val();
  $.get(url, function (data) {
    $('DIV#hello').html(data.hello);
  });
}
