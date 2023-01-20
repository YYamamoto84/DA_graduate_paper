import make_randominstance2 as instance
import make_cancelation as cancel
import Blockingpair_class as blockpair
import pattarn2 as p2
import randomly_in_matching as randommatch

import numpy as np
import matplotlib.pyplot as plt

#パラメータ

st_members = 100
st_list = list(range(1,st_members+1))

sc_members = 3
sc_list = list(range(1,sc_members+1))

#受け入れ可能人数
sc_capa = [10,10,10,10,10,10,10,10,8,8]#32行目書き換え忘れずに

#キャンセル人数or割合
c_number = int(st_members*0.05)

#繰り返し回数
repeat = 1000

blockpair_list = []


for i in range(0, repeat):

    sc_capacity = [10,10,10,10,10,10,10,10,8,8]#直で指定するしかない


    x = instance.make_stlist(st_members, sc_members)
    y = instance.make_sclist(sc_members, sc_capacity, st_members)

    print("x =", x)
    print("y =", y)

    st_instance = instance.make_stInstance(x)
    sc_instance = instance.make_scInstance(y)



    m = instance.matching(st_instance, sc_instance)
    print("m=",m)
    other_students_list = instance.other_students_list
    print("others=",other_students_list)



    #ブロッキングペアを数える
    st_block = blockpair.make_stInstance(x)
    sc_block = blockpair.make_scInstance(y)

    print(blockpair.Countblock(st_block, sc_block, m))



    #ランダムにキャンセルを発生させる

    z = cancel.cancel(m, x, other_students_list, c_number)
    cancelstudent = cancel.c_student#キャンセルした人だけリストで表示
    print("cancel = ", z)



    #全員マッチングし直す（パターン1）

    c_instance = instance.make_stInstance(z)
    sc_instance = instance.make_scInstance(y)
    print(y)

    m2 = instance.matching(c_instance, sc_instance)
    other_students_list2 = instance.other_students_list

    print("m2 =", m2)
    print("others=", other_students_list2)



    #ブロッキングペアを数える

    c_block = blockpair.make_stInstance(z)
    sc_block_2 = blockpair.make_scInstance(y)

    print(blockpair.Countblock(c_block, sc_block_2, m2))




    #一部をマッチングし直す（パターン2）

    k = p2.del_cancelstudents(m, sc_capacity, cancelstudent)
    l = p2.not_matched(st_list, z, y, k, other_students_list, m, cancelstudent)

    print("枠が確定していないstudents", p2.student_1)
    print("キャンセル後のSchools", y)

    new_st_instance = instance.make_stInstance(p2.student_1)#student_1はマッチが決まっていない生徒リスト
    new_sc_instance = instance.make_scInstance(l)


    m3 = instance.matching(new_st_instance, new_sc_instance)
    print("m3", m3)
    print("others", instance.other_students_list)


    #既にペアが決まっている人のマッチと合体させる
    newmatch = p2.newmatch1#空き枠ありのマッチ


    #'''

    #！！！パターン3をチェックするときはここをコメントアウト

    for i in sc_list:
        newmatch[i].extend(m3[i])

    print("newmatch", newmatch)


    #ブロッキングペアを数える（パターン２）
    print(z)
    print(y)

    notmatched_block = blockpair.make_stInstance(z)
    sc_block_3 = blockpair.make_scInstance(y)

    b = blockpair.Countblock(notmatched_block, sc_block_3, newmatch)

    print('!!!', b)
    blockpair_list.append(b)

    '''

    #ランダムに入れる（パターン3）
    key = list(set(cancel.keylist))
    print(key)
    print("newmatch!!", p2.newmatch1)

    k = randommatch.Randommatch(p2.student_1, sc_list, k, p2.newmatch1, key)
    print("k",k)

    random_st_instance = blockpair.make_stInstance(z)
    random_sc_instance = blockpair.make_scInstance(y)

    c = blockpair.Countblock(random_st_instance, random_sc_instance, k)

    print('!!!', c)
    blockpair_list.append(c)

    #'''




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
