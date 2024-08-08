function choose_module() {

    var module = $(this).data('module');

    history.pushState({module: module}, '', '/module=' + module);
    
    $.ajax({
        url: "/module=" + module,
        method: 'GET',
        success: function(data) {
            $(".navbar_lessons").html(data);
        }
    });

    style_choosen_button("button_choose_module", "module", module)

}