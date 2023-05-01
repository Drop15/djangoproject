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

def add_word(request):
    if request.method == "POST":
        cache.clear()
        new_word = request.POST.get("new_word", "")
        new_translation = request.POST.get("new_translation", "")
        context = {}
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
        return render(request, "add_word.html", context)
    else:
        word_added(request)

def word_added(request):
    return render(request, "word_added.html")