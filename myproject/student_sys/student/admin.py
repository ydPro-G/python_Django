from django.contrib import admin
from .models import Student # 导入models文件Student类

# 注册在models.py里设置的模型
# 后台操作的设置文件

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','profession','email','qq','phone','status','created_time') # admin页面列表展示
    list_filter = ('sex','status','created_time') # 指定admin页面列表项排序字段，性别，状态，创建时间
    search_fields = ('name','profession') # 指定admin页面搜索的字段，只能通过姓名或职业搜索
    fieldsets = (
        (None,{
            'fields':(
                'name',
                ('sex','profession'),
                ('email','qq','phone'),
                'status',
            )
        }),
    )

admin.site.register(Student,StudentAdmin) # 注册模型Student(models.py设置)

