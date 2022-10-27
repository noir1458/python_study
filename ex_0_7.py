def python_study():
    
    for i in range(10):
        if i%2==1:
            continue #홀수일때 다음 반복으로 건너뛴다
        print(i)


    k = 0
    while True:
        print(k)
        k = k + 1
        if k == 1000:
            print('k가 {0}이 되었습니다. 반복문을 중단합니다'.format(k))
            break    

    return None

def main():
    python_study()
    return None

if(__name__=="__main__"):
    main()