$(document).ready(function() {
    generateGridView()
    $("select").change(function () {
        $('.field_grid').empty()
        generateGridView()
    })

    var colorMode;
    $('#colors').on('click', '.cell', function(){
        $('#colors').children().css('border', '');
        $(this).css('border', '5px solid grey');
        $('.field_grid .cell').css({'cursor': 's-resize'});
        colorMode = this.className;
    });

    $(document).on('click', '.field_grid .cell', function() {
        if (colorMode) {
            $(this).removeAttr('class', colorMode);
            $(this).attr('class', colorMode);
        }
    });
})

function generateGridView(){
    var field_width = $('#field_width option:selected').text()
    var field_length = $('#field_length option:selected').text()
    for(let i = 1; i <= field_length; i++){
        var container = $("<span></span>")
        for(let j = 1; j <= field_width; j++){
            var cell = $('<div class="cell"></div>')
            container.append(cell)
        }
        $('.field_grid').append(container)
    }
}

