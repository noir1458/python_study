# test

def TestTupleOp():
    evenT = (0, 2, 4, 6, 8)
    oddT = (1, 3, 5, 7, 9)
    # concatenate two tuples
    T1 = evenT + oddT
    T2 = T1 * 2 # repitition
    print(T1)
    print(T2)
    print(T1[-1]) # negative index
    print(T1[3:6])
    print(evenT > T1) #comparison 
    print(len(T1))

    print(2 in evenT) # membership check: in and not in
    return None

# main function
def main():
    TestTupleOp()
    return None

# main entrance
if(__name__ == "__main__"):
    main()