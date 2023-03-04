# Complex class
class _Complex():
    # class variables & instance variables
    __i_symbol = 'i'
    # constructors
    def __new__(cls,*args):
        obj = super(_Complex,cls).__new__(cls)
        return obj
    def __init__(self, r=0, i=0):
        self.real_ = r # real part
        self.imag_ = i # imaginary part
        return None

    # methods
    def _add(self, rhs):
        # your code
        r = self.real_ + rhs.real_
        i = self.imag_ + rhs.imag_
        return _Complex(r, i)

    # magic functions
    def __add__(self, rhs):
        #same as add
        r = self.real_ + rhs.real_
        i = self.imag_ + rhs.imag_
        return _Complex(r, i)

    def __str__(self):
        cpx = str(self.real_) +"+" + str(self.imag_)+_Complex.__i_symbol
        return cpx

def main():
    c1 = _Complex(1,2) # c1 = 1+2i
    c2 = _Complex(3,4) # c2 = 3+4i
    c3 = c1 + c2 # c3 = 4+6i
    print(c3)
    return None

if __name__ == "__main__":
    main()