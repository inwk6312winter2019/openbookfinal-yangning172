def unique_words(file):
    mylist = []
    
    f = open(file)
    import string
    for line in f:
       pass



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

