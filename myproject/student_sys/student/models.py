from django.db import models

# 创建模板

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

    # 编写相关字段 功能简介参考：https://www.cnblogs.com/limaomao/p/9255148.html
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
