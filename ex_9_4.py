
def str_2_int(Input):
    Output = []

    # my job to do
    '''
    1. input 리스트의 각 성분을 가져와서
    2. 각 성분 튜플의 끝항 전까지의 string을 더한다
    input각 성분의 -1번째 항만큼 더함
    3. 그 값을 int로 바꾸고 리스트에 넣어서 output 시켜주면 된다
    '''
    
    list_idx = 0
    while(list_idx < len(Input)):
        k = ""
        #print(Input[list_idx])

        tuple_idx = 0
        while(tuple_idx < Input[list_idx][-1]):  # input 각 성분의 -1 항의 숫자만큼 더한다
            k = k + Input[list_idx][tuple_idx]
            #print(Input[list_idx][tuple_idx])
            tuple_idx = tuple_idx + 1
             
        Output.append(int(k))
        list_idx = list_idx + 1
    
    print(Output)
    return Output

def main():
    Input = [("1",1),("1","20",2),("1","20","300",3),("1","20","300","4000",4)]
    
    str_2_int(Input)
    #output = [1,120,120300,1203004000]
    return None

if(__name__ == "__main__"):
    main()