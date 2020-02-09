$(function(){
    var brand = $('select[name=brand]');
    brand.prepend('<option value="Not selected" selected disabled>Selecione a marca...</option>');
                request_url = '../brand/list';
                $.ajax({
                    url: request_url,
                    type: "GET",
                    success: function(data){
                        brand.empty();
                        brand.prepend('<option value="Not selected" selected disabled>Selecione a marca...</option>');                        
                        $.each(data, function(key, value){
                            brand.append('<option value="' + key + '">' + value + '</option>');
                        });
                    }
                })
});
