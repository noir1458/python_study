def testTuple():
    str_list=["p","i","t","h",0,"n"]
    print(str_list[1]) # i
    print(str_list[4:]) # [0,'n']
    str_list[1]="y" # list는 mutable
    print(str_list) # ['p','y','t','h',0,'n'] list의 내용이 바뀜

    del str_list[0] # 메모리에서 지워버린다, string에서는 이렇게 못함
    print(str_list)
    return None

def main():
    testTuple()
    return None

if (__name__=="__main__"):
    main()

    '''
    string의 값은 item assignment를 지원하지 않는다.
    list는 가능하다
    두 개체의 차이는?

    Ownership : 프로그램이 변수에 접근할수 있는 범위
    데이터 구조나 타입은 mutable(변경가능) 하거나 immutable(변경불가능)하다

    mutable : list, dictionary, set ,and user-defined classes
    immutable : int, float, decimal, bool, string, tuple ,and range
    python이 immutable한 개체는 내용변경을 허용하지 않음

    list : Fixed-size Writeable
    tuple : Fixed-size Read-only(immutable)
    tuple은
    1. 메모리 소모가 적다
    2. 더 빠른 반복을 지원함
    3. 에러발생 가능성 감소
    '''