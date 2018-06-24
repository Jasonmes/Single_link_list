# def Modele():
#     print("欢迎进入模块的世界")

zhang = ["张三", 18, "man"]
lisi = ["李四", 28, "female"]
laowu = ["老五", 34, "gay"]
feiwu = ["废物", 189, "freak"]

# 全部名片
Lu = [zhang, lisi, laowu, feiwu]

# 新建名片
def Creat_NewName():
    New_One = []
    newname = input("新的名字：")
    New_One.append(newname)
    newage = int(input("年龄："))
    New_One.append(newage)
    newsex = input("新的性别：")
    New_One.append(newsex)
    Lu.append(New_One)
    return Lu

# 查询名片
def Search_NameCard():
    Search_Name = input("请输入要找的的名字：")
    for i in range(len(Lu)):
        if Search_Name == Lu[i]:
            print(Lu[i])
        else:
            print("输入有误")

def Enter_System(item):

    # ONE = Creat_NewName()
    # TWo = Search_NameCard()
    dict = {"1": "全部名片", "2": ONE, "3": TWo, "4": "退出系统"}
    if item == dict.keys():
        # dict = {1: Creat_NewName(), 2: Lu, 3: Search_NameCard(), 4: "退出系统"}
        # 出错，不能把类作为对象储存，只能是对象。
        print(dict["1"])

Item = input("输入一个选项：")
Enter_System(Item)
