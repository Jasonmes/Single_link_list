# cording:utf-8

class Node(object):
    def __init__(self, elem):
        """节点"""
        self.elem = elem
        self.next = None


class Single_Link_list(object):

    def __init__(self, node=None):
        self._head = node


    def is_empty(self):
        """判断链表是否为空"""
        return self._head== None
        pass

    def length(self):
        """链表长度"""
        """current游标，用来遍历节点"""
        """count来计数"""
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def travel(self):
        """遍历单链表"""
        current = self._head
        while current != None:
            print(current.elem)
            current = current.next



    def add(self,item):
        """链表头部增加元素"""

        # 创建一个节点
        # 保存单链表的一个节点作为新节点的下一个节点
        # 把新节点赋值给self头节点

        node = Node(item)
        node.next = self._head
        self._head = node

        pass


    def appended(self,item ):
        """链表尾部增加元素"""
        """创建一个节点，然后遍历所有节点找到最后一个节点，最后把赋值一个末尾节点"""
        node = Node(item)

        if self.is_empty():
            self._head = node
        else:
            current = self._head
            while current != None:
                current = current.next
            current.next = node






    def insert(self, pos, item):
        # pos指添加的位置
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length()-1:
            self.appended(item)
        else:
            # pre是链表的第一个节点
            # 包含有elem，next属性
            pre = self._head
            count = 0
            # 得到pre后就往后面移动pos-1个单位，于是pre将找到你要插入的前面节点位置
            while count <= pos - 1:
                pre = pre.next
                count += 1
            # 当循环结束后，pre指向插入的位置
            node = Node(item)
            # 将创建的node与pre的下一个节点的头连接
            # pre.next是pre的下一个节点，把下一个节点改为node的下一个节点
            node.next = pre.next
            # 将node与pre的节点的尾部连接
            # 这两个步骤不能调换，调换就是不理解了
            pre.next = node

    def remove(self, item):
        """链表移走或者删除元素"""
        # 删掉之后得链接起来
        # 删除节点
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self._head:
                    self._head=cur.next
                else:
                    pre.next = cur.next
            # 链接删除节点的前一个节点和后一个节点
            pre.next = cur.next



    def search(self, item):
        """搜索元素"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


# #创建一个对象
# node=Node(100)
# single_obj=Single_Link_list(node )
# single_obj.travel()
# print(single_obj._head)

if __name__ == "__main__":
    Text = Single_Link_list()
    print(Text.is_empty())
    print(Text.length())
    print("==one=================")

    Text.appended(1)
    print(Text.is_empty())
    print(Text.length())
    print("==two=================")

    Text.appended(2)
    Text.appended(3)
    Text.appended(4)
    Text.appended(5)
    Text.appended(6)
    Text.appended(7)
    Text.travel()
    Text.insert(4,100)

