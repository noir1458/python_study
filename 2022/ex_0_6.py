def python_study():
    
    for i in range(1,6):
        for j in range(i):
            print("*", end="")
        print()

    return None

def main():
    python_study()
    return None

if(__name__=="__main__"):
    main()