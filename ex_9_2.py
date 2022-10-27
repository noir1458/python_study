
def TestTuple():
    idx = 0
    nums= (23,-1,15,9,0,890,10,19,777)    #tuple
    nums_list= [23,-1,15,9,0,890,10,19,777]    #a list
    #print all elts
    idx = 0
    while(idx < len(nums)):
        print(nums[idx])
        idx = idx + 1


    #update the tulpe & the list
    #nums[1] = -2 #work ? => immutable
    '''
    tuple은 immutable
    nums[1] = -2
    이런 업데이트는 작동하지 않는다
    '''
    nums_list[1] = -2 #work => mutable
    print(nums_list)

    return None

# main function
def main():
    TestTuple()
    return None

# main entrance
if(__name__ == "__main__"):
    main()

