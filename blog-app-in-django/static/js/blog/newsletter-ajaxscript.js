$(document).ready(function () {
    $('#newsletterForm').submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/',
            data: $(this).serialize(),
            success: function (response) {
                $("#msg").html('<div class="alert alert-success alert-dismissible" role="alert">   <div>'+ response.message +'</div>   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>');

                // Clear form fields
                $('#newsletterForm')[0].reset();
            },
            error: function (error) {
                $("#msg").html('<div class="alert alert-danger alert-dismissible" role="alert">   <div>'+ error.responseJSON.error +'</div>   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>');
                
            }
        });
    });
});