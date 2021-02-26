var click_count = 0
var auth_token = 'TesTeTokEn'
var IS_NAMES = {
    'SP':'Service Providers',
    'TR':'Transportation',
    'OIL/HSE':'Oil & Gas | Maximo Health, Safety and Environment',//OilAndGasAndHSE
    'ACM':'Asset Configuration Mananger',
    'AVI':'Aviation',
    'UTI':'Utilities',
    'NUC':'Nuclear'
}

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }

function triggerJob(_btn){
    var id = _btn.id
    var _class = _btn.classList

    var IS = IS_NAMES[_class[1]]
    var IS_SG = _class[1]
    var VER = _class[2]
    console.log('Nome da IS = ' + IS);
    console.log('Versão da IS = ' + VER);

    var page
    if(click_count == 0){
        
        page = window.open('http://auto:113b7ebf8a0d5069480fba8b545328259c@localhost:8080/job/Python_Pipe_00//build?token='+auth_token);
        page.close();
        click_count++; 
    }
}
