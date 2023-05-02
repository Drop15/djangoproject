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

