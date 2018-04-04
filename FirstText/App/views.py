import random
from django.http import HttpResponse

from App.models import User, AiLog, Article
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        email = request.POST.get('email','')
        sex = request.POST.get('')

        return HttpResponse(username, password, email, sex)

    return render(request,'user/register.html')

# sunjianshi 个人信息
def jianShi(request):

    return render(request, 'user/jianshi.html')

# songjiawen 个人信息
def jianWen(request):

    return render(request, 'user/jiawen.html')

# 爱情日志
def aiLog(request):
    a = AiLog.objects.filter(id = 1)
    title = a[0].title
    mood_tag = a[0].mood_tag
    content = a[0].content
    pub_time = a[0].pub_time
    print(title)
    print(mood_tag)
    print(content)
    print(pub_time)
    print('_____________________')
    return render(request, 'user/log_index.html')

# 搜索
def souSuo(request):
    if request.method == 'POST':
        find = request.POST.get('username')
        text = AiLog.objects.filter(title__icontains = find)
        return HttpResponse(text[0].content)

# 温馨瞬间
def photos(request):
    article = Article.objects.all()
    article1 = article[:6]

    return render(request, 'user/recall_index.html', {'article1':article1})