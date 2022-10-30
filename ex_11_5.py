
def buildWordCountDict():
    word_count_dict = {}
    fpath, fname, fmode = "./", "random.txt", "r"
    fhandle = open(fpath+fname, fmode)

    #your code
    wordlist = []
    while(True):
        line = fhandle.readline()
        wordlist = wordlist + line.split(" ")
        if 0==len(line):
            break

    for word in wordlist:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
        '''
        if word in word_count_dict:
            word_count_dict[word] = word_count_dict.get(word) + 1
            # word_count_dict.update({word : word_count_dict[word] + 1})
        else:
            word_count_dict[word] = 1
            # word_count_dict.update({word : 1})'''
    
    fhandle.close()
    return word_count_dict

def main():
    word_count_dict = buildWordCountDict()
    print(word_count_dict)
    return None

if __name__=="__main__":
    main()