# Django
目标：一个学习笔记（密码记录）Web应用程序，让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加日志目录。学习笔记的主页对这个网站进行描述，并邀请用户注册或登录，用户登录后可以创建新主题，添加新条目，以及阅读既有的条目。

## 开发流程记录：
1. 确定需求，分析需求
2. 初始化环境
3. 创建项目
4. 创建APP
5. 编写代码
    + 后台开发：
    + 编写models.py：在MVC(Model（模型）+View（视图）+ Controller（控制器）设计模式)或者说MTV设计模式中，模型（M）代表对数据库的操作。
    + 编写admin.py：管理后台，通过读取你的模型数据，快速构造出一个可以对实际数据进行管理的Web站点。
    + 编写settings.py：Django项目的设置文件位于项目同名目录下，名叫settings.py。这个模块，集合了整个项目方方面面的设置属性，可以设置语言，时区是项目启动和提供服务的根本保证。

    + 创建数据库：
    + 命令：数据库迁移文件：python manage.py makemigrations
    + 命令：创建表：python manage.py migrate
    + 命令：创建用户名和密码：python manage.py createsuperuser
    + 登录admin后台

    + 前台开发：
    + 编写views.py:视图的概念是一类具有相同功能和模板的网页的集合。一个视图函数通常对应一个页面，提供特定的功能，使用特定的模板。  **（注意class-based view 和 function view 的区别）**
    + 编写index.html:编写一个网页模板，具体数据从view中获取
    + 编写urls.py:设置路由

    + 输出数据
    + 修改views.py,修改index.html

    + 提交数据：
    + 创建forms.py：设置页面可提交数据
    + 在index.html 中设置模板

    + 进阶一：在views.py中使用class-based view:编写结构化的类，让每一部分的代码负责的功能更加明确
    + 进阶二：配置middleware:编写middleware.py设置中间件，将middleware中定义的类放到settings.py中
    + 进阶三：编写TestCase:编写单元测试，使用unittest模块里的方法 


    


