from modeltranslation.translator import translator, TranslationOptions
from app1.models import TodoModel

class NewsTranslationOptions(TranslationOptions):
    fields = ('task','note')

translator.register(TodoModel, NewsTranslationOptions)