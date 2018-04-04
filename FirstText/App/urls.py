from django.urls import path

from App import views

urlpatterns = [
    path('register', views.register, name='register'),
    # 首页
    path('', views.index, name='home'),
    # 孙建师个人信息
    path('jianshi', views.jianShi, name='jianshi'),
    # 宋佳文个人信息
    path('jiawen', views.jianWen, name='jiawen'),
    # 爱情日志
    path('ailog', views.aiLog, name='ailog'),
    # 搜索
    path('sousuo', views.souSuo, ),
#     温馨瞬间
    path('photo', views.photos),
]