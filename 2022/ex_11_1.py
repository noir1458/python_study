

def main():
    f_path = "C:/test/python/" # 현재 디렉토리 밑에있는 (./)
    f_name = "test.txt"
    f_mode = "r" # r : read , w : write
    fhandle = open(f_path + f_name, f_mode) #f_path + f_name 합치면 디렉토리 문자열이 된다
    # C:\test\python\test.txt
    print("Handle : ", fhandle)

if (__name__ == "__main__"):
    main()