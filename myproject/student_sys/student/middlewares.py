import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

# 配置middleware（中间件）
# 统计首页每次访问程序所消耗的时间（Django接受请求到最终返回的时间

class TimeItMiddleware(MiddlewareMixin):

    # 请求来到middlewares中时进入的第一个方法，可以在这里做一些校验（用户登录之类）
    # 两个返回值：HttpResponse或None。如果返回HttpResponse，接下来处理方法只会执行process_response，如果是None，那么Django会帮你执行view函数，得到最终的response
    # 注意：如果你middleare是settings配置的MIDDLEARE第一个，那么剩下的middleaware也不会执行
    def process_request(self,request):
        return
    
    # 在process_request方法后执行，参数如同代码所示
    # func是将要执行的view方法
    #返回值和process_request一样，HttpResponse或者None，逻辑也是一样，如果返回None，那么Django会帮你执行view函数，得到最终的response
    def process_view(self,request,func,*args,**kwargs):
        if request.path != reverse('index'):
            return None
        # 返回当前时间的时间戳
        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view: {:.2f}s'.format(costed))
        return response
    
    # 发生异常时，会进入这个方法
    # 在将要调用view中出现异常，或返回的模板response在渲染时发生的异常，如果是在process_view手动调用了func，就不会出发了
    # 可以选择处理异常，返回一个含有异常信息的TttpResponse，或直接返回None，不处理
    def process_exception(self,request,exception):
        pass
    
    # 执行完上面的方法，并且Django帮我们执行完view，拿到最终的response后，如果使用了模板的response，就会来到这个方法中
    # 在这个方法中可以对response做操作，比如Content-Type设置或其他header头设置
    def process_template_response(self,request,response):
        return response
    
    # 所有流程都处理完就来到了这个方法。这个方法逻辑和process_template_response完全一样，只是后者针对带有模板的response处理
    def process_response(self,request,response):
        return response




