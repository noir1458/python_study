
def python_Study():
    a = [1, 2, 3]
    a.append(4) # 끝에 새 요소 추가
    print(a)
    a.extend([4,5,6]) # 다른 리스트를 이어붙임 +와 같은기능
    print(a)

    a.insert(0,99) # 0위치에 99삽입
    print(a)
    a.insert(3,99)
    print(a)

    a.remove(99) # 매개변수로 입력한 데이터를 리스트에서 찾아 발견한 첫번째 요소를 제거
    print(a)

    print(a.pop()) # 리스트의 마지막 요소를 뽑아냄
    print(a)

    print(a.pop(2)) #2번 자리를 뽑아냄 0,1,2...
    print(a)

    print(a.index(3))
    
    #print(a.index(7))

    print(a.count(4))

    a1 = [3,4,5,1,2]
    a1.sort()
    print(a1)

    a1.sort(reverse = True) # 이름을 명시하는 매개변수, 키워드 매개변수 라고 함
    print(a1)

    b = [1,7,4,3]
    print(b)
    b.reverse() #순서를 뒤집음(반환값은 none)
    print(b)


    return None

def main():
    python_Study()
    return None

if(__name__=="__main__"):
    main()