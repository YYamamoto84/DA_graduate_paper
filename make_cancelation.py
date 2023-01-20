import make_randominstance2 as instance
import random


def cancel(pair, students, others, c_number):

    #既にマッチしている人のインデックスを表示
    st_matched = [x[0] for x in students if x[0] not in others]
    #print("#", st_matched)


    #キャンセルした人のindexを表示
    global c_student
    c_student = random.sample(st_matched, c_number)
    #print("cancel =", c_student)

    global keylist
    keylist = []

    for i in c_student:

        #print(students)
        cancel  = students[i-1]#キャンセルした人
        #print("cancel =", cancel)

        key = [k for k, v in pair.items() if i in v]#キャンセルした人とマッチしていた学校のキー
        print("keylist", keylist)
        
        keylist.append(key[0])
        print("key=",key)

        x = cancel[1].index(key[0])#keyの選好リストにおける選好順

        del cancel[1][x]#cancel[1] = 選好リスト


    #print("!!!=", students)
    return students
