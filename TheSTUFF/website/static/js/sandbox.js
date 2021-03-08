/*      function that acts as an intermidiate between the form pages and the server, 
passing the necessary inputs for the code and sending the output for the 
desired destination */
function getPythonOutput(inputArgs, outputId) {
    $.ajax({
        url: 'sandbox',
        type: 'POST',
        data: inputArgs,
        success: function (outputPassword) {
            $(outputId).val(outputPassword);
        }
    });
}

/* Senhas aleatorias */
function getPasswordGenPython() {
    let data = JSON.stringify({
        type: 'password_generator',
        L: $('#PW_w_LC').is(":checked") ? 1 : 0,
        U: $('#PW_w_UC').is(":checked") ? 1 : 0,
        N: $('#PW_w_NC').is(":checked") ? 1 : 0,
        S: $('#PW_w_SC').is(":checked") ? 1 : 0,
        pwl: $('#passwordLen').val()
    })
    getPythonOutput(data, '#pswdOutput')
}
function getPasswordGenSourcePython() {
    let scrTgl = document.getElementById('sourceToggle');
    if (document.getElementById('passwordGenSourcePython').classList.contains("show")) {
        document.getElementById('passwordGenSourcePython').classList.remove("show");
    }
    else {
        $.ajax({
            url: 'sandbox/python/getPasswordGenSource',
            type: 'POST',
            success: function (outputSource) {
                document.getElementById('passwordGenSourcePython').innerHTML = "<pre>" + outputSource + "</pre>"
            }
        });
        document.getElementById('passwordGenSourcePython').classList.add("show");

    }
}

/* Documentos pessoais */
function checkDocumentCPF_python() {
    if (document.getElementById('DocumentCPFSourcePython').classList.contains("show")) {
        document.getElementById('DocumentCPFSourcePython').classList.remove("show");
    }
    else {
        $.ajax({
            url: 'sandbox/python/getDocumentCPFSource',
            type: 'POST',
            success: function (outputSource) {
                document.getElementById('DocumentCPFSourcePython').innerHTML = "<pre>" + outputSource + "</pre>"
            }
        });
        document.getElementById('DocumentCPFSourcePython').classList.add("show");

    }
}

function getNewCPF_python(){
    let data = JSON.stringify({
        type: 'doc_cpf',
        action: 'new',        
        formated: $('#formatedCPF').is(":checked") ? true : false,
    })
    getPythonOutput(data,'#outputCPF')
}

function checkDocumentCPF_python(){
    let data = JSON.stringify({
        type: 'doc_cpf',
        action: 'check',        
        input: $('#InputCPF').val()
    })
    getPythonOutput(data,'#outputCPF')
}