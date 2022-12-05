# Ellipse class
#
class _Ellipse():
    PI__ = 3.141592
    bg_color__ = "Yellow"
    def __new__(cls,*args,**kwargs):
        this = super(_Ellipse,cls).__new__(cls)
        return this
    def __init__(self, mj = None, mi = None):
        self.major_ = mj
        self.minor_ = mi
        return None

    def _get_minor(self):
        return self.minor_
    def _get_major(self):
        return self.major_
    def _set_minor(self, mi):
        self.minor_ = mi
        return None
    def _set_major(self, mj):
        self.major_ = mj
        return None
    def _area(self):
        return self.major_*self.minor_*_Ellipse.PI__
    def _print(self):
        print("major =",self.major_,"minor = ",self.minor_)
        return None

def main():
    ell1 = _Ellipse() 
    ell2 = _Ellipse(5, 3)
    print("Major of ell2 =", ell2._get_major())
    print("Area of ell2 =", ell2._area())
    ell2._set_minor(10)
    print("Area of ell2 =", ell2._area())
    ell2._print()
    
    return None

if __name__ == "__main__":
    main()