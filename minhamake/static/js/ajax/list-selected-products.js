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
    if(product && shade){
        $.ajax({
            type: 'POST', 
            url: request_url,
            data: {
                product: product.val(), 
                shade: shade.val()
            },
            success: function (response) {
                loadSelected2(response);        
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }          
        })
    }
};

function removeSelectedProduct(pk){

    request_url = "user/selected/del";
    $.ajax({
        type: 'POST', 
        url: request_url,
        data: {
            id_selected:pk
        },
        success: function (response) {
            loadSelected2(response);        
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }          
    })
};

function loadSelected2(response){

    var selected = $('select[id=teste]');
    selected.empty();
    response['instance'].forEach((item) => {
        $("#teste").append(
           `<option selected="selected" value="${item.id_selected}">
                ${item["name_brand"] + " - " + item["name_product"] + " - " + item["name_shade"] || ""}</option> 
           `
        );
    });
}