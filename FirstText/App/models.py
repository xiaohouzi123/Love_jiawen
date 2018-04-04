from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)

# 爱情日志
class AiLog(models.Model):
    title = models.CharField(u'标题', max_length=50)
    mood_tag = models.CharField(u'心情标签', max_length=20)
    content = models.TextField(u'内容')
    pub_time = models.DateField(u'发表时间', )

    class Mate:
        verbose_name = "爱情日志"
        verbose_name_plural = "爱情日志"

    def __str__(self):
        return self.title

# 时间轴
class TimerShaft(models.Model):
    timer = models.DateField(u'记录时间',)
    title = models.CharField(u'标题', max_length=50)
    content = models.TextField(u'内容')

    def __str__(self):
        return self.title

# 温馨瞬间
class Article(models.Model):
    describe = models.CharField(u'描述', max_length=256)
    ph = models.ImageField(u'图片',upload_to='uploadImages')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    class Mate:
        verbose_name = "温馨图片"
        verbose_name_plural = "温馨图片"


    def __str__(self):
        return self.describe

