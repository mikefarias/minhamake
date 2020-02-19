function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function addSelectedProduct(){

    var product = $('select[name=product]');
    var shade = $('select[name=shade]');
    
    request_url = "user/selected/add"
    if(product){
        $.ajax({
            type: 'POST', 
            url: request_url,
            data: {
                product: product.val(), 
                shade: shade.val()
            },
            success: function (response) {
                // on successfull creating object
                // 1. clear the form.
                $("#selected").trigger('reset');
         
                // 2. focus to nickname input 
                $("#id_nick_name").focus();
    
                // display the newly friend to table.
                console.log(response);

                response['instance'].forEach((item) => {
                    pk = item.id_product;
                    $("#selected").append(
                        `<tr>
                            <td>${item["name_brand"]||""}</td>
                            <td>${item["name_product"]||""}</td>
                            <td>${item["name_shade"]||""}</td>
                            <td>
                                <a href="user/selected/del/${item.id_product}" class="btn btn-danger"> Remove </a>
                            </td>
                            <td></td>
                        </tr>`
                    );
                });
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }          
        })
    }
};