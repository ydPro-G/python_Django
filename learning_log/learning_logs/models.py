from django.db import models

# 在这里创建模型
# 模型就是一个类，包含属性和方法

class Topic(models.Model): # 创建一个类，继承Model，只有两个属性：text,date_added
    """用户学习的主题"""
    text = models.CharField(max_length=200) # CharField:由字符或文本组成的数据，需要存储少量文本时可使用，定义CharField时需要注意设置最大字符空间
    date_added = models.DateTimeField(auto_now_add=True) #DateTimeField:记录日期和时间的数据，传递了实参auto_add_now=True,每当用户创建新主题，自动设置成当前时间

    def _str_(self): # 方法
        """返回模型的字符串表示"""
        return self.text # 返回存储在属性中的字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

class Entry(models.Model): # 继承基类Model
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete= models.CASCADE) # 属性1.外键，Topic的外键，用于关联到特定主题, 表与表之间关联的时候,必须要写on_delete参数
    text = models.TextField() # 属性2.字段，不需要长度限制
    date_added = models.DateTimeField(auto_now_add=True) # 属性3.按创建顺序呈现条目，在每个条目旁放置时间戳

    class Meta: # 在Entry类中嵌套Meta类，用来管理模型的额外信息
        verbose_name_plural = 'entries' # 一个特殊的属性，在需要时使用Entries表示多个条目

        def __str__(self): # 呈现条目时返回text属性前50
            """返回模型的字符串表示"""
            return self.text[:50] + "..."

