import make_cancelation as cancel
import random



#キャンセルした生徒を現在のマッチから外す
def del_cancelstudents(pair, sc_capacity, st_cancel):

    for i in range(0,len(sc_capacity)):
        sc_capacity[i] = 0

    for i in pair.values():
        for j in st_cancel:

            if j in i:
                key = [k for k, v in pair.items() if v == i]#jが入っている辞書のキーを出す

                x = pair[key[0]]
                x.remove(int(j))
                print(sc_capacity[key[0]-1])
                
                sc_capacity[key[0]-1] = sc_capacity[key[0]-1] + 1

    global newmatch1
    newmatch1 = pair
    print("キャンセル者が出た後のmatch", newmatch1)

    return sc_capacity



def not_matched(st_list, student, school, sc_capacity, others, pair, st_cancel):#studentはキャンセル後の選好

    #まだマッチができていない生徒だけを表示、リスト化
    list = others + st_cancel
    print("list", list)


    others = []

    global student_1
    student_1 = [k for k in student if k[0] in list]

    #print("マッチが決まっていない生徒リスト", student_1)


    #キャンセルした人以外の人を出す
    already_matched = [i for i in st_list if i not in list]

    print("already_matched", already_matched)


    for s in school:
        s[1] = sc_capacity[school.index(s)]

    return school
