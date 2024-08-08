from flask import Flask, render_template, render_template_string, request
from paths import *
from funcs import get_lessons

app = Flask(
    __name__,
    static_folder=STATIC_PATH,
    template_folder=TEMPLATES_PATH,
)

MODULES = get_lessons()

@app.route("/")
def index():
    print(MODULES)
    return render_template("index.html", modules_info=MODULES)

@app.route("/module=<module>")
def load_module(module):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        function_string = """
            {% from 'components/lessons_list.html' import generate_lessons_list %}
            {{ generate_lessons_list(lessons) }}
        """
        return render_template_string(function_string, lessons=MODULES[module]["lessons"])
    else:
        return render_template("index.html", modules_info=MODULES)

@app.route("/module=<module>/lesson=<lesson>")
def load_lesson(module, lesson):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render_template(f"lessons/{module}/{lesson}/lesson.html", difficulty_level=MODULES[module]["lessons"][lesson]["difficulty"])
    else:
        return render_template("index.html", modules_info=MODULES)

if __name__ == "__main__":
    app.run()