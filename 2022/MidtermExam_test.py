def invert_dictt(file_dict):
    inverted_dict = {}
    split_dict = {}
    for k,v in file_dict.items():
        split_dict[k] = v.split(" ")
    
    for k,v in split_dict.items():
        for word in v:
            value_dict = inverted_dict.get(word,{})
            value_dict[k] = value_dict.get(k,0) + 1
            inverted_dict[word] = value_dict
    return inverted_dict

def main():
    file_dict = {
        "f1":"i like Python",
        "f2":"Python is my life",
        "f3":"Python Python Python",
        "f4":"Python is my Python"
    }
    print(invert_dictt(file_dict))
    return None

if __name__ == "__main__":
    main()