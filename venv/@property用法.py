# coding=utf-8

class student(object):
    #需要继承父类object，否则property等无法生效
    def __init__(self, v_id="000"):
        self.__id = v_id

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, v_score):
        if not isinstance(v_score, int):
            raise ValueError("score must be an integer!")
        if v_score < 0 or v_score > 100:
            print("Not exit")
        else:
            print(v_score, "operation success")
        self.score = v_score
    @property
    def get_id(self):
        return self.__id

s = student("001")
s.score = 60
print(s.get_id)
print(s.score)

s = student()
s.score = -100
print(s.get_id)
print(s.score)



