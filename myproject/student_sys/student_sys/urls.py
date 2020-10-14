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

from student.views import index # 导入视图中index函数

urlpatterns = [
    # path(route,view,name=None,**kwargs) route:路径 view：视图 name:别名 **kwargs：字典，传给view函数
    url(r'^$',index,name='index'), # 设置路径，设置函数
    url(r'^admin/', admin.site.urls),
]
