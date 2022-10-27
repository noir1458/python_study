#file open and read

def main():
    fpath = "C:/test/python/"
    fname = "Byron.txt"
    fmode = "r"
    # create a handle
    # fpath + fname = C:/test/python/Byron.txt
    fhandle = open(fpath + fname, fmode)

    '''for a_line in fhandle: #for문은 알아서 다 읽어준다 read 필요 x
        print(a_line)'''
    list_of_words = [] #=["when","we","to"]
    while(True): #while statement + readline() => end of file check=>break
        a_line_of_strings = fhandle.readline()
        #print(output)

        split_string = a_line_of_strings.split(" ")
        list_of_words = list_of_words + split_string
        
        if a_line_of_strings=="":
            break
            
    print(list_of_words)

        
    #print("Handle = ", fhandle)

    '''
    output = fhandle.read(32) #문자단위
    # 읽고 나면 파일 포인터가 읽은 위치까지 간다
    print(output)
    output = fhandle.readline() #한줄
    print(output)'''

    fhandle.close()
    return None

if __name__=="__main__":
    main()