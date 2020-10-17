from model.controller import *
from model.model import *

class StudentManagerView():
    """
    视图模块
    """
    def __init__(self):
        #绑定控制对象，方便数据处理
        self.__manager_controller = StudentManagerController()

    def __display_menu(self):
        """
        主菜单
        :return:
        """
        print('+---------------------+')
        print('| 1)添加学生信息        |')
        print('| 2)显示学生信息        |')
        print('| 3)删除学生信息        |')
        print('| 4)修改学生信息        |')
        print('| 5)按照成绩升序排序     |')
        print('| 0)退出                |')
        print('+---------------------+')

    def __elect_menu(self,value):
        """
        选择菜单处理
        :param value: 选项
        :return:
        """
        if value == '1':
            self.add_student()
        elif value == '2':
            self.show_student()
        elif value == '3':
            self.remove_student()
        elif value == '4':
            self.update_student()
        elif value == '5':
            self.sort_stuent()

    def add_student(self):
        while True:
            name = input('姓名:')
            age = int(input('年龄:'))
            gender = input('性别:')
            score = int(input('分数:'))
            print("是否继续添加：y/n")
            s = input("确认/取消：")

            stu = Stuent(name,age,gender,score)
            self.__manager_controller.add_student(stu)

            if s == 'n':
                break

    def main(self):
        """
        界面入口
        :return:
        """
        while True:
            self.__display_menu()
            value = input('操作:')
            self.__elect_menu(value)
            if value == '0':
                break

    def show_student(self):
        """
        显示学生信息
        :return:
        """
        for i in self.__manager_controller.stu__list:
            print("id:%d,姓名:%s,年龄:%d,性别:%s,分数:%d" % (i.id,i.name,i.age,i.gender,i.score))

    def remove_student(self):
        """
        删除学生信息
        :return:
        """
        self.show_student()
        print('请输入要删除的学生ID：')
        id = int(input(':'))
        for i in self.__manager_controller.stu__list:
            if i.id == id:
                self.__manager_controller.remove_student(i)

    def update_student(self):
        """
        修改学生信息
        :return:
        """
        self.show_student()
        id = int(input('请输入需要修改的ID：'))
        name = input('姓名:')
        age = int(input('年龄:'))
        gender = input('性别:')
        score = int(input('分数:'))
        stu = Stuent(name,age,gender,score,id)
        self.__manager_controller.update_student(stu)

    def sort_stuent(self):
        """
        学生分数升序排序
        :return:
        """
        self.__manager_controller.sort_student_score()