

def build_range_dict(input_string):
    range_dict = {}
    #yourcode
    #문자열 분리하여 리스트에 담기
    split_string = input_string.split()
    #print(split_string)

    #tmp_dict에 2개 단위로 저장, 이미 중복된 키값이 있으면 기존 value값 리스트에 더해서 넣는다
    tmp_dict = {}
    for k in range(0,len(split_string),2):
        if split_string[k] in tmp_dict.keys():
            in_value = tmp_dict.get(split_string[k])
            add_value = [int(split_string[k+1])]

            tmp_dict[split_string[k]] = in_value + add_value
        else:
            tmp_dict[split_string[k]] = [int(split_string[k+1])]

    #print(tmp_dict)

    for k,v in tmp_dict.items():
        min_num1 = v[0]
        max_num1 = v[0]
        for num in v:
            if num<min_num1:
                min_num1 = num
                    
            if num>max_num1:
                max_num1 = num
                    

        num_list = [min_num1, max_num1]
        num_list.sort()   #튜플 저장할때 저장되는 순서가 불규칙적이라, 리스트에 넣고 정렬하고 튜플로 바꾼다
        num_tuple = tuple(num_list)

        range_dict[k] = num_tuple
        #print(k, max_num1, min_num1, num_tuple)

    return range_dict



def main():
    #input_string = ""
    input_string = "computer 2 keyboard 12 mouse 7 pen 11 mouse 19 computer 5 mouse 5 postit 2 ipad 1 keyboard 10"
    solution = build_range_dict(input_string)
    print(solution)
    return None

if __name__ == "__main__":
    main()