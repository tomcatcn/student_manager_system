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