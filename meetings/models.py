from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Meeting(models.Model):
    id = models.AutoField(primary_key=True)             # 자동 삽입 (primary_key=True인 속성이 없다면)
    created = models.DateTimeField(auto_now_add=True)   # 객체가 처음 생성될 때의 시간으로 자동 설정
    sinceWhen = models.DateTimeField()
    tillWhen = models.DateTimeField()
    # auth.User : 타겟 모델
    # related_name='meetings' : 역참조 시 사용할 이름 (유저.meetings()는 예약 객체들의 쿼리셋을 반환)
    # on_delete=models.CASCADE : 유저가 삭제되면 그 유저의 예약들도 모두 삭제
    user = models.ForeignKey('auth.User', related_name='meetings', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('id', 'created', 'sinceWhen', 'tillWhen', 'user')

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        #lexer = get_lexer_by_name(self.language)
        #linenos = 'table' if self.linenos else False
        #options = {'title': self.title} if self.title else {}
        #formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        #self.highlighted = highlight(self.code, lexer, formatter)
        super(Meeting, self).save(*args, **kwargs)
