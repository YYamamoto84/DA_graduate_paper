import random


class Student:
    def __init__(self, name, preference):
        self.preference = preference
        self.name = name
        self.rejectcount = 0

    def tempPref(self):
        return self.preference[self.rejectcount]

class School:


    def __init__(self, name, capacity, preference):
        self.name = name
        self.capacity = capacity
        self.preference = preference

        self.temporaryList = []


    def sortstudent(self, student):
        self.temporaryList.insert(0, student)

        for tempstudent in self.temporaryList[::-1]:
            last = self.temporaryList.index(tempstudent)

            if self.preference.index(tempstudent.name) < self.preference.index(student.name):
                self.temporaryList.insert(last+1, student)
                del self.temporaryList[0]
                break

        return self


    def choice(self, student):

        if self.capacity > len(self.temporaryList):
            return None, self.sortstudent(student)

        elif self.capacity == 0:
            rejectstudent = student
            rejectstudent.rejectcount += 1
            return rejectstudent, self

        elif self.preference.index(student.name) < self.preference.index(self.temporaryList[-1].name):

            rejectstudent = self.temporaryList[-1]
            rejectstudent.rejectcount += 1
            del self.temporaryList[-1]
            return rejectstudent, self.sortstudent(student)


        else:
            rejectstudent = student
            rejectstudent.rejectcount += 1
            return rejectstudent, self






# one to many DA algorithm
def matching(students, schools):
    poolList = students
    differdAccept = schools

    global other_students_list
    other_students_list = []

    other_students_list.clear()
    print("cleared",other_students_list)


    # poolListが空になる（全員の配属が決定）まで提案と諾否の決定を続ける。
    while len(poolList)>0:

        if poolList[0].rejectcount < len(schools) and poolList[0].rejectcount + 1 <= len(poolList[0].preference):


            school = next(school for school in differdAccept if school.name == poolList[0].tempPref())
            index = schools.index(school)

            select = school.choice(poolList[0])

            if select[0] == None:
                del poolList[0]
                differdAccept[index] = school

            else:
                del poolList[0]
                poolList.append(select[0])
                differdAccept[index] = school

        elif poolList[0].rejectcount + 1 > len(poolList[0].preference):
            other_students_list.append(poolList[0].name)
            del poolList[0]
            differdAccept[index] = school

        else:
            other_students_list.append(poolList[0].name)
            del poolList[0]
            differdAccept[index] = school

    matching = {}
    for school in differdAccept:
        result = []
        for student in school.temporaryList:
            result.append(student.name)
        matching[school.name] = result
    return matching





def make_stlist(st_members, sc_members):

    members_students = range(1, sc_members+1)

    #生徒の学校に対する選好
    st_preference = []
    for i in range(0, st_members):
        x = random.sample(members_students, sc_members)
        st_preference.append(x)

    #生徒のname,preferenceのリストを作る
    student = []

    #list1に結果を格納
    st_name = 0
    for i in range(0, st_members):
        st_name += 1
        list1 = [st_name, st_preference[i]]
        student.append(list1)

    return student


def make_sclist(sc_members, sc_capacity, st_members):

    members_schools = range(1, st_members+1)

    #学校の生徒に対する選好
    sc_preference = []
    for i in range(0,sc_members):
        y = random.sample(members_schools, st_members)
        sc_preference.append(y)

    #学校のname,capacity,preferenceのリストを作る
    school = []

    #list2に結果を格納
    sc_name = 0
    for i in range(0,sc_members):
        sc_name += 1
        list2 = [sc_name, sc_capacity[i], sc_preference[i]]
        school.append(list2)

    return school



#生徒のインスタンス作成
def make_stInstance(students):

    st_instance_list = []

    for p in students:
        name, preference = p
        st_instance = Student(name, preference)
        st_instance_list.append(st_instance)

    return st_instance_list


def make_scInstance(schools):

    sc_instance_list = []

    for q in schools:
        name, capacity, preference = q
        sc_instance = School(name, capacity, preference)
        sc_instance_list.append(sc_instance)

    return sc_instance_list
