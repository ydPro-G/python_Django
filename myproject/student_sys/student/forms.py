# 提交数据
from django import forms # 导入django表单，有表单功能

from .models import Student # 导入模型，类


# 和models.py里的Student定义类似，那么我们可以复用Student的代码，用ModelForm
# class StudentForm(forms.Form):
#     name = forms.CharField(label='姓名',max_length=128)
#     sex = forms.ChoiceField(label='性别',choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label='职业',max_length=128)
#     email = forms.EmailField(label='邮箱',max_length=128)
#     qq = forms.CharField(label='QQ',max_length=128)
#     phone = forms.CharField(label='手机',max_length=128)

# 通过继承ModelForm,写下需要展示的fields
class StudentForm(forms.ModelForm):
    # 设置QQ输入限制
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        # isdigit()验证是否是数字
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        # 返回整数型
        return int(cleaned_data)


    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        )

