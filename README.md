信息管理系统

需求
	实现对学生信息的增加、删除、修改和查询。
分析
界面可能使用控制台，也可能使用Web等等。
1.识别对象：界面视图类     逻辑控制类     数据模型类

2.分配职责：
界面视图类：负责处理界面逻辑，比如显示菜单，获取输入，显示结果等。
逻辑控制类：负责存储学生信息，处理业务逻辑。比如添加、删除等
数据模型类：定义需要处理的数据类型。比如学生信息。


3.建立交互：
界面视图对象  <----> 数据模型对象   <---->  逻辑控制对象
设计
	数据模型类：StudentModel	
		数据：编号 id,姓名 name,年龄 age,成绩 score 
	逻辑控制类：StudentManagerController	
		数据：学生列表 __stu_list 
		行为：获取列表 stu_list,添加学生 add_student，删除学生remove_student，修改学生update_student，根据成绩排序order_by_score。
	界面视图类：StudentManagerView
		数据：逻辑控制对象__manager
		行为：显示菜单__display_menu，选择菜单项__select_menu_item，入口逻辑main，
输入学生__input_students，输出学生__output_students，删除学生__delete_student，修改学生信息__modify_student

