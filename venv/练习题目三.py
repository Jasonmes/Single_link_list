# # # 输入一串字符，分别统计出字母，数字，空格和其他符号的个数
# # # cording:utf-8
# #
# # import string
# # Str = input("input a string,you like:")
# # Letter = 0
# # Space = 0
# # Digit = 0
# # Others = 0
# # for c in Str:
# #     if c.isalpha():
# #         Letter += 1
# #     elif c.isspace():
# #         Space += 1
# #     elif c.isdigit():
# #         Digit += 1
# #     else:
# #         Others += 1
# #
# # print(Letter)
# # print(Space)
# # print(Digit)
# # print(Others)
# # # print("%d%d%d%d")%(Letter,Space,Digit,Others)
# # print("Letter=%d Space=%d Digit=%d Others=%d") % (Letter, Space, Digit, Others)
#
#
# # 求s=a+aa+aaa+aaaa+aaaaa，例如：2+22+222+2222+22222，五个数字相加
# # 取得个位数，每个数字只需要添加个位数
# # 先定义总和
# # 得到下一个数，个位数不变，每个数字只需要添加个位数
# # 下一个循环就是下一个数，所以交换数值
# # a_number = int(input("输入一个个位数："))
# # a = a_number
# # Sum = 0
# # for i in range(1,6):
# #     Sum += a_number
# #     A_number = a_number * 10 + a
# #     a_number = A_number
# # print(Sum)
#
# # print("=======")
# # print(Sum)
#
# # Tn = 0
# # Sn = []
# # n = int(input("input a nuber:"))
# # a = int(input("input a nuber:"))
# # for count in range(n):
# #     Tn = Tn + a
# #     a = a * 10
# #     Sn.append(Tn)
# # Sn = lambda x,y : x+y, Sn
# # print(Sn)
#
# # 一个数如果恰好是等于它的因子只和，这个数就称为完数。例如6=1+2+3。找出1000以内的所有完数
#
# # Sum = []
# # yinzijihe = []
# # # 从1开始
# #
# # for i in range(1,1001):
# #     # 每得到一个数，遍历这个数字，得到因子
# #     for j in range(1,i):
# #         if i % j == 0:
# #             # 收集这些因子
# #             yinzijihe.append(j)
# #         for a in range(len(yinzijihe)):
# #             sum = 0
# #             sum += a
# #             if sum == i
# #                 Sum.append(i)
# #
# # print(Sum)
#
#
# # # 一球从100米高度自由落下，每次落地后反弹回原高度的一半：再落下，求它在第十次落地时，经过了多少米？第十次反弹高度多高？
# #
# # Start = 100
# # Sum = 0
# # f = []
# # for i in range(10):
# #     Sum += Start
# #     a = Start/2
# #     Start = a
# #     # 收集每个高度的数据
# #     f.append(a)
# # print("第十次高度是%f米"%f[9])
# # print("总经过路程%f米"%Sum)
#
# # 猴子第一天摘了很多桃子，当天吃了一半，嘴馋吃多了一个；第二天又吃了一半，还是因为嘴馋又吃一个。。。。。。第十天只剩1一个桃子了，请问猴子摘了多少桃子
# # 这样理解，当天的桃子数加1再乘以一半就等于前一天的数量，10天，减掉已知的一天，循环9次
# # # 最后一天的数量
# # day = 1
# # Sum = 0
# # r = [1]
# # for i in range(9):
# #     Sum += day
# #     Pref = (day + 1) * 2
# #     day = Pref
# #     r.append(Pref)
# # print(Sum)
# # print(r)
#
# # for i in range(9,0,-1):
# #     print(i)
#
# #
# '''
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# # '''
# # from sys import stdout
# # for i in range(4):
# #     for j in range(2 - i + 1):
# #         stdout.write(" ")
# #     for k in range(2 * i + 1):
# #         stdout.write("*")
# #     print("\n")
# #
# # for i in range(3):
# #     for j in range(i + 1):
# #         stdout.write(" ")
# #     for k in range(4 - i * 2 + 1):
# #         stdout.write("*")
# #     print("\n")
#
# # # 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13，。。。。。求这个数列20项之和
# # i = 2
# # j = 1
# # Sum = 0
# # s = []
# # for k in range(10):
# #     san = i / j
# #     i, j = i + j,i
# #     # S.append(san)
# #     Sum += san
# #     # 收集它们，看看是否准确
# #     s.append("%d/%d"%(i , j))
# # print(Sum)
# # print(s)
#
#
# # lu = []
# # a = 2
# # b = 1
# # for n in range(1, 21):
# #     b, a = a, a + b
# #     lu.append(a/b)
# # C = (lambda x, y: x + y, lu)
# # print(C)
#
# # 求1+2!+3!+4!.......20!
# #
# # j = 1
# # He = 0
# # for i in range(1,21):
# #     sum = j * i
# #     j = sum
# #     He += sum
# #     print(j)
# #     # print(sum)
# # print(He)
# # ================================================================================
# # 利用递归方法求5！
# # fn = fn_1*4!
# # ================================================================================
# # 26 -- 28 题目
#
# # 给一个不多于5位的正整数，要求：一，求他是几位数，逆序打出各位数字。
#
# # 转为字符串的形式更好处理
# # number = int(input("input your number:"))
# # Number = str(number)
# # L = int(len(Number))
# # LU = []
# # for i in range(L):
# #     LU.append(Number[L-i-1])
# # print(LU)
#
#
#
#
# # 一个五位数，判断是不是回文数
# # # 即12321是回文数#
# # number = int(input("input your number:"))
# # Number = str(number)
# # if Number[0] == Number[4] and Number[1] == Number[3]:
# #     print("这是一个回文数")
# # else:
# #     print("这不是一个回文数")
#
# #
# # number = int(input("input your number:"))
# # MUM = str(number)
# # Nu = int(len(MUM))
# # # 左右各占一半的长度为
# # Half = int(Nu-1)/2
# # if Nu % 2 != 0:
# #     for i in range(1, Half+1):
# #         # 才是中间的那个不用加上1，然后依次判断左右是否相等
# #         # 中间那个数是MUM[Half]
# #         # i最后停止于4
# #         # 保证循环次数为Half
# #         if MUM[Half - i] == MUM[Half + i] and i == Half:
# #             print("这是一个回文数")
# #     print(":这不是回文数")
# # else:
# #     print("：这不是回文数")
#
#
#
#
#
#
# # # 请输入星期几的第一个字母来判断是星期几，如果第一个字母一样，则继续判断第二个字母
# # mo
# # tu
# # we
# # th
# # fr
# # sa
# # su
#

