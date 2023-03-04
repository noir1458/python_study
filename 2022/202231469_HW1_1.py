"""
Home assignment #1
Due: 22/09/2022, at 11:59pm
"""


def build_a_list_of_tuples():
    list_of_tuple = []
    #list_of_tuple = [(1,2),(3,4,5),(6,7,-8,-9),(-1000,1),(2,9,10)]

    # your code
    # 정수 tuple 로 구성된 list input()사용 
    # 4개 이상의 tuple , 저장값은 integer type, 문자나 특수문자는 모두 7로 대체하여
    


    print("<4개이상의 정수 tuple로 구성된 list를 입력하세요, 문자나 특수 문자 입력시 7이 저장됩니다>")
    while True:
        list_len = int(input("list 안의 요소(tuple) 개수를 입력하세요 (4 이상) : "))
        if (list_len >= 4):
            break
        print("list 안에는 4개 이상의 정수 tuple로 구성되어야 합니다")
    
    
    for tuple_num in range(list_len):
        while True:
            print(tuple_num + 1, " 번째 tuple 안에 들어갈 숫자의 개수를 입력하세요.", end = " > ")
            tuple_len_str = input()
            if(tuple_len_str.isnumeric() == True):
                tuple_len = int(tuple_len_str)
                break
            else:
                print("숫자만 입력하세요")
            

        tmp_tuplelist = []
        for k in range(tuple_len):
            print(tuple_num + 1, " 번째 tuple의", k + 1, " 번째 숫자(정수)를 입력하세요", end = " >> ")
            in_tuple = input()

            #받은게 숫자가 아니면 바꿔줘야 한다, input 받은것은 str이므로
            #음수인지 아닌지 판단하여 앞에 -가 있다면 분리한다
            #in_tuple_tmp 는 input 받은 수에서 부호를 뺀것
            if (in_tuple == "-"):
                #정수 자리에 마이너스만 입력한경우 특수문자 하나로 취급해야되서 그대로 in_tuple_tmp 변수에 넣는다
                in_tuple_tmp = in_tuple
                input_minus = False
            elif (in_tuple[0] == "-"):
                #앞자리에 마이너스가 있는 경우는 분리한다
                in_tuple_tmp = in_tuple[1:]
                input_minus = True
            else:
                #앞자리에 마이너스가 없는경우 그냥 in_tuple_tmp로
                in_tuple_tmp = in_tuple
                input_minus = False

            tmp_str = ""

            for input_idx in range(len(in_tuple_tmp)):

                if (in_tuple_tmp[input_idx].isdigit() == False):
                    #숫자가 아니면 7로
                    tmp_str = tmp_str + "7"
                else:
                    #숫자면 그대로
                    tmp_str = tmp_str + in_tuple_tmp[input_idx]
            

            if (input_minus == True):
                tmp_str = "-" + tmp_str


            
            tmp_tuplelist = tmp_tuplelist + [int(tmp_str)]
            
            print("이전에 입력한 튜플 > ", list_of_tuple)
            print("현재 입력중인 튜플 > ", tmp_tuplelist)

        list_of_tuple.append(tuple(tmp_tuplelist))
        
        
    

    
    

    return list_of_tuple

def form_product_list(list_of_tuple):
    product_list = []
    # your code
    # 각 tuple 처음과 마지막값 곱하여 계산된 새 정수로 구성되는 list생성
    # for나 while-loop는 한번 사용 가능
    for Input_tuple in list_of_tuple:
        tmp_a = Input_tuple[0]*Input_tuple[-1]
        product_list = product_list + [tmp_a]

    print(product_list)

    return product_list

def sort_product_list(product_list):
    sorted_product_list = []
    # your code
    # 생성된 list를 정렬하여 저장된 tuple을 출력하기 위해 함수 정의
    #출력은 tuple type, for나 while문 사용불가
    product_list.sort()
    sorted_product_list = product_list
    #sorted_product_list = product_list.sort()  ????
    return sorted_product_list

def main():
    list_of_tuple = build_a_list_of_tuples()
    print("[Input]")
    print(list_of_tuple) # input한 튜플 출력
    product_list = form_product_list(list_of_tuple) # #2로 list새로 생성
    sorted_product_tuple = sort_product_list(product_list) # #3으로 list정렬하여 출력
    print("[Output]")
    print(sorted_product_tuple)

    return None

if(__name__ == "__main__"):
    main()


