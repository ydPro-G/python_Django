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
            email='dd@dd.com',
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
    
    def test_get_index(self):
        # 请求首页，测试首页的可用性
        client = Client()
        response = client.get('/')
        # 断言相等,assertEqual(a,b,[msg='测试失败时打印的消息']) 状态代码，200
        self.assertEqual(response.status_code,200,'status code must be 200!')

    def test_post_student(self):
        # 提交数据，然后请求首页
        client = Client()
        data = dict(
            name = 'test_for_post',
            sex = 1,
            email=333@dd.com,
            profession='程序员',
            qq='3333',
            phone='32222',
        )
        response = client.post('/',data)
        self.assertEqual(response.status_code,302,'status code must be 302!')

        response = client.get('/')
        # 断言为真 ，assertTrue(expr, msg=None)
        # b是什么？response.content的内容是bytes类，所以需要在对比的字符串前加b来声明它是bytes而不是str
        self.assertTrue(b'test_for_post' in response.content,'response content must contain "test_for_post"')