# Week = ["m", "tu", "w", "th", "f", "sa", "su"]

# week1 = {"m":"星期一", "w":"星期三", "f":"星期五"}
# week2 = {"tu":"星期二", "th":"星期四", "sa":"星期六", "su":"星期日"}
# Day_one = input("输入第一个字母:")
# STR = ""
#
# for KEY in week1.keys():
#     if Day_one == KEY:
#         print(week1[Day_one])
#         break
#
#     else:
#         Day_two = input("输入第二个字母：")
#         STR = Day_one + Day_two
#         for KEYS in week2.keys():
#             if STR == KEYS:
#                 print(week2[STR])
#     break


# # press any key to change color,do you want to try it,hurry up
# # import ctypes, sys
# #
# # STD_INPUT_HANDLE = -10
# # STD_OUTPUT_HANDLE = -11
# # STD_ERROR_HANDLE = -12
# #
# # # Windows CMD命令行 字体颜色定义 text colors
# # FOREGROUND_BLACK = 0x00  # black.
# # FOREGROUND_DARKBLUE = 0x01  # dark blue.
# # FOREGROUND_DARKGREEN = 0x02  # dark green.
# # FOREGROUND_DARKSKYBLUE = 0x03  # dark skyblue.
# # FOREGROUND_DARKRED = 0x04  # dark red.
# # FOREGROUND_DARKPINK = 0x05  # dark pink.
# # FOREGROUND_DARKYELLOW = 0x06  # dark yellow.
# # FOREGROUND_DARKWHITE = 0x07  # dark white.
# # FOREGROUND_DARKGRAY = 0x08  # dark gray.
# # FOREGROUND_BLUE = 0x09  # blue.
# # FOREGROUND_GREEN = 0x0a  # green.
# # FOREGROUND_SKYBLUE = 0x0b  # skyblue.
# # FOREGROUND_RED = 0x0c  # red.
# # FOREGROUND_PINK = 0x0d  # pink.
# # FOREGROUND_YELLOW = 0x0e  # yellow.
# # FOREGROUND_WHITE = 0x0f  # white.
# #
# # BACKGROUND_BLUE = 0x10  # dark blue.
# # BACKGROUND_GREEN = 0x20  # dark green.
# # BACKGROUND_DARKSKYBLUE = 0x30  # dark skyblue.
# # BACKGROUND_DARKRED = 0x40  # dark red.
# # BACKGROUND_DARKPINK = 0x50  # dark pink.
# # BACKGROUND_DARKYELLOW = 0x60  # dark yellow.
# # BACKGROUND_DARKWHITE = 0x70  # dark white.
# # BACKGROUND_DARKGRAY = 0x80  # dark gray.
# # BACKGROUND_BLUE = 0x90  # blue.
# # BACKGROUND_GREEN = 0xa0  # green.
# # BACKGROUND_SKYBLUE = 0xb0  # skyblue.
# # BACKGROUND_RED = 0xc0  # red.
# # BACKGROUND_PINK = 0xd0  # pink.
# # BACKGROUND_YELLOW = 0xe0  # yellow.
# # BACKGROUND_WHITE = 0xf0  # white.
# #
# # # get handle 获取输出窗口的句柄
# # std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
# #
# #
# # def set_cmd_text_color(color, handle=std_out_handle):
# #     Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
# #     return Bool
# #
# #
# # # reset white
# # def resetColor():
# #     set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
# #
# #
# # # 绿色
# # # green
# # def printgreen(str):
# #     set_cmd_text_color(FOREGROUND_GREEN)
# #     sys.stdout.write(str)
# #     resetColor()
# #
# #
# # # 天蓝色
# # # sky blue
# # def printSkyBlue(str):
# #     set_cmd_text_color(FOREGROUND_SKYBLUE)
# #     sys.stdout.write(str)
# #     resetColor()
# #
# #
# # # 白底暗粉字
# # def printWHITEDARKPINK(str):
# #     set_cmd_text_color(BACKGROUND_WHITE | FOREGROUND_DARKPINK)
# #     sys.stdout.write(str)
# #     resetColor()
# #
# #
# # # 绿底粉字
# # def printYellowPink(str):
# #     set_cmd_text_color(BACKGROUND_GREEN | FOREGROUND_PINK)
# #     sys.stdout.write(str)
# #     resetColor()
# #
# #
# # # 黄底红字
# # def printYellowRed(str):
# #     set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
# #     sys.stdout.write(str)
# #     resetColor()
# #
# #
# # if __name__ == '__main__':
# #     print
# # printSkyBlue(u'printSkyBlue:天蓝色文字\n')
# # input("please press any key")
# # printYellowRed(u'printYellowRed:黄底红字输出\n')
# # input("please press any key")
# # printYellowPink(u'printYellowPink:绿底粉字输出\n')
# # input("please press any key")
# # printWHITEDARKPINK(u'printWHITEDARKPINK:白底暗粉字输出\n')
#
# # 学习gotoxy() clrscr()
# # 文本颜色设置
#
# # 求100之内的素数
# # Su = []
# # for i in range(1,101):
# #     if i / 1 == i and i/i == 1:
# #         for j in range(1,101):
# #             if j <= i and i % j != 0:
# # #
# #
# # print(Su)
#
#
#
#
#
#
#
#
#
#
#
# # 对10个数进行排序
#
# # Zha = []
# # for i in range(10):
# #     zha = int(input("input ten number:"))
# #     Zha.append(zha)
# # print(sorted(Zha))
#
#
#
#
# # 求一个3*3矩阵对角线元素之和
# # 有一个排序好的数组，现在输入一个数字，要求按照用来的规律插入数组中，
#
#
# # 将一个数组逆序输出
#
# # Hao = [11,2,4,8,9,6,3,1111,22,98]
# # Hao = sorted(Hao)
# # # reverse()不带参数
# # Hao.reverse()
# # print(Hao)
# # print(Hao[::-1])
#
#
# #
# # def queen(A, cur=0):
# #     if cur == len(A):
# #         print(A)
# #         return 0
# #     for col in range(len(A)):
# #         A[cur], flag = col, True
# #         for row in range(cur):
# #             if A[row] == col or abs(col - A[row]) == cur - row:
# #                 flag = False
# #                 break
# #         if flag:
# #             queen(A, cur+1)
# # queen([None]*8)
#
#
#
# # 学习static定义静态变量的方法
# # 学习使用auto定义变量的用法
# # 学习使用static的另一种用法
# # 学习使用external的用法
# # 学习使用register定义变量的方法
# # 宏#define命令练习一，二，三
#  #if #ifdef #ifndef的综合应用
# # 学习使用按位与&
# # 0&0=0，1&0=0，1&1=0
# # 学习使用按位或|
# # 学习使用按位异或^
# # 学习使用按位取反～
# # 画图，学会circle画圆形
# # 画图，学用line画直线
# # 画图，学用rectangle画方形
#
# # 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
# # lu = []
# # for i in range(10):
# #     ao = int(input("依次输入10个数字："))
# #     lu.append(ao)
# # Lu = sorted(lu)
# # lu[0], lu[int(len(Lu))-1] = Lu[int(len(Lu))-1], Lu[0]
# # print(lu)
#
#
# # 有M个整数，使其前面各数顺序向后移N个位置，最后N个数变成最前面的N个数。
# # 这样理解，就像一杯水，你用手压这杯水，最下面的水就跑到最上面了
# # lu = []
# # nu = []
# # for j in range(N - 1):
# #     nu.append(lu[int(len(lu)) - j])
# #
# # for i in range(M - 3):
# #     nu.append(lu[i])
# # print(nu)
#
#
# # 用list模拟结构（不使用class）
#
#
#
#
# # 创建两个节点，连接两个节点
# # 创建两个链表，并且连接两个链表
#
# # 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+。。。。1/n，当输入n为奇数的时，调用函数1/1+1/3+。。。1/n(利用指针函数)
# # def Test(item):
# #     if item % 2 == 0 and item != 0:
# #         OUshu(item)
# #     else:
# #         JIshu(item)
# #
# # def OUshu(item):
# #     sum = 0
# #     if item >= 2:
# #         for i in range(item/2):
# #             sum += 1/(item - 2 * i)
# #     print(sum)
# #
# # def JIshu(item):
# #     sum = 0
# #     if item >= 1:
# #         for i in range(item/2):
# #             sum += 1/(item - 2 * i)
# #     print(sum)
# #
# #
# # X = int(input("a number:"))
# # Test(X)
# # # print(type(X))
#
# # 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5，然后用和除以10的余数代替该数字，再将第一位第四位数字交换，第二位和第三位交换
# # 公司又如何把得到的数据转换成原数据呢
# # 1.每位数字都加上5
# # 2.用和除以10的余数代替该数字
#
# # T = "1234"
# # Test = int(T)
# # test = []
# # for i in range(4):
# #     # test.append(Test[i]+5)
# #     test.append((Test[i] + 5) % 10)
# # # 3.再将第一位第四位数字交换
# # test[0], test[3] = test[3], test[0]
# #
# # # 4.第二位和第三位交换
# # test[1], test[2] = test[2], test[1]
# # print(test)
#
#
# # 思考一个问题，如何根据得到的数据来推断传送进来的数是什么样子的
# #   9876 or 4321 == 1,2,3,4
# #     余数是0的只有5
#
# # 计算字符串中子串出现的次数
# # string = input("enter a string:")
# # str = input("enter a str:")
# # Count = string.count(str)
# # print(Count)
#
# # # 从键盘输入一些字符，逐个把他们送到磁盘上面去，直到输入一个#为止
# Input = input("enter:")
# with open("/Users/jason/Downloads/未命名.txt", "w") as FIle:
#     if Input == "#":
#         print()
#     else:
#         FIle.write(Input)
#         print(FIle)
#
# del FIle
# print(FIle)

str = "2018 01 01"
strq = str.split("0")
print(strq)





# # 从键盘呼入一个字符串，将小写字母全部换成大写字母，然后输出到一个磁盘文件"test"中保存，输入的字符串用！结束
# # 有两个磁盘文件，A，B，各存放一行字母，要求把这两个文件中的信息合并，按照字母顺序排列，输出到一个新的文件夹中
#
#
#
#
# # a = "1234"
# # B = []
# # for i in range(4):
# #     B.append(int(a[i]))
# # print(B)
