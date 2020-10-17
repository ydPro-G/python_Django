from django.contrib import admin
from .models import Student # 导入models文件Student类

# 注册在models.py里设置的模型
# 后台显示与操作的设置文件

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','profession','email','qq','phone','status','created_time') # admin页面列表展示
    list_filter = ('sex','status','created_time') # 指定admin页面列表项排序字段，性别，状态，创建时间
    search_fields = ('name','profession') # 指定admin页面搜索的字段，只能通过姓名或职业搜索
    
    # 根据字段对页面进行分组显示或布局,fieldsets是一个二元元组列表
    # 格式为(name,field_options)--name表示标题的字符串；---ffield_options是一个包含在该fiedset内的字段列表
    fieldsets = (
        ('自定义字符串',{ # name = '自定义字符串'
            'fields':(
                'name', # name 一行
                ('sex','profession'),  # sex profession 一行
                ('email','qq','phone'),
                'status',
            )
        }),
    )

admin.site.register(Student,StudentAdmin) # 注册模型Student(models.py设置)

