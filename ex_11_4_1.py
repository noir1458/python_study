def extract_an_receipient():
    # line을 읽고
    fpath, fname, mode = "./", "email.txt", "r"
    fhandle = open(fpath+fname, mode)
    receiver = ""

    while(True):
        string_line = fhandle.readline()
        if string_line == "":
            # 0 == len(string_line) 가능
            # line이 끝?
            break
        if string_line.startswith("Reply-To"):
            #line 이 reply-to
            split_email = string_line.split(" ")
            print(split_email)
            # line 을 split
            break

    # receiver를 저장
    receiver = split_email[1][1:-2]
    # print(receiver)
    print("The receiver is ",receiver) # <, > removing


    fhandle.close()
    return None

def main():
    extract_an_receipient()

if __name__=="__main__":
    main()