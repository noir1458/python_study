
import sys

def python_study():
    print("수를 입력하세요 : ")
    a = int(input())

    '''
    if a==0:
        print("0은 나눗셈에 이용할수 없습니다")
    else:
        print('3 /',a,'=', 3/a)'''
    
    if a == 0: #if not a와 동일한 코드
        # a가 0이 아닌 어떤 숫자라면 not a는 false가 된다
        # a가 0이라면 not a는 true 가 된다
        print(not a)
        print('0은 나눗셈에 이용할수 없습니다')
        sys.exit(0)
    
    print('3 /', a ,'=', 3/a)

    return None

def main():
    python_study()
    return None

if(__name__=="__main__"):
    main()