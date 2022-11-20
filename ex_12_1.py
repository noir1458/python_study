# Rectangle class
# class 정의(define)
class _Rectangle(): # 붕어빵틀
    # attributes -> member variables
    print("here")
    # methods -> member methods
    pass

# class의 instance를 instantiate

def main():
    # 붕어빵 instantiate
    rect1 = _Rectangle()
    rect2 = _Rectangle()
    print("rect1 : ", rect1)
    print("rect2 : ", rect2)

    return None 

if __name__ == "__main__":
    main()