
$(function(){

    var email = $("#email");
    var c_password = $("#id_password2");
    var password = $("#id_password1")

    // password checker
    password.after("<div class='row password-checker'> <div class='col-3'></div> <div class='col-2'><div id='week'></div><small>week</small></div>  <div class='col-3'><div id='strong'></div><small>strong</small></div> <div class='col-2'><div id='hard'></div><small style='margin-left:-32px'>hard</small></div></div>")

    var week = $("#week");
    var strong = $("#strong");
    var hard = $("#hard");

    $(".password-checker").css({
        'margin-top': '7px',
    }).hide()
    
    week.css({
        'height': '5px',
        'width': '60px',
        'background': '#e0e3d7',
        'border-radius': '5px',
        'margin-left': '-11px'
    })
    strong.css({
        'height': '5px',
        'width': '60px',
        'background': '#e0e3d7',
        'border-radius': '5px',
        'margin-left': '-11px'
    })
    hard.css({
        'height': '5px',
        'width': '60px',
        'background': '#e0e3d7',
        'margin-left': '-42px',
        'border-radius': '5px',
    })
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


    // all login and register field focus and blur 
    email.focus(function(){
        $(this).css({
            'box-shadow': '0 0 4px #E4AF2C',
            'border': '1px solid #6FA7F8'
        })
    });
    email.blur(function(){
        $(this).css({
            'box-shadow': '0 0 4px white',
            'border': '1px solid #bdbfb9'
        })
    });

    c_password.focus(function(){
        $(this).css({
            'box-shadow': '0 0 4px #E4AF2C',
            'border': '1px solid #6FA7F8'
        })
        
    });
    c_password.blur(function(){
        $(this).css({
            'box-shadow': '0 0 4px white',
            'border': '1px solid #bdbfb9'
        })
    });
    password.focus(function(){
        $(this).css({
            'box-shadow': '0 0 4px #E4AF2C',
            'border': '1px solid #6FA7F8'
        })
    });
    password.blur(function(){
        $(this).css({
            'box-shadow': '0 0 4px white',
            'border': '1px solid #bdbfb9'
        })
    });

})
















