
$(function(){
    
    var username = $("#username");
    var loginPassword = $("#login-password");
    

    loginPassword.focus(function(){
        $(this).css({
            'box-shadow': '0 0 4px #E4AF2C',
            'border': '1px solid #6FA7F8'
        })
    });
    loginPassword.blur(function(){
        $(this).css({
            'box-shadow': '0 0 4px white',
            'border': '1px solid #bdbfb9'
        })
    });

    username.focus(function(){
        $(this).css({
            'box-shadow': '0 0 4px #E4AF2C',
            'border': '1px solid #6FA7F8'
        })
    });
    username.blur(function(){
        $(this).css({
            'box-shadow': '0 0 4px white',
            'border': '1px solid #bdbfb9'
        })
    });

    // error message show 
    $("#signIn-form").submit(function(event){
        var this_ = $(this)
        var LoginFormUrl = this_.attr('action')
        var LoginFormData = this_.serialize()
        $.ajax({
            url: LoginFormUrl,
            method: 'POST',
            data: LoginFormData,
            success: function(data){
                if (!data.is_login){
                    $(".login-error-message").html("<span id='l-msg'>Invalid username or Password!</span>").css({
                        'margin-bottom': '10px',
                    })
                    $("#l-msg").css({
                        'background-color': '#F7AEC2',
                        'height': '20px',
                        'padding': '10px',
                        'border-radius': '2px'
                    })
                
                    setTimeout(function(){
                        $("#l-msg").fadeOut(1000);
                    }, 1500); 
                }else{
                    document.location.href = "/accounts/dashboard/"
                }
                console.log(data)
            },
            error: function(data){
                console.log('Error')
            }
        })

        event.preventDefault()
    })




});





