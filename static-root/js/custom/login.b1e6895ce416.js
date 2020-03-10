$(function(){
    // error message 
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