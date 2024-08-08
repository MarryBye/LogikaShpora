function page_load() {

    var parameters = get_path_parameters()

    var module = parameters["module"];
    var lesson = parameters["lesson"];

    if (module) {
        
        $.ajax({
            url: "/module=" + module,
            method: 'GET',
            success: function(data) {
                $(".navbar_lessons").html(data);
            }
        });

        style_choosen_button("button_choose_module", "module", module)

    }

    if (lesson) {

        $.ajax({
            url: "/module=" + module + "/lesson=" + lesson,
            method: 'GET',
            success: function(data) {
                $(".content_right").html(data);
            }
        });

        style_choosen_button("button_choose_lesson", "lesson", lesson)
        
    }
}