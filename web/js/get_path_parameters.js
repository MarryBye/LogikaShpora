function get_path_parameters() {
    var path = window.location.pathname

    var path_segments = path.split("/")
    var parameters = {}
    
    path_segments.forEach(function(element, index) {
        var parameter = element.split("=")
        if (parameter[0] && parameter[1]) {
            parameters[parameter[0]] = parameter[1]
        }
    });
    
    return parameters
    
}