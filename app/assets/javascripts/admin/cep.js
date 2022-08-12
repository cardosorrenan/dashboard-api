function loadCepApi() {
    $(".cep-input").on('blur', function() {
        //Nova variável "cep" somente com dígitos.
        var cep = $(this).val().replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                var inputRua = $(this).closest('.nested-fields').find('.rua-input').first()
                var inputBairro = $(this).closest('.nested-fields').find('.bairro-input').first()
                var inputCidade = $(this).closest('.nested-fields').find('.cidade-input').first()
                var inputUf = $(this).closest('.nested-fields').find('.uf-input').first()

                //Preenche os campos com "..." enquanto consulta webservice.
                inputRua.val("...")
                inputBairro.val("...")
                inputCidade.val("...")
                inputUf.val("...")

                //Consulta o webservice viacep.com.br/
                $.getJSON("//viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                    if (!("erro" in dados)) {
                        //Atualiza os campos com os valores da consulta.
                        inputRua.val(dados.logradouro);
                        inputBairro.val(dados.bairro);
                        inputCidade.val(dados.localidade);
                        inputUf.val(dados.uf);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
        } //end if.
    });
}

$(document).ready(function() {
  loadCepApi();
});