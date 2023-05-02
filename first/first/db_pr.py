from first.models import Lessons, Words

def db_get_lessons_for_table():
    lessons = []
    for i, lesson in enumerate(Lessons.objects.all()):
        lessons.append([i+1, lesson.lesson_date, lesson.topic])
    return lessons

def db_write_lesson(new_lesson_date, new_topic):
    lesson = Lessons(lesson_date=new_lesson_date, topic=new_topic)
    lesson.save()

def db_get_words_for_table():
    words = []
    for i, wor in enumerate(Words.objects.all()):
        words.append([i+1, wor.word, wor.translation])
    return words

def db_write_words(new_word, new_translation):
    word = Words(word=new_word, translation=new_translation)
    word.save()


# def db_get_terms_stats():
#     db_terms = len(TermAuthors.objects.filter(termsource=”db”))
#     user_terms = len(TermAuthors.objects.filter(termsource=”user”))
#     terms = Terms.objects.all()
#     defin_len = [len(term.definition) for term in terms]
#     stats = {
#         “terms_all”: db_terms + user_terms,
#         “terms_own”: db_terms,
#         “terms_added”: user_terms,
#         “words_avg”: sum(defin_len)/len(defin_len),
#         “words_max”: max(defin_len),
#         “words_min”: min(defin_len)
#     }
#     return stats
