from django.shortcuts import render # 根据视图提供的数据渲染响应
from .models import Topic # 引入models文件中的 Topic类
# 创建视图
def index(request): # url请求时，在views查找函数index
    """学习笔记主页"""
    return render(request,'learning_logs/index.html') # 两个实参，1.原始请求对象2.用于创建网页的模板

def topics(request): # 一个形参：从服务器那里收到的request对象
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added') # 查询数据库-请求提供Topic对象，并按属性date_added对他们排序，将返回的查询集存储在topics中
    context = {'topics': topics}# 发送给模板的上下文-键值对
    return render(request,'learning_logs/topics.html',context)
