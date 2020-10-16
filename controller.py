from model import *

class StudentManagerController():
    """
    逻辑控制模型
    """
    stu_id = 1000

    def __init__(self):
        """
        建立学生列表
        """
        self.stu__list = []

    @property
    def get_stu_list(self):
        return self.__stu__list

    def add_student(self, stu):
        """

        :param name: 姓名
        :param age: 年龄
        :param gender: 性别
        :param score: 分数
        :return:
        """
        # id 需要自动生成
        id = self.__genarater_id()
        stu.id = id
        self.stu__list.append(stu)

    def __genarater_id(self):
        """
        生成id
        :return:id
        """
        StudentManagerController.stu_id += 1
        return StudentManagerController.stu_id

    def remove_student(self,stu):
        """
        删除学生
        :param stu:
        :return: None
        """
        for i in self.stu__list:
            if i.id == stu.id:
                self.stu__list.remove(i)

    def update_student(self,stu):
        """
        修改学生信息
        :param stu:学生对象
        :return:
        """
        print("进入方法内部")
        for i in self.stu__list:
            print("进入筛选")
            if i.id == stu.id:
                i.name = stu.name
                i.age = stu.age
                i.gender = stu.gender
                i.score = stu.score
                print(i.__dict__)

    def sort_student_score(self):
        """
        给学生分数排序，从小到大
        :return:
        """
        #最后一位不用比较了
        for i in range(len(self.stu__list)-1):
            for j in range(i+1,len(self.stu__list)):
                if self.stu__list[i].score > self.stu__list[j].score:
                    self.stu__list[i],self.stu__list[j] = self.stu__list[j],self.stu__list[i]