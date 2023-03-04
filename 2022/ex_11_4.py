# file writing
def main():
    # fpath, fname, wmode = "./", "test_copy1.txt", "w"
    fpath, fname, wmode = "./", "test_copy2.txt", "w"
    fhandle = open(fpath + fname, wmode)

    # a_string = "A sample string"
    a_string = "A sample string\n"
    for i in range(5):
        fhandle.write(str(i) + ":" + a_string)
    # 파일쓰기는 문자열밖에 저장이 안됨.
    fhandle.close()

    '''
    # a list of strings
    a_line_of_strings = [a_string+"1\n",a_string+"2\n",a_string+"3\n"]
    fhandle = open(fpath+fname, wmode)
    fhandle.writelines(a_line_of_strings)
    fhandle.close()
    '''
    return None

if __name__=="__main__":
    main()