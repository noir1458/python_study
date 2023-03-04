




def encode(k, inputText):
    
    # a tuple
    lowercase = (" ","a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z")
    # a dictionary
    encodeBook = {0:"#",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",
                14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
    encodedText = ""

    # finding index
    # lowercase.index("")
    '''
    for tmp_str in inputText:
        tmp_idx = lowercase.index(tmp_str)
        if tmp_idx == 0:
            encode_idx = 0
        else:
            encode_idx = (tmp_idx + k) % 26

        encode_str = encodeBook[encode_idx]
        encodedText = encodedText + encode_str'''

    for idx in range(len(inputText)):
        if (inputText[idx]==" "):
            encodedText = encodedText + "#"
        else:
            location = lowercase.index(inputText[idx])
            image_location = (location + k) % 26
            encodedText = encodedText + encodeBook[image_location]

    return encodedText

def decode(k, encodedText):

    # a tuple
    lowercase = (" ","a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z")
    # a dictionary
    encodeBook = {0:"#",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",
                14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
    decodeBook = { v:k for k,v in encodeBook.items() }


    decoded_text = ""

    for idx in range(len(encodedText)):
        if(encodedText[idx] == "#"):
            decoded_text = decoded_text + " "
        else:
            location2 = decodeBook[encodedText[idx]]
            decode_location = (location2 - k) % 26
            decoded_text = decoded_text + lowercase[decode_location]


    return decoded_text


def main():
    input_text = input("Enter Your text : ")
    k = int(input("input k : "))
    #encoding: s=>t
    encoded_text = encode(k,input_text)
    print(encoded_text)
    #decoding: t=>s
    decoded_text = decode(k, encoded_text)
    #check if s=>s'
    print(decoded_text)
    if(decoded_text != input_text):
        print("x")
    else:
        print("good")
        
    return None


if(__name__ == "__main__"):
    main()