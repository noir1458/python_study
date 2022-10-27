def accumulator():
    dict_1 = { 'a':1, 'b':2, 'c':3}
    print(dict_1.get('d',"없는 값입니다"))
    # dict.get('찾는value의 키값', 'value값이 없을경우 이 값이 value에 들어감')

def main():
    accumulator()
    return None

if __name__ == "__main__":
    main()