#Function for unique_words
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


unique_words('Book1.txt')


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




def sorted_words(book):
	sorted_list=[]
        for line in book:
                for word in line.split():
                        if word not in sorted_list:
                                sorted_list.append(word)
				sorted(sorted_list)
	print (sorted_list)

def character_word_count(book):
	my_dict={}
	list1=[]
	book_copy=book
	for line in book:
                for word in line.split():
                        if word not in list1:
				list1.append(word)
	for list_words in list1:
		count=0
		for lines in book_copy:
                	for word1 in lines.split():
				if word1==list_words:
					count+=1
		my_dict[list_words]=count
	print (my_dict)

def starts_with_vow(book):
	count =0
        for line in book:
                for word in line.split():
                        if word[0] in ("a","e","i","o","u"):
				count=count+1
	return (count)



print(starts_with_vow(book_open))

