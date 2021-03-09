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
/* CPF */
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

function getNewCPF_python() {
    let data = JSON.stringify({
        type: 'doc_cpf',
        action: 'new',
        formated: $('#formatedCPF').is(":checked") ? true : false,
    })
    getPythonOutput(data, '#outputCPF')
}

function checkDocumentCPF_python() {
    $.ajax({
        url: 'sandbox',
        type: 'POST',
        data: JSON.stringify({
            type: 'doc_cpf',
            action: 'check',
            input: $('#InputCPF').val()
        }),
        success: function (output) {
            let tag = document.getElementById("ValidationOutputCPF")
            tag.innerHTML = output;
            if(output == 'All OK') tag.style.color="green";
            else if(output == 'Invalid') tag.style.color="orange";
            else tag.style.color="yellow";
        }
    });
}

function getCPFSourcePython() {
    let scrTgl = document.getElementById('sourceToggle');
    if (document.getElementById('DocumentCPFSourcePython').classList.contains("show")) {
        document.getElementById('DocumentCPFSourcePython').classList.remove("show");
    }
    else {
        $.ajax({
            url: 'sandbox/python/getCPFSource',
            type: 'POST',
            success: function (outputSource) {
                document.getElementById('DocumentCPFSourcePython').innerHTML = "<pre>" + outputSource + "</pre>"
            }
        });
        document.getElementById('DocumentCPFSourcePython').classList.add("show");

    }
}
/* RG */
function checkDocumentRG_python() {
    if (document.getElementById('DocumentRGSourcePython').classList.contains("show")) {
        document.getElementById('DocumentRGSourcePython').classList.remove("show");
    }
    else {
        $.ajax({
            url: 'sandbox/python/getDocumentRGSource',
            type: 'POST',
            success: function (outputSource) {
                document.getElementById('DocumentRGSourcePython').innerHTML = "<pre>" + outputSource + "</pre>"
            }
        });
        document.getElementById('DocumentRGSourcePython').classList.add("show");

    }
}

function getNewRG_python() {
    let data = JSON.stringify({
        type: 'doc_rg',
        action: 'new',
        formated: $('#formatedRG').is(":checked") ? true : false,
    })
    getPythonOutput(data, '#outputRG')
}

function checkDocumentRG_python() {
    $.ajax({
        url: 'sandbox',
        type: 'POST',
        data: JSON.stringify({
            type: 'doc_rg',
            action: 'check',
            input: $('#InputRG').val()
        }),
        success: function (output) {
            let tag = document.getElementById("ValidationOutputRG")
            tag.innerHTML = output;
            if(output == 'All OK') tag.style.color="green";
            else if(output == 'Invalid') tag.style.color="orange";
            else tag.style.color="yellow";
        }
    });
}

function getRGSourcePython() {
    let scrTgl = document.getElementById('sourceToggle');
    if (document.getElementById('DocumentRGSourcePython').classList.contains("show")) {
        document.getElementById('DocumentRGSourcePython').classList.remove("show");
    }
    else {
        $.ajax({
            url: 'sandbox/python/getRGSource',
            type: 'POST',
            success: function (outputSource) {
                document.getElementById('DocumentRGSourcePython').innerHTML = "<pre>" + outputSource + "</pre>"
            }
        });
        document.getElementById('DocumentRGSourcePython').classList.add("show");

    }
}