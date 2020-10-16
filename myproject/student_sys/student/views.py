from django.shortcuts import render
from django.http import HttpResponseRedirect # http响应重定向
from django.urls import reverse
from django.views import View # class-based view

from .forms import StudentForm # 导入forms模板StudentForm类
from .models import Student # 导入models模板Student类


# 创建视图：开发首页
# 注意：渲染模板/静态页面时，会去每个APP下面查找，就是settings设置的APP
# 并且是顺序查找，如果有2个APP，都存在index.html，那么都会加载前面的APP的index.html
# class-based view 和 function view 的区别


# 创建 class-based view
class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        # 数据获取逻辑封装到了Model层，通过Student模型拿到所有的student数据
        students = Student.get_all() 
        context = {
            'students':students
        }
        return context
    
    # 处理get请求
    def get(self,request): # request是Django对用户发送过来的HTTP请求的封装
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form':form
        })
        return render(request,self.template_name,context=context)

    # 处理post请求
    def post(self,request):
        # 保存提交的request请求数据
        form = StudentForm(request.POST)
        # 校验机制，如果是有效的post请求
        if form.is_valid():
            # 保存信息
            form.save()
            # 通过reverse拿到urls.py里对应的url
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form':form
        })
        # 通过render渲染页面，使用了模板文件index.html。把数据放到context中传递到模板
        return render(request,self.template_name,context=context)












# 不使用class-based view,这是function view
# # 定义函数index，参数是request
# def index(request): # request是Django对用户发送过来的HTTP请求的封装
#     # 通过Student模型拿到所有的student数据
#     students = Student.get_all() # 数据获取逻辑封装到了Model层，这是个更语义化代码
#     if request.method == 'POST':
#         form = StudentForm(request.POST) # 传的是post请求
#         # 校验机制，如果是有效的post请求
#         if form.is_valid():

#             #这一段是手动构建Student对象保存student数据，但其实可以省掉
#             # cleaned_data它是Form 根据字段类型对用户提交的数据做完转换后的结果
#             cleaned_data = form.cleaned_data 
#             student = Student()
#             # 对应字段提交表单数据，将用户提交的数据存到数据库中
#             student.name = cleaned_data['name'] 
#             student.sex = cleaned_data['sex']
#             student.email = cleaned_data['email']
#             student.profession = cleaned_data['profession']
#             student.qq = cleaned_data['qq']
#             student.phone = cleaned_data['phone']


#             # 保存数据
#             student.save() 
#             # 通过reverse拿到urls.py里对应的url
#             return HttpResponseRedirect(reverse('index'))
#         else:
#             # 如果是get请求就把StudentFrom实例传到模板中
#             form = StudentForm()
        
#         context = {
#             'student':students,
#             'form':form,
#         }
        
#         return render(request, 'index.html', context=context)








#     # 通过render渲染页面，使用了模板文件index.html。把数据放到context中传递到模板
#     return render(request,'index.html',context={'students':students}) #render里的words传递给模板index.html



