def doDict():
    dict1 = {"a" : 1, "b" : 253, "c" : 356, "d" : 407} # 집합기호 => 순서는 상관x
    dict2 = dict([("e", 654), ("f", 906)]) # tuple쌍을 list로 감싼 dict 형식도 가능하다

    #check if a key in a dictonary
    a_key = "a" in dict1
    print(a_key) #true
    a_value = 1 in dict1
    print(a_value) #안됨 false
    # 사전에 없는 키값을 찾으면 에러가 나온다 dict1["aaa"]=> keyerror


    # add a element to dict1
    # dict2 <= ("d" : 0001) error 키값은 중복될수 없다
    print("Before: ", dict1)
    dict1["g"] = 1510 # update
    print("After: ", dict1)
    dict1["g"] = 1519 # 이건 update
    print("AAfter: ", dict1)
    # delete : dict2 = dict([("e", 654), ("f", 906)]) => dict([("e", 654)])
    del dict1["g"] # 명령어라고 생각하기
    print("AAAfter: ", dict1)
    del dict2 # delete


    #list up
    #for [k,v] in dict1.items(): 이것도 가능하지만 key, value 값 날아갈수 있음
    # unpacking of all dictionary items into
    # a pair of key and value
    for k,v in dict1.items():
        print("(key= ", k,"Value= ", v, ")")


    
    dict1 = {"a" : 1, "b" : 253, "c" : 356, "d" : 407}
    dict1.update({"aa":11})
    print(dict1) 
    #>> {'a': 1, 'b': 253, 'c': 356, 'd': 407, 'aa': 11}


    

    return None

def main():
    doDict()
    return None

if (__name__ == "__main__"):
    main()

