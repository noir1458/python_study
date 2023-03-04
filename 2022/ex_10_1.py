
def testDict():
    dict1 = {
        # key : values
        "Sicario" : [2015],
        "Arrival" : "2016",
        "Blade Runner 2049" : 2017,
        "Dune" : 2021
    }
    dict2 = {
        2021 : ["Dune", "Gray man", "starwars"],
        2019 : ("Sicario","Arrival")
    }
    print("dict1:items =>", dict1.items())
    list1 = dict1.items()
    # print("list1[1]", list1[1]) #실제 리스트로 받는게 아니라서 슬라이싱 불가, 실행 창에서도 dict_items()타입으로 받는것 확인가능
    print("list1[1]", type(list1)) #실제 리스트롤 받아서 막 바꿔버리면 dictonary의 의미가 없어서...

    print("dict2:keys =>", dict2.keys())
    print("dict1:values =>", dict1.values())
    print("Values = ", dict2.get(2021)) #value를 리스트로 받아온다, 조작가능. key는 조작불가

    return None

def main():
    testDict()
    return None

if(__name__ == "__main__"):
    main()

    '''
    단일 변수에 많은 값을 갖도록 허용
    정렬되지 않은 collection이다. each value with its own label
    영어사전을 찾는것과 같다. commend > c부터 하나씩 찾아들어간다.> 마지막에 찾으면 뜻 1,2,3
    정수 인덱스 대신 키워드를 사용하여 찾음

    java.util.HashMap in java
    std::map in C++
    std::collections::HashMap in Rust

    The dictionary data type models a super fast searchable collection of (key-values) items
    키값은 중복될수 없다(집합과 똑같음)
    Keys must be immutable and hashable
    '''