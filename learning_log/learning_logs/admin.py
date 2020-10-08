from django.contrib import admin
from learning_logs.models import Topic  # 导入模型

# 在这里注册你的模型
admin.site.register(Topic) # 通过管理网站管理模型

