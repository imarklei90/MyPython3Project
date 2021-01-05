from student import *


class StudentManager(object):

    def __init__(self):
        self.student_list = []

    def __str__(self):
        print(self.student_list)

    def run(self):
        # 加载数据
        self.load_students()
        while True:
            # 显示菜单
            self.show_menu()

            # 获取用户输入
            user_select = int(input('请输入需要执行的操作：'))

            # 执行操作
            if user_select == 1:
                self.add_student()
            elif user_select == 2:
                self.del_student()
            elif user_select == 3:
                self.update_student()
            elif user_select == 4:
                self.find_student()
            elif user_select == 5:
                self.save_student()
            elif user_select == 6:
                self.list_student()
            elif user_select == 7:
                # 退出程序
                break



    def load_students(self):
        pass

    def show_menu(self):
        print('***** 请选择需要执行的操作: ')
        print('1. 添加用户')
        print('2. 删除用户')
        print('3. 修改用户')
        print('4. 查找用户')
        print('5. 保存用户')
        print('6. 列出用户')
        print('7. 退出操作')

    def add_student(self):
        # 添加用户
        name = input('输入需要添加的用户名:')
        age = input('输入需要添加的年龄:')
        phone = input('输入需要添加的电话:')
        # 创建Student对象
        stu = Student(name, age, phone)
        # 将student对象添加到列表中
        self.student_list.append(stu)
        print(self.student_list)
        print(stu)

    def del_student(self):
        # 删除用户
        name = input('输入需要删除的用户名:')
        for i in self.student_list:
            if i.name == name:
                self.student_list.remove(i)
                break
        else:
            print('没有此用户')

    def update_student(self):
        # 更新用户
        name = input('输入需要更新的用户名：')
        age = input('输入需要更新的年龄：')
        phone = input('输入需要更新的电话：')
        for i in self.student_list:
            if i.name == name:
                i.name = name
                i.age = age
                i.phone = phone
                print(f'修改的信息为：{i.name}, {i.age}, {i.phone}')
                break
        else:
            print('没有此用户')

    def find_student(self):
        # 查找用户
        name = input('输入需要查找的用户名：')
        for i in self.student_list:
            if i.name == name:
                print(f'{i.name}, {i.age}, {i.phone}')
            break
        else:
            print('查无此人')

    def save_student(self):
        # 将用户保存到文件中
        f = open('student.data', 'w')

        # 先将对象转换成字典
        new_list = [i.__dict__ for i in self.student_list]

        # 转化为字符串
        f.write(str(new_list))

        f.close()

    def list_student(self):
        # 从文件中读取数据

        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['age'], i['phone']) for i in new_list]
            print(self.student_list)
        finally:
            f.close()


