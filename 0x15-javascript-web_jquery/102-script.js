$('document').ready(function () {
  const page = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').on('click', function () {
    const url = page + $('INPUT#language_code').val();
    $.get(url, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
