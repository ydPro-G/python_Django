from django.test import TestCase,Client

from .models import Student

# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='GG',
            sex=1,
            email='1@163.com',
            profession='程序员',
            qq='3333',
            phone='2222',
        )
    
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='dd@dd.com'
            profession='程序员',
            qq='3333',
            phone='2222',
        )
        # 性别测试
        self.assertEqual(Student.sex_show,'男','性别字段内容跟展示不一致！')
    
    def test_filter(self):
        Student.objects.create(
            name='g',
            sex=1,
            email='body@dd.com',
            profession='程序员',
            qq='3333',
            phone='2222',
        )
        name = 'gg'
        # name测试
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,'应该只存在一个名称为{}的记录'.format(name))
        