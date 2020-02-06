$(function(){
    var product = $('select[name=product]');
    product.empty();
    product.prepend('<option value="Not selected" selected disabled>Selecione o produto...</option>');
        $('select[name=brand]').change(function(){
            if($("#idTipo option:selected").text() != ("YOU SHOULD INSERT THE INITIAL VALUE OF THE setor FIELD WHEN IT IS NOT SELECTED")) {
                var brand_id = $('select[name=brand]').val();
                request_url = '../product/list/' + brand_id;
                $.ajax({
                    url: request_url,
                    type: "GET",
                    success: function(data){
                        product.empty();
                        $.each(data, function(key, value){
                            product.append('<option value="' + key + '">' + value + '</option>');
                        });
                    }
                })
            }
        })
});
