from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    writer = models.CharField(max_length=50, verbose_name="작성자")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    content = models.TextField(verbose_name="내용")
    hits = models.PositiveIntegerField(default=0, verbose_name="조회수")
    top_fixed = models.BooleanField(default=False, verbose_name="상단고정")

    def __str__(self):
        return self.title

