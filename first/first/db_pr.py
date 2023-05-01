from first.models import Lessons, Words

def db_get_lessons_for_table():
    lessons = []
    for i, lesson in enumerate(Lessons.objects.all()):
        lessons.append([i+1, item.lesson_date, item.topic])
    return lessons

def db_write_lesson(new_lesson_date, new_topic):
    lesson = Lessons(lessondate=new_lesson_date, lessontopic=new_topic)
    lesson.save()

def db_get_words_for_table():
    words = []
    for i, word in enumerate(Words.objects.all()):
        words.append([i+1, item.word, item.translation])
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
