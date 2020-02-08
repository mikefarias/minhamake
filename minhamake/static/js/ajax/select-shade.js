$(function(){
    var shade = $('select[name=shade]');
    shade.empty();
    shade.prepend('<option value="Not selected" selected disabled>Selecione a cor...</option>');
        $('select[name=product]').change(function(){
            if($("#idTipo option:selected").text() != ("Selecione a cor...")) {
                var product_id = $('select[name=product]').val();
                request_url = '../shade/list/' + product_id;
                $.ajax({
                    url: request_url,
                    type: "GET",
                    success: function(data){
                        shade.empty();
                        shade.prepend('<option value="Not selected" selected disabled>Selecione a cor...</option>');
                        $.each(data, function(key, value){
                            shade.append('<option value="' + key + '">' + value + '</option>');
                        });
                    }
                })
            }
        })
});
