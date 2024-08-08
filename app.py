import os

from flask import *
from src.funcs.get_lessons import get_lessons

STATIC_PATH = os.path.join("web")
TEMPLATES_PATH = os.path.join(STATIC_PATH, "templates")
LESSONS_PATH = os.path.join(TEMPLATES_PATH, "lessons")

MODULES = get_lessons()

web_app = Flask(
    __name__,
    static_folder=STATIC_PATH,
    template_folder=TEMPLATES_PATH,
)

@web_app.route("/")
def index():
    print(MODULES)
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