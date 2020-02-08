$(function(){
    var product = $('select[name=product]');
    product.empty();
    var shade = $('select[name=shade]');

    product.prepend('<option value="Not selected" selected disabled>Selecione o produto...</option>');
        $('select[name=brand]').change(function(){
            if($("#idTipo option:selected").text() != ("Selecione o produto...")) {
                shade.empty();
                shade.prepend('<option value="Not selected" selected disabled>Selecione a cor...</option>');
                var brand_id = $('select[name=brand]').val();
                request_url = '../product/list/' + brand_id;
                $.ajax({
                    url: request_url,
                    type: "GET",
                    success: function(data){
                        product.empty();
                        product.prepend('<option value="Not selected" selected disabled>Selecione o produto...</option>');                        
                        $.each(data, function(key, value){
                            product.append('<option value="' + key + '">' + value + '</option>');
                        });
                    }
                })
            }
        })
});
