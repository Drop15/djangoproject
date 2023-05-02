from django.shortcuts import render
from . import db_pr
from django.core.cache import cache

def index(request):
    return render(request, "index.html")

def lessons(request):
    lessons = db_pr.db_get_lessons_for_table()
    return render(request, "lessons.html", context={"lessons": lessons})

def words(request):
    words = db_pr.db_get_words_for_table()
    return render(request, "words.html", context={"words": words})

def send_word(request):
    if request.method == "POST":
        cache.clear()
        new_word = request.POST.get("word", "")
        new_translation = request.POST.get("translation", "")
        context = {"word": new_word}
        if len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Введите слово"
        elif len(new_translation) == 0:
            context["success"] = False
            context["comment"] = "Введите перевод"
        else:
            context["success"] = True
            context["comment"] = "Слово добавлено!"
            db_pr.db_write_words(new_word, new_translation)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "word_added.html", context)
    else:
        add_word(request)

def add_word(request):
    return render(request, "add_word.html")

def send_lesson(request):
    if request.method == "POST":
        cache.clear()
        lesson_date = request.POST.get("lesson_date", "")
        topic = request.POST.get("topic", "")
        context = {"lesson_date": lesson_date}
        if len(lesson_date) == 0:
            context["success"] = False
            context["comment"] = "Введите дату урока"
        elif len(topic) == 0:
            context["success"] = False
            context["comment"] = "Введите тему урока"
        else:
            context["success"] = True
            context["comment"] = "Урок добавлен!"
            db_pr.db_write_lesson(lesson_date, topic)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "lesson_added.html", context)
    else:
        add_lesson(request)

def add_lesson(request):
    return render(request, "add_lesson.html")