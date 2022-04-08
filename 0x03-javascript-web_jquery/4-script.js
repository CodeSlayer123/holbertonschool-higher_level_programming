#!/usr/bin/node
$('DIV#toggle_header').click(function () {
  if (!$(this).hasClass('red') && !$(this).hasClass('green')) {
    $(this).addClass('green');
  }
  if ($(this).hasClass('red')) {
    $(this).toggleClass('green');
  } else if ($(this).hasClass('green')) {
    $(this).toggleClass('red');
  }
});
