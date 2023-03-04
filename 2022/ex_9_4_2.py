
def str_2_int(Input):
    Output = []
    # 1. read each tuple
    for each_tuple in Input:
    # 2. read the number (= m) of strings in the tuple
        no_of_strings = each_tuple[-1]

        tmp_string =""
    # 3. read each string as many as the number m
    # 4. Concatenate using +
    # 5. convert into an integer
    # and add the integer to a list using +, Output
        for idx in range(no_of_strings):
            tmp_string= tmp_string + each_tuple[idx]
        
        Out_int = int(tmp_string)
        Output = Output + [Out_int]

        #tmp_list[0] = int(tmp_string)
    return Output

def main():
    Input = [("1",1),("1","20",2),("1","20","300",3),("1","20","300","4000",4)]
    Output = str_2_int(Input)
    print(Output)
    #output = [1,120,120300,1203004000]
    return None

if(__name__ == "__main__"):
    main()