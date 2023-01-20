import make_randominstance2 as instance

import numpy as np
import matplotlib.pyplot as plt


class Student:

    def __init__(self, name, preference):
        self.name = name
        self.preference = preference
        self.pref_higher = []

    def get_keys(self, pair):#マッチしている学校のキーを取得

        key = [k for k, v in pair.items() if self.name in v]
        return key


    def Prefer(self,pair):#マッチしている学校より好ましい学校があるか調べる

        if self.get_keys(pair) == []:#Pairに入ってない場合
            self.pref_higher = self.pref_higher + self.preference
            return self.pref_higher

        else:
            x = self.preference.index(self.get_keys(pair)[0])

            for i in range(0,len(self.preference)):
                if i < x:
                    self.pref_higher.append(self.preference[i])
            return self.pref_higher


class School:
    def __init__(self, name, capacity, preference):
        self.name = name
        self.preference = preference
        self.capacity = capacity


def Countblock(students,schools,pair):

    global blockingpair
    blockingpair = 0

    for student in students:
        print("student = ", student.name, "prefer", student.Prefer(pair))

        for school in schools:

            #生徒のpref_higherリストの中に、schoolのnameが入っていたら
            if school.name in student.pref_higher:
                print("school = ", school.name)

                x = pair.get(school.name)#Schoolが現在マッチしているstudentを取得

                print("school", school.name, "now matches student", x)
                print(school.preference)

                for i in x:

                    if school.preference.index(student.name) < school.preference.index(i):
                        print("blockpair true")
                        blockingpair += 1
                        print("now blockingpair" , blockingpair)

                    else:
                        print("blockpair false")
                        print("now blockingpair ", blockingpair)
    return blockingpair

#===========================================================

#生徒のインスタンス化
def make_stInstance(students):

    st_instance_list = []

    for p in students:
        name, preference = p
        st_instance = Student(name, preference)
        st_instance_list.append(st_instance)

    return st_instance_list


#学校のインスタンス化
def make_scInstance(schools):

    sc_instance_list = []

    for q in schools:
        name, capacity, preference = q
        sc_instance = School(name, capacity, preference)
        sc_instance_list.append(sc_instance)

    return sc_instance_list
