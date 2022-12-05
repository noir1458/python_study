class _SecretLetter():
    # class variable & instance variable
    e1__, e2__, e3__, e4__ = 5,7,2,11
    d1__, d2__, d3__, d4__ = 30,5,9,4
    alpha_dict__ = {0: '#', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 
7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
  25: 'Y', 26: 'Z', 27: 'a', 28: 'b', 29: 'c', 30: 'd', 31: 'e', 32: 'f', 33: 'g',
   34: 'h', 35: 'i', 36: 'j', 37: 'k', 38: 'l', 39: 'm', 40: 'n', 41: 'o', 42: 'p',
    43: 'q', 44: 'r', 45: 's', 46: 't', 47: 'u', 48: 'v', 49: 'w', 50: 'x', 51: 'y', 52: 'z'}
    # constructors
    def __new__(cls,*args):
        obj = super(_SecretLetter,cls).__new__(cls)
        return obj
    def __init__(self, name = 'tmp', mode = 'r', path = './', p=None):
        self.name_ = name
        self.mode_ = mode
        self.path_ = path
        self.p_ = p
        return None
    # method
    def _encoding(self):
        fpath = self.path_
        fname = self.name_
        fmode = self.mode_
        tmp = ''
        en_dict = _SecretLetter.alpha_dict__
        en_dict2 = {v:k for k,v in _SecretLetter.alpha_dict__.items()}
        fhandle = open(fpath+fname, fmode)
        while(True):
            line = fhandle.read(2) #문자 2개를 읽는다
            if len(line) == 0:
                break
            #각각의 공백은 #로 대체하여 작성한후 비밀 편지를 계산해낸다. 이부분 놓침.
            if line[0] == ' ':
                a1 = en_dict2['#']
            else:
                a1 = en_dict2[line[0]]
            if line[1] == ' ':
                a2 = en_dict2['#']
            else:
                a2 = en_dict2[line[1]]
            b1 = (_SecretLetter.e1__*a1 + _SecretLetter.e2__*a2)%53
            b2 = (_SecretLetter.e3__*a1 + _SecretLetter.e4__*a2)%53
            t1 = en_dict[b1]
            t2 = en_dict[b2]
            encode_str = t1 + t2
            tmp += encode_str
        #print(tmp)    
        return tmp

    def _decoding(self):
        fpath = self.path_
        fname = self.name_
        fmode = self.mode_
        tmp = ''
        en_dict = _SecretLetter.alpha_dict__
        en_dict2 = {v:k for k,v in _SecretLetter.alpha_dict__.items()}
        fhandle = open(fpath+fname, fmode)
        while(True):
            line = fhandle.read(2) #문자 2개를 읽는다
            if len(line) == 0:
                break
            a1 = en_dict2[line[0]]
            a2 = en_dict2[line[1]]
            b1 = (_SecretLetter.d1__*a1 + _SecretLetter.d2__*a2)%53
            b2 = (_SecretLetter.d3__*a1 + _SecretLetter.d4__*a2)%53
            t1 = en_dict[b1]
            if t1 == '#':
                t1 = ' '
            t2 = en_dict[b2]
            if t2 == '#':
                t2 = ' '
            decode_str = t1 + t2
            tmp += decode_str
        #print(tmp)    
        return tmp

def main():
    s1 = _SecretLetter('letter.txt','r','./')
    s2 = s1._decoding()
    print(s2)
    return None
if __name__=="__main__":
    main()