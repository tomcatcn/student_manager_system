class Stuent():
    """
    学生模型
    """
    def __init__(self,name="",age=0,gender=None,score=0,id=0):
        """
        给学生对象赋值
        :param name: 姓名
        :param age: 年龄
        :param gender: 性别
        :param score: 分数
        :param id: 唯一标示
        """
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

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
        for i in self.stu__list:
            if i.id == stu.id:
                i.name = stu.name
                i.age = stu.age
                i.gender = stu.gender
                i.score = stu.score


#测试代码
if __name__ == "__main__":
    stu = Stuent("xiao",15,'man',60)
    stu1 = Stuent("xiao",16,'man',80)
    stu2 = Stuent("xiao",17,'man',90)
    stu3 = Stuent("hong", 17, 'man', 90,id = 1001)
    sc = StudentManagerController()
    sc.add_student(stu)
    sc.add_student(stu1)
    sc.add_student(stu2)
    sc.update_student(stu3)
    for i in sc.stu__list:
        print(i.name,i.age,i.id)
