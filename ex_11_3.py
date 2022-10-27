#file open and read

def main():
    fpath = "C:/test/python/"
    fname = "Byron.txt"
    fmode = "r"
    # create a handle
    # fpath + fname = C:/test/python/Byron.txt
    fhandle = open(fpath + fname, fmode)

    while(True):
        output = fhandle.readline()
        print("Now I am at...",fhandle.tell())
        if(output==""):
            # move the file ptr to the head (offset,from) where from 0,1,2 &offset
            fhandle.seek(0, 0) 
            
            break
        print(output)

    output2 = fhandle.read()
    print("Output2 = ",output2)


    # close
    fhandle.close()
    return None

if __name__=="__main__":
    main()