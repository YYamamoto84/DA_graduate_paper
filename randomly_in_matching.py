import random


def Randommatch(student, sc_list, sc_capacity, pair, key):
    print(student)
    randomlist = []

    while len(key) > 0:

        #空き枠がある学校から1つ選ぶ
        x = random.choice(key)
        randomlist.append(x)
        key.remove(x)

    print("randomlist", randomlist)

    for i in randomlist:
        print(randomlist)
        print("randomlist_i", i)
        handed_st = []

        for j in student:
            if i in j[1]:
                handed_st.append(j[0])

        print('handed_st', handed_st)

        #選好提出した人の中から空き枠の数だけ人を選ぶ
        if len(handed_st) < sc_capacity[i-1]:
            pair[i].extend(handed_st)



        else:
            h = random.sample(handed_st, sc_capacity[i-1])
            pair[i].extend(h)

            for i in h:
                for j in student:
                    if j[0] == i:
                        student.remove(j)


    return pair
