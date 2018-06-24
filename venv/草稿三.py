class DOG:
    def __init__(self, name, *args):
        # print("调用了初始化")
        self.name = name
        # print("世界送了你一只小狗叫%s"%(self.name))

    def eatShit(self, food):
        self.food = food
        print("%s正在%s"%(self.name, self.food))

    def action(self, action, *args):
        self.action = action
        print("%s正在%s"%(self.name, self.action))
        self.eatShit(args)

    def __str__(self):
        return "%s见上帝了" % self.name

    def kill_self(self):
        self.__str__()

    def __ouyou__(self):
        print("新的调用")



xiaohuang = DOG("小黄")
# xiaohuang.food = "吃屎"
# xiaohuang.action("加入狗仔队", xiaohuang.food)
# print(xiaohuang)
print(xiaohuang)

