$('.send-it').click(function () {
    $.ajax({
        url: 'sandbox',
        type: 'POST',
        data: JSON.stringify({
            L: $('#PW_w_LC').is(":checked") ? 1 : 0,
            U: $('#PW_w_UC').is(":checked") ? 1 : 0,
            N: $('#PW_w_NC').is(":checked") ? 1 : 0,
            S: $('#PW_w_SC').is(":checked") ? 1 : 0,
            pwl: $('#passwordLen').val()
        }),
        success: function (outputPassword) {
            $('#pswdOutput').val(outputPassword);
        }
    });
});