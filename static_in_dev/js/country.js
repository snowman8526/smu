function sele(option, op2){
    if ($('#' + option + ' option').length > 1){
        $("#" + option).empty();
        $('#' + option).append('<option value="' + "choce" + '">' + op2 + '</option>');
        $("#" + option).attr("disabled", "disabled");
    };
};
$("#country option[value='choce']").prop("selected", true);
$("#sity").attr("disabled", "disabled");
$("#area").attr("disabled", "disabled");
$("#street").attr("disabled", "disabled");
$("#house").attr("disabled", "disabled");
$("#flat").attr("disabled", "disabled");
//console.log($('#sity option').length);

//Обработка страны
$("#country").change(function(){
    sele("sity","Выберите город");
    sele("area", "Выберите район");
    sele("street", "Выберите улицу");
    sele("house", "Выберите дом");
    sele("flat", "Выберите квартиру");

    $.ajax({type: 'GET',
    url: "{% url 'country' %}",
    data: {con: $(this).val()},
    success: function(data){
        $("#sity").removeAttr("disabled");
        //console.log(data);
        $.each(data, function(key, value) {
            $('#sity').append('<option value="' + key + '">' + value + '</option>');
        });

    }})
    //console.log($(this).val());
});
//обработка городов
$("#sity").change(function(){
    sele("area", "Выберите район");
    sele("street", "Выберите улицу");
    sele("house", "Выберите дом");
    sele("flat", "Выберите квартиру");

    $.ajax({type: 'GET',
    url: "{% url 'sity' %}",
    data: {con: $("#country").val(),
            sity: $(this).val()},
    success: function(area){
        $("#area").removeAttr("disabled");
        //console.log(area);
        $.each(area, function(key, value) {
            $('#area').append('<option value="' + key + '">' + value + '</option>');
        });

    }})
    //console.log($(this).val());
});
//отбор районов
$("#area").change(function(){
    sele("street", "Выберите улицу");
    sele("house", "Выберите дом");
    sele("flat", "Выберите квартиру");

    $.ajax({type: 'GET',
    url: "{% url 'area' %}",
    data: {con: $("#country").val(),
            sity: $("#sity").val(),
            area: $(this).val()},
    success: function(street){
        $("#street").removeAttr("disabled");
        //console.log(street);
        $.each(street, function(key, value) {
            $('#street').append('<option value="' + key + '">' + value + '</option>');
        });

    }})
   //console.log($(this).val());
});


//отбор домов
$("#street").change(function(){
    sele("house", "Выберите дом");
    sele("flat", "Выберите квартиру");

    $.ajax({type: 'GET',
    url: "{% url 'street' %}",
    data: {con: $("#country").val(),
            sity: $("#sity").val(),
            area: $("#area").val(),
            street: $(this).val()},
    success: function(house){
        $("#house").removeAttr("disabled");
        //console.log(house);
        $.each(house, function(key, value) {
            $('#house').append('<option value="' + key + '">' + value + '</option>');
        });

    }})
    //console.log($(this).val());
});

//отбор квартир
$("#house").change(function(){
    sele("flat", "Выберите квартиру");

    $.ajax({type: 'GET',
    url: "{% url 'house' %}",
    data: {con: $("#country").val(),
            sity: $("#sity").val(),
            area: $("#area").val(),
            street: $("#street").val(),
            house: $(this).val()},
    success: function(flat){
        $("#flat").removeAttr("disabled");
        console.log(flat);
        $.each(flat, function(key, value) {
            $('#flat').append('<option value="' + key + '">' + value + '</option>');
        });

    }})
    console.log($(this).val());
});

