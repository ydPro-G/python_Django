"""定义learning_logs的url模式"""
from django.urls import path,re_path #导入path，将path映射到视图
from . import views # 导入模块views，.从当前urls.py模块所在文件夹导入视图

urlpatterns = [   # 一个列表
    # 主页
    # 三个实参（第一：一个正则表达式，定义Django可查找的模式）
    # 第二个实参：指定要调用的视图函数，url与第一个实参匹配就调用这个视图函数
    # 第三个实参：指定这个url模式的名称指定为index
    path('',views.index,name='index'), 
]