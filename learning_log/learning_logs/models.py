from django.db import models

# 在这里创建模型
# 模型就是一个类，包含属性和方法

class Topic(models.Model): # 创建一个类，继承Model，只有两个属性：text,date_added
    """用户学习的主题"""
    text = models.CharField(max_length=200) # CharField:由字符或文本组成的数据，需要存储少量文本时可使用，定义CharField时需要注意设置最大字符空间
    date_added = models.DateTimeField(auto_now_add=True) #DateTimeField:记录日期和时间的数据，传递了实参auto_add_now=True,每当用户创建新主题，自动设置成当前时间

    def _str_(self): # 方法，显示模型的简单表示
        """返回模型的字符串表示"""
        return self.text # 返回存储在属性中的字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
