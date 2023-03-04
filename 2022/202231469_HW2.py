'''
Home assignment #2
Due : 10/13/2022, at 11:59 pm
'''

def get_text(min_length): #임의의 문자열 입력받기
    #your code
    #input_text 는 string
    #특수문자 제외
    #문자열 길이는 공백포함 50자 이상
    input_text = "is A is big is thing is is is A Hmmm is I have is no idea is" #테스트용 문자열
    
    '''
    while(True):
        input_text_tmp = input("문자열을 입력하세요, 문자열 길이는 공백 포함 50자 이상입니다, 특수문자 제외합니다 : ")
        if(len(input_text_tmp)>=50):
            break
        else:
            print("문자열 길이는 공백 포함 50자 이상이며, 특수문자를 제외합니다")

    input_text = ""
    for k in input_text_tmp:
        if (k == " " or k.isalnum() == True): #특수문자를 제외합니다. 공백은 포함시켜야 함
            input_text = input_text + k
    '''
    return input_text


def search_backward(keyword, my_text): #keyword에 단어를 입력받아 이 단어의 모든 앞단어를 찾는 다음 함수를 정의하고 구현
    #your code
    #한개 이상의 dictionary type 변수 사용
    #입력 parameter인 keyword는 기준이 되는 string type의 변수이며, text는 탐색할 string type의 변수로 get_text() 로 만들어진 길이50이상 문자열
    #모든 앞단어를 찾아 tuple 변수 predecessors (alphabet 오름차순 정렬)에 저장
    split_text = my_text.split()

    #dictionary에 나눈 문자열을 넣는다 {list_index값: 문자열}
    split_dict = {}
    for tmp_idx in range(len(split_text)):
        split_dict[tmp_idx] = split_text[tmp_idx]

    #keyword가 몇번째인지 찾아서 저장한다
    keyword_idx = []
    for key,value in split_dict.items():
        if value == keyword:
            keyword_idx = keyword_idx + [key]

    #predecessors 찾기
    newpredecessors = []
    for tmp in keyword_idx:
        if tmp == 0: #맨 앞 글자일경우 그 앞글자는 공백
            newpredecessors = newpredecessors + [" "]
        else:
            newpredecessors = newpredecessors + [split_dict[tmp - 1]]
    
    #중복제거
    predecessors_norept = []
    for n in newpredecessors:
        if n not in predecessors_norept:
            predecessors_norept = predecessors_norept + [n]

    #튜플에 넣고 오름차순 정렬한다
    predecessors_norept.sort()
    predecessors = tuple(predecessors_norept)

    return predecessors


def search_forward(keyword, my_text):
    #your code
    #모든 뒷단어를 찾아 tuple 변수 successors (alphabet 내림차순 정렬)에 저장
    split_text = my_text.split()

    #dictionary에 나눈 문자열을 넣는다 {list_index값: 문자열}
    split_dict = {}
    for tmp_idx in range(len(split_text)):
        split_dict[tmp_idx] = split_text[tmp_idx]

    #keyword가 몇번째인지 찾아서 저장한다
    keyword_idx = []
    for key,value in split_dict.items():
        if value == keyword:
            keyword_idx = keyword_idx + [key]
    
    #successors 찾기
    newsuccessors = []
    for tmp in keyword_idx:
        if tmp == len(split_text)-1: #맨 뒷글자일 경우 그 뒷글자는 공백
            newsuccessors = newsuccessors + [" "]
        else:
            newsuccessors = newsuccessors + [split_dict[tmp + 1]]
    
    #중복제거
    successors_norept = []
    for n in newsuccessors:
        if n not in successors_norept:
            successors_norept = successors_norept + [n]

    #튜플에 넣고 내림차순 정렬한다
    successors_norept.sort(reverse = True)
    successors = tuple(successors_norept)
    
    return successors

def main():
    minimum_length = 50
    my_text = get_text(minimum_length)
    print("my text = ", my_text)
    pwords = [] #predecessors
    swords = [] #successors
    keyword = input("Enter a target word : ")
    pwords = search_backward(keyword, my_text)
    print("[All predecessors of ", keyword, "]: ", pwords, sep="")
    keyword = input("Enter a target word: ")
    swords = search_forward(keyword, my_text)
    print("[All successors of ", keyword, "]: ", swords, sep="")

    return None

if(__name__ == "__main__"):
    main()
