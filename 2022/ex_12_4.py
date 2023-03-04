class _Circle():
    # class variables pi__, bgcolor__, border__
    border__ = 1
    bgcolor__ = "white"
    pi__ = 3.141592

    #instance variables radius_
    # __new__ & __init__
    # _area & _print
    def __new__(cls,*args,**kwargs):
        this = super(_Circle,cls).__new__(cls)
        return this
    
    def __init__(self, r = None):
        self.radius_ = r


    def _area(self):
        # return self.radius_*self.radius_*self.pi__ ??
        return self.radius_*self.radius_*_Circle.pi__
    
    def _print(self):
        print("radius =", self.radius_)
        return None

def main():
    c1 = _Circle(3)
    c1._print()
    print(c1._area())

if __name__ == "__main__":
    main()