# # 烤鸡腿
# class Chiken(object):
#     def __init__(self):
#         self.cook_time = 0
#         #self.Veg_Material = []  # 佐料材料
#
#
#
#
#     def CooKTime(self, Ctime):
#
#         if Ctime > 0 and Ctime < 3:
#             print("三成熟的地瓜，烤了%s分钟" % Ctime)
#         elif Ctime > 3 and Ctime <7:
#             print("半成熟的地瓜，烤了%s分钟" % Ctime)
#         elif Ctime > 7 and Ctime <10:
#             print("熟了，享用吧，用时 % s" % Ctime)
#         elif Ctime > 10:
#             print("烤糊的地瓜只需要超过%s分钟" % Ctime)
#         else:
#             print("输入时间有误")
#             return
#
#
# you_time = input("enter your time:")
# big_Chiken = Chiken()
# big_Chiken.cook_time(you_time)

class bigdatui(object):
    def __init__(self):
        self.state = "生的"
        self.cook = 0
        self.Material = []

    def cookTime(self, time):  # 参数最好小写
        self.cook += time
        if self.cook <= 0:
            self.state = "生的"
        elif 0 < self.cook < 7:
            self.state = "半生不熟"
        elif 7 < self.cook < 10:
            self.state = "熟了"
        else:
            self.state = "烤糊了"

    def add_material(self, material):
        self.Material.append(material)

    def __str__(self):
        # 一般做成返回值return最好
        return "此大腿状态是%s,烤了%s分钟，用了%s这些材料" % (self.state, self.cook, self.Material)


Datui = bigdatui()
Enter_time = int(input("输入你喜欢的时间:"))

for i in range(10):
    if Datui.cook > 10:
        print(Datui)
        break
    else:
        MaTerial = input("放入你喜欢的佐料:")
        Datui.cookTime(Enter_time)
        Datui.add_material(MaTerial)
        print(Datui)
        i += 2