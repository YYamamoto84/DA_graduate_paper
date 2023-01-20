import make_randominstance2 as instance
import make_cancelation as cancel
import Blockingpair_class as blockpair
import pattarn2 as p2
import randomly_in_matching as randommatch

import numpy as np
import matplotlib.pyplot as plt

#パラメータ

st_members = 10
st_list = list(range(1,st_members+1))

sc_members = 3
sc_list = list(range(1,sc_members+1))

#受け入れ可能人数
sc_capa = [3,3,3]#32行目書き換え忘れずに

#キャンセル人数or割合
c_number = 2

#繰り返し回数
repeat = 20

blockpair_list = []

#k = 2


for i in range(0, repeat):

    sc_capacity = [3,3,3]#直で指定するしかない

    x = instance.make_stlist(st_members, sc_members)
    y = instance.make_sclist(sc_members, sc_capacity, st_members)

    print("x =", x)
    print("y =", y)

    st_instance = instance.make_stInstance(x)
    sc_instance = instance.make_scInstance(y)

    m = instance.matching(st_instance, sc_instance)
    other_students_list = instance.other_students_list
    print("m=",m)
    print("others=",other_students_list)



    #ブロッキングペアを数える
    st_block = blockpair.make_stInstance(x)
    sc_block = blockpair.make_scInstance(y)

    print(blockpair.Countblock(st_block, sc_block, m))

    other_list = other_students_list

    for j in range(0,2):#kの値を変更するときはここを変更


        #ランダムにキャンセルを発生させる
        z = cancel.cancel(m, x, other_list, c_number)
        c_student = cancel.c_student#キャンセルした人だけリストで表示

        print("cancel = ", c_student, z)

        #一部をマッチングし直す（パターン2）
        k = p2.del_cancelstudents(m, sc_capacity, c_student)
        l = p2.not_matched(st_list, z, y, k, other_list, m, c_student)

        print("枠が確定していないstudents", p2.student_1)
        print("キャンセル後のSchools", y)


        new_st_instance = instance.make_stInstance(p2.student_1)#student_1はマッチが決まっていない生徒リスト
        new_sc_instance = instance.make_scInstance(l)


        m3 = instance.matching(new_st_instance, new_sc_instance)
        other_list = instance.other_students_list
        print("m3", m3)
        print("others", other_list)

        #既にペアが決まっている人のマッチと合体させる
        newmatch = p2.newmatch1#空き枠ありのマッチ

        for i in sc_list:
            newmatch[i].extend(m3[i])

        print("newmatch", newmatch)

        print(y)
        print(sc_capacity)
        #print("range", list(range(0,3)))

        for i in range(0,3):
            sc_capacity[i] = sc_capacity[i] - len(m3[i + 1])

        print("capa", sc_capacity)


    #ブロッキングペアを数える（パターン２）
    notmatched_block = blockpair.make_stInstance(z)
    sc_block_3 = blockpair.make_scInstance(y)

    b = blockpair.Countblock(notmatched_block, sc_block_3, newmatch)

    print('!!!', b)
    blockpair_list.append(b)





print(blockpair_list)
sum = sum(blockpair_list)
ave = sum/repeat
print(sum)
print(ave)




#グラフで表示
left = np.array([1])
height = np.array([sum])
label = [1]
plt.bar(left, height, width=0.5, tick_label=label)
#plt.show()
