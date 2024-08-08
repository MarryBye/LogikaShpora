function style_choosen_button(id, data, value) {
    setTimeout(function() {
    var buttons = $('button#' + id);

    buttons.each(function() {
        var button = $(this); 

        if (button.data(data) === value) {
            button.css({
                "color": "rgb(236, 228, 121)"
            });
        } else {
            button.css({
                "color": "white"
            });
        }
    });
    }, 75);
}