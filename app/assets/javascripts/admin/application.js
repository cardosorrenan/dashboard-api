// This is a manifest file that'll be compiled into application.js, which will include all the files
// listed below.
//
// Any JavaScript/Coffee file within this directory, lib/assets/javascripts, vendor/assets/javascripts,
// or vendor/assets/javascripts of plugins, if any, can be referenced here using a relative path.
//
// It's not advisable to add code directly here, but if you do, it'll appear at the bottom of the
// compiled file.
//
// Read Sprockets README (https://github.com/sstephenson/sprockets#sprockets-directives) for details
// about supported directives.
//
//= require jquery
//= require jquery_ujs
//= require bootstrap-sprockets
//= require cocoon
//= require_tree .

$(document).ready(function () {
  setFormMasks();
  $('#wizard').bwizard({
    nextBtnText: 'Próximo',
    backBtnText: 'Anterior'
  });
  App.init();

  var input = $('input.currency');
  input.css('text-align', 'right');
  input.maskMoney({
    prefix: '',
    thousands: ".",
    decimal: ","
  });

  $('.simple_form').on('submit', function (e) {
    $(this).find('input.currency').each(function () {
      $(this).val($(this).maskMoney('unmasked')[0]);
    });
  });

  $("input[type='checkbox'].boolean").bootstrapSwitch({
    onText: 'Sim',
    offText: 'Não'
  });
});

function setFormMasks() {
  $('.hint').tooltip();

  $("input.cpf").mask("999.999.999-99");
  $("input.cep-input").mask("99.999-999");
  $("input.phone").mask("(99) 9999-9999?9");
  $("input.time-field").mask("99:99");
  $("input.date").mask("99/99/9999");
  $("input.cnpj").mask("99.999.999/9999-99");
}

$(document).on('cocoon:after-insert', function (e, insertedItem) {
  setFormMasks();
  loadCepApi();
});
