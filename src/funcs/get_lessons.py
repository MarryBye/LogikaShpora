import os

import pprint

def get_lessons() -> dict[str: dict["name": str, "lessons_count": int, "lessons": dict[str: dict["name": str, "diffictulty": int]]]]:

    # l = {
    #     "module_first": {
    #         "module_name": "Перший модуль",
    #         "module_lessons_count": 6,
    #         "module_lessons": {
    #             "lesson1": {
    #                 "lesson_name": "1. Вивод інформації",
    #                 "lesson_difficulty": 0,
    #             },
    #             "lesson2": {
    #                 "lesson_name": "2. Ввод інформації",
    #                 "lesson_difficulty": 0,
    #             }
    #         }
    #     }
    # }

    program = {}

    lessons_path = os.path.join("web", "templates", "lessons")
    modules = os.listdir(lessons_path)

    for module in modules:
        module_path = os.path.join(lessons_path, module)

        module_lessons = os.listdir(module_path)
        module_lessons.remove("module_info.txt")

        module_info = open(os.path.join(module_path, "module_info.txt"), "r", encoding="UTF-8").readlines()
        module_name = module_info[0]

        program[module] = {
            "name": module_name,
            "lessons_count": len(module_lessons),
            "lessons": {}
        }

        for lesson in module_lessons:
            lesson_path = os.path.join(module_path, lesson)

            lesson_info = open(os.path.join(lesson_path, "lesson_info.txt"), "r", encoding="UTF-8").readlines()
            lesson_name = lesson_info[0]
            lesson_difficulty = lesson_info[1]

            program[module]["lessons"][lesson] = {
                "name": lesson_name,
                "difficulty": lesson_difficulty
            }

    return program


pprint.pprint(get_lessons())