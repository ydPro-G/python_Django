from django.db import models

# 设计模型：通过数据-模型语句，通过对象关系映射器来使用python代码描述数据库结构。

#编写一个范围的类
class Student(models.Model):
    SEX_ITEMS = [
        (1,'男'),
        (2,'女'),
        (0,'未知'),
    ]
    STATUS_ITEMS = [
        (0,'申请'),
        (1,'通过'),
        (2,'拒绝'),
    ]

    # 通过数据-模型语句创建数据库 功能简介参考：https://www.cnblogs.com/limaomao/p/9255148.html
    name = models.CharField(max_length=128,verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS,verbose_name='性别')# 整数类型 数据库11位int类型
    profession = models.CharField(max_length=128,verbose_name='职业')# 字符串类型，映射到数据库转化成varchar类型 
    email = models.CharField(max_length=128,verbose_name='Email')# max_length 定义最大字节长度
    qq = models.CharField(max_length=128,verbose_name='QQ')
    phone = models.CharField(max_length=128,verbose_name='电话')

    status = models.IntegerField(choices=STATUS_ITEMS,default=0,verbose_name='审核状态')
    created_time = models.DateField(auto_now_add=True,editable=False,verbose_name='创建时间')

    def __str__(self):
        return '<Student: {}>'.format(self.name) # 返回函数
    
    class Meta:
        verbose_name = verbose_name_plural = '学员信息'
    
    @classmethod # 不需要实例化，要使用student类的方法直接类名.方法名()调用
    def get_all(cls):# cls：表示自身类的参数
        # 返回所有的学生信息
        return cls.objects.all() #从数据库中查询出来的结果一般是一个集合，这个集合叫做QuerySet。Entry.objects.all()就是QuerySet查询所有的Entry目录
