import os

from flask import *

STATIC_PATH = os.path.join("web")
TEMPLATES_PATH = os.path.join(STATIC_PATH, "templates")
LESSONS_PATH = os.path.join(TEMPLATES_PATH, "lessons")

MODULES = {}

for module in os.listdir(LESSONS_PATH):
    module_lessons = os.listdir(os.path.join(LESSONS_PATH, module))
    MODULES[module] = {}
    MODULES[module]["lessons_count"] = len(module_lessons)
    MODULES[module]["lessons"] = [lesson for lesson in module_lessons]

web_app = Flask(
    __name__,
    static_folder=STATIC_PATH,
    template_folder=TEMPLATES_PATH,
)

@web_app.route("/")
def index():
    return render_template("index.html", modules_info=MODULES)

@web_app.route("/module=<module>")
def load_module(module):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        function_string = """
            {% from 'components/lessons_list.html' import generate_lessons_list %}
            {{ generate_lessons_list(lessons) }}
        """
        return render_template_string(function_string, lessons=MODULES[module]["lessons"])
    else:
        return render_template("index.html", modules_info=MODULES)

@web_app.route("/module=<module>/lesson=<lesson>")
def load_lesson(module, lesson):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template(f"lessons/{module}/{lesson}/lesson.html")
    else:
        return render_template("index.html", modules_info=MODULES)
    
web_app.run()