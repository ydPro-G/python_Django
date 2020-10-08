from django.contrib import admin
from learning_logs.models import Topic,Entry  # 导入模型

# 注册模型，这些模型都是models里面的类
admin.site.register(Topic) # 注册模型Topic
admin.site.register(Entry) # 注册模型Entry


