def frequently_used(file):
    reverse_dic = {}
    mydic = each_word(file)  # the result of task2 callable,return mydic
    for key in mydic:
        val = mydic[key]

        if val not in reverse_dic:
            reverse_dic[val] = [key]
        else:
            reverse_dic[val].append(key)

    f = sorted(reverse_dic)[::-1]
    for n in range(20):
        print(reverse_dic[f[n]])

