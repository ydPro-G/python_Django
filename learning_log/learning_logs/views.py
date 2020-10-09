from django.shortcuts import render # 根据视图提供的数据渲染响应

# 创建视图
def index(request): # url请求时，在views查找函数index
    """学习笔记主页"""
    return render(request,'learning_logs/index.html') # 两个实参，1.原始请求对象2.用于创建网页的模板
