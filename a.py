
def acc(word,key):
    lowercase = (" ","a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z")
    tmpnum = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'
    , 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}           
    tmp2 = {}

    for k,v in tmpnum.items():
        key2 = k + key
        if key2 > 26:
            key2 = key2 - 26
        tmp2.update({k:tmpnum[key2]})

    tmpnum2 = {v:k for k,v in tmpnum.items()}

    answer = ''
    for tmpword in word:
        kk = tmpnum2[tmpword]
        answer += tmp2[kk]

    return answer

def main():
    word = 'secret'
    key = 6
    print(acc(word,key))
    return None

if __name__ == "__main__":
    main()