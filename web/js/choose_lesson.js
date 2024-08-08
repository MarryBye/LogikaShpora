function choose_lesson() {
    var parameters = get_path_parameters()

    var module = parameters["module"];
    var lesson = $(this).data('lesson');

    history.pushState({module: module, lesson: lesson}, '', '/module=' + module + '/lesson=' + lesson);

    $.ajax({
        url: "/module=" + module + "/lesson=" + lesson,
        method: 'GET',
        success: function(data) {
            $(".content_right").html(data);
        }
    });

    style_choosen_button("button_choose_lesson", "lesson", lesson)
}