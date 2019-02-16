# Task1A_1
def unique_words(book):
    f = open(book)
    mylist1 = []
    mylist2 = []
    mydic = {}
    import string

    for line in f:
        line1 = line.strip().lower()
        for punc in string.punctuation:
            line1 = line1.replace(punc,' ')
        for word in line1.split():
            mylist1.append(word)
    for key in mylist1:
        if key not in mydic:
            mydic[key] = 1
        else:
            mydic[key] += 1
    for k in mydic:
        mylist2.append(k)
    print(mylist2)
    return mylist2


# unique_words('Book1.txt')

# Task1A_2
def count_the_article(file):
    f = open(file)
    mylist = list()
    count = 0
    import string

    for line in f:
        mylist.append(line)

    for word in mylist:
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        for punc in string.punctuation:
            word = word.replace(punc, ' ')
        count += len(word.split(' '))
    print(count)


# Task1A_3
def sorted_words(book):
    f = open(book)
    mylist = []
    d = dict()
    for line in f:
        line = line.strip().lower()
        import string
        for punc in string.punctuation:
            line = line.replace(punc,' ')
        for word in line.split():
            mylist.append(word)
    for key in mylist:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    list2 = sorted(d)
    print(list2[::-1])

# sorted_words('Book1.txt')


# Task1A_4
def character_word_count(book):
    f = open(book)
    d = dict()
    for line in f:
        line = line.strip().lower()
        import string
        for punc in string.punctuation:
            line = line.replace(punc,' ')
        for word in line.split():
            if word not in d:
                d[word] = len(word)
    print(d)
    return d



# Task1A_5
def start_with_vow(book):
    f = open(book)
    list1 = ['a','e','i','o','u']   #all is lower letter means that I need transfer words in the book in lower letter to match
    list2 = []
    list3 = []
    count = 0
    for line in f:
        line = line.strip().lower()
        import string
        for punc in string.punctuation:
            line = line.replace(punc,' ')
        for word in line.split():
            list2.append(word)
    for k in list2:
        if k[0] in list1:
            count += 1
            list3.append(k)
    print(list3)         # check the list  whether just includ words start from 'a','e','i','o','u'
    print(count)
    return count


start_with_vow('Book1.txt')

