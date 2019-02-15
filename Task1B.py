def frequently_used(file):
    reverse_dic = {}

    f = open(file)
    mylist = list()
    mylist2 = list()
    mydic = dict()
    import string

    for line in f:
        mylist.append(line)

    for word in mylist:
        word = word.strip(string.whitespace)
        word = word.lower()

        for punc in string.punctuation:
            word = word.replace(punc, ' ')

        for i in word.split(' '):
            mylist2.append(i)

    for key in mylist2:
        if key not in mydic:
            mydic[key] = 1
        else:
            mydic[key] = mydic[key] + 1
    
  
    for key in mydic:
        val = mydic[key]

        if val not in reverse_dic:
            reverse_dic[val] = [key]
        else:
            reverse_dic[val].append(key)

    f = sorted(reverse_dic)[::-1]
    for n in range(20):
        print(reverse_dic[f[n]])

