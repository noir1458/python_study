
def python_study():
    a = "Hello"
    print(a.startswith("He")) #원본 문자열이 입력한 문자열로 시작되는지> True

    print(a.endswith("lo")) #원본 문자열이 입력한 문자열로 끝나는지> True

    print(a.find("k")) #매개변수로 입력한 문자열이 존재하는 위치 앞에서부터 찾기> -1(없음)
    print(a.find("l")) # 지정 문자열 처음 위치(l이 2개 있는데 그중 앞에것) > 2
    print(a.rfind("l")) # 지정 문자열 끝 위치> 3

    print(a.count("l")) #입력한 문자열 등장횟수 세기 > 2

    
    b = "    Test    "
    print(b.lstrip())
    print(b.rstrip())
    print(b.strip()) #공백제거

    c="abb"
    print(c.isalpha()) #알파벳으로만 이루어져있는지 > T
    print(c.isnumeric()) #수로만 이루어져 있는지 > F
    print(c.isalnum()) #알파벳과 수로만 이루어져 있는지 > T
    
    d = "Hello, world"
    e = d.replace("world","korea")
    print(d,e,sep=" // ")

    
    f = "Apple, Orange, Kiwi"
    g = f.split(",")
    print(g, type(g), sep=" // ")

    h = f.upper()
    print(h)
    i = f.lower()
    print(i)


    a1 = 'my name is {0}. I am {1} years old.'.format("abc",33)
    print(a1)
    b1 = 'my name is {0}. I am {1} years old.'
    print(b1.format("3232",322))
    c1 = 'my name is {name}. I am {age} years old.'.format(name='gg',age=242)
    print(c1)







    return None

def main():
    python_study()
    return None

if(__name__=="__main__"):
    main()