$(function(){

    // password checker
	var c_password = $("#id_password2");
    var password = $("#id_password1")
    password.after("<div class='row password-checker'> <div class='col-3'></div> <div class='col-2'><div id='week'></div><small>week</small></div>  <div class='col-3'><div id='strong'></div><small>strong</small></div> <div class='col-2'><div id='hard'></div><small style='margin-left:-32px'>hard</small></div></div>")
    var week = $("#week");
    var strong = $("#strong");
    var hard = $("#hard");
    $(".password-checker").css({
        'margin-top': '7px',
    }).hide()
    password.keydown(function(event){
        $(".password-checker").show();
    })
    password.keyup(function(event){
        var value = $(this).val().trim();
        var Regx = /[a-z]/g
        var Regx2 = /[0-9]/g
        var Regx3 = /[@#%&_$^(){}!?><+=]/g
        var Regx4 = /[A-Z]/g
        // week 
        if(value){
            week.css({
                'background': '#ff0000',
            })
        }else{
            week.css({
                'background': '#e0e3d7',
            })
        }
        // strong 
        var strongRegx = Regx.test(value) && Regx2.test(value)
        if(value.length >= 5 && (strongRegx || Regx3.test(value))){
            strong.css({
                'background': '#f9c231'
            })
        }
        else{
            strong.css({
                'background': '#e0e3d7'
            })
        }
        // hard 
        var hardRegx = Regx.test(value) && Regx2.test(value) && Regx3.test(value) && Regx4.test(value)
        if (value.length >= 8 && hardRegx){
            hard.css({
                'background': 'green'
            })
        }else{
            hard.css({
                'background': '#e0e3d7'
            })
        }
    })



});




