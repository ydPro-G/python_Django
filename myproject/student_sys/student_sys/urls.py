"""student_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from student.views import IndexView # 导入views中IndexView类

urlpatterns = [
    # path(route,view,name=None,**kwargs) route:路径 view：视图 name:别名 **kwargs：字典，传给view函数
    url(r'^$',IndexView.as_view(),name='index'), # 设置路径，设置函数,as_view对get和post方法的包装
    url(r'^admin/', admin.site.urls),
]
#Django 使用如上的方式配置 URL 到对应视图函数的路由映射。注意到 url() 函数前两个位置参数需要传递的值，第一个是需要捕获的 url 的正则模式，第二个参数则是一个可调用的对象（即视图函数）。
# 如果我们通过 def 定义视图函数，那么传入的这个可调用对象就是这个函数本身；而如果我们定义的是类视图，则必须调用类视图的 as_view 方法返回一个根据这个类生成的可调用对象。