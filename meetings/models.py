from django.db import models
from pygments.lexers import get_all_lexers#, get_lexer_by_name
from pygments.styles import get_all_styles
#from pygments.formatters.html import HtmlFormatter
#from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Meeting(models.Model):
    id = models.AutoField(primary_key=True)             # 자동 삽입 (primary_key=True인 속성이 없다면)
    created = models.DateTimeField(auto_now_add=True)   # 객체가 처음 생성될 때의 시간으로 자동 설정
    sinceWhen = models.DateTimeField()
    tillWhen = models.DateTimeField()
    #user = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    #highlighted = models.TextField()

    class Meta:
        ordering = ('id', 'created', 'sinceWhen', 'tillWhen')
