#1 class naming
class _Rectangle(): # _ => user defined, (): later
    # class variable
    # 1. class
    color__ = "white"     # background color
    border__ = 1          # border line width
    # 2. instance
    # member methods
    # default constructors - 클래스가 오브젝트를 만들때 constructors를 먼저 부른다
    def __new__(cls, *args, **kwargs): # class variable 초기화, 이름없는 (this) 객체 공간 확보
        this = super(_Rectangle, cls).__new__(cls) # python에 메모리 확보 요청하는것
        return this
    
    def __init__(self, w = None, h = None): # member variable 초기화, 생성, h, w, self 순서로 들어감(맵핑됨), self는 관례적으로 사용 다른문자 ok
        # self - new에서 받은 this를 가리킴
        self.width_ = w # instance variables, 클래스 변수와 구분되도록 꼭 표시
        self.height_ = h
    '''    
    def __init__(self) #이렇게 하지말기 오류발생, w = None 이렇게 기본값 주기
            self.width_ = None
            self.height_ = None'''
    # area
    def _area(self):
        return self.width_*self.height_

    # print width & height
    def _print(self):
        print("width =",self.width_, "and height =",self.height_)
        return None



def main():
    rect1 = _Rectangle(4, 3) # 4cm * 3cm rectangle # self가 숨어있다...(에러메세지로 확인가능), class 메소드에도 숨어있음.
    rect2 = _Rectangle(1, 6) # 1 * 6. 
    rect3 = _Rectangle()
    #print(" ==> 4", rect1)
    #print(" ==> 5", rect2)
    rect1._print()
    rect2._print()
    rect3._print()
    print("rect1 area is = ", rect1._area())
    print(rect2._area())

    return None

if __name__ == "__main__":
    main()