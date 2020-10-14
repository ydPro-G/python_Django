from django.shortcuts import render
from .models import Student # 导入models模板Student函数

# 创建视图：开发首页

# 注意：渲染模板/静态页面时，回去每个APP下面查找，就是settings设置的APP
# 并且是顺序查找，如果有2个APP，都存在index.html，那么都会加载前面的APP的index.html




# 定义函数index，参数是request
def index(request): # request是Django对用户发送过来的HTTP请求的封装
    # 通过Student模型拿到所有的student数据
    students = Student.objects.all() #从数据库中查询出来的结果一般是一个集合，这个集合叫做QuerySet。Entry.objects.all()就是QuerySet查询所有的Entry目录

    # 通过render渲染页面，使用了模板文件index.html。把数据放到context中传递到模板
    return render(request,'index.html',context={'students':students}) #render里的words传递给模板index.html



