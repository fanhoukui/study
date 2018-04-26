#!/usr/bin/env python
# -*- coding:utf-8 -*-


# class Student:
#     count = 0
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         Student.count += 1
#
#
# s1 = Student('李坦克', 18, '男')
# s2 = Student('张大炮', 20, '男')
# print("实例化%s个学生" % Student.count)
# print(s1.__dict__)
# print(s1.name)
# print(s2.name)


class Hero:
    def __init__(self, name, nick_name, att, blood):
        self.name = name
        self.nickname = nick_name
        self.att = att
        self.blood = blood

    def hit(self, hero2):
        hero2.blood -= self.att
        print("%s攻击%s,%s被打%s剩余血量%s" % (self.nickname, hero2.nickname, hero2.nickname, self.att, hero2.blood))
        if hero2.blood <= 0:
            print("%s打败了%s！" % (self.name, hero2.name))
            res = "deal"
        else:
            res = "alive"
        return res


h1 = Hero("张大炮", "炮", 800, 1000)
h2 = Hero("李坦克", "坦", 200, 3000)
while True:
    if h1.hit(h2) == "deal" or h2.hit(h1) == "deal":
        break