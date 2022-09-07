from django import template
from news.models import obscenities

register = template.Library()

@register.filter(name='censor')
def censor(text: str):
    for word in obscenities:
        if new_word.lower().find(word):
            new_word.replace(word, f' {word[:]}){len(word)-}*"*"}', new_word.count(word))
        return  f'{new_word}'
