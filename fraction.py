# Fraction class
class _Fraction():
    # 1. class variables
    # 2. instance variables
        # den(분모), num(분자)
    # 3. constructors
    
    def __new__(cls,*args,**kwargs):
        this = super(_Fraction,cls).__new__(cls)
        return this
    def __init__(self,n = 1,d = 1): # 분모는 0일수 없다는데 유의
        self.den_ = d
        self.num_ = n
        return None

    # print a fraction
    def _print(self):
        print(str(self.num_)+"/"+str(self.den_))
        return None

    def _get_den(self,d):
        print("den =", self.den_)
        return None
    def _get_num(self,n):
        print("num =",self.num_)
        return None

    # addition
    def _add(self,rhs):
        den = self.den_ * rhs.den_
        num = self.num_ * rhs.den_ + rhs.num_ * self.den_
        return _Fraction(num,den)
    
    # def subtract
    def _subtract(self,rhs):
        den = self.den_ * rhs.den_
        num = self.num_ * rhs.den_ - rhs.num_ * self.den_
        return _Fraction(num,den)

    # def multiply
    def _multiply(self, rhs):
        den = self.den_*rhs.den_
        num = self.num_*rhs.num_
        return _Fraction(num,den)

    # def div
    def _div(self, rhs):
        den = self.den_*rhs.num_
        num = self.num_*rhs.den_ 
        if rhs.num_ == 0:
            print('cant divde by 0')
        return _Fraction(num,den)

    ### magic function
    def __add__(self, rhs):
        den = self.den_ * rhs.den_
        num = self.num_ * rhs.den_ + rhs.num_ * self.den_
        return _Fraction(num,den)
    
    def __mul__(self, rhs):
        den = self.den_*rhs.den_
        num = self.num_*rhs.num_
        return _Fraction(num,den)
    
    def __str__(self):
        fraction = str(self.num_) + "/" + str(self.den_)
        return fraction


def main():
    f1 = _Fraction(1,2) # 1/2
    f2 = _Fraction(3,4) # f2 = 3/4
    print("f1 =", f1)
    ####
    f3 = f1 + f2
    f3._print()
    f4 = f1 * f2
    f4._print()
    return None

if __name__=="__main__":
    main()