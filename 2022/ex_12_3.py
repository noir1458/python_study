class _A4Paper():
    width__ = 210
    height__ = 297

    def __new__(cls,*args,**kwargs):
        this = super(_A4Paper,cls).__new__(cls)
        return this

    def __init__(self, m, b):
        self.manufacture_ = m
        self.background_color_ = b

def main():
    paper1 = _A4Paper("miilk","white")
    print(paper1)

if __name__ == "__main__":
    main()