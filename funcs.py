import os
from paths import LESSONS_PATH

def get_lessons():

    program = {}

    modules = os.listdir(LESSONS_PATH)

    for module in modules:
        module_path = os.path.join(LESSONS_PATH, module)

        module_lessons = os.listdir(module_path)
        module_lessons.remove("module_info.txt")

        module_file = open(os.path.join(module_path, "module_info.txt"), "r", encoding="UTF-8")
        module_info = module_file.readlines()
        module_file.close()
        
        module_name = module_info[0]

        program[module] = {
            "name": module_name,
            "lessons_count": len(module_lessons),
            "lessons": {}
        }

        for lesson in module_lessons:
            lesson_path = os.path.join(module_path, lesson)

            lesson_file = open(os.path.join(lesson_path, "lesson_info.txt"), "r", encoding="UTF-8")
            lesson_info = lesson_file.readlines()
            lesson_file.close()

            lesson_name = lesson_info[0]
            lesson_difficulty = lesson_info[1]

            program[module]["lessons"][lesson] = {
                "name": lesson_name,
                "difficulty": lesson_difficulty
            }

    return program