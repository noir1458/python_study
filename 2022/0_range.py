nums = (23, -1, 15, 9, 7, 890, 10, 99, 777)
tuple_range = range(0,len(nums),3)
for idx in tuple_range:
    print(nums[idx])
print(type(tuple_range))
print(tuple_range)

'''
# range(end)
range(0)
0부터 0전까지 => empty list 리턴

# range(start, end)
start부터 end전까지 리턴

# range(start, end, step)
start로 시작되는 숫자부터 리턴
end가 포함되지 않는 숫자까지(전까지) 리턴
연속적인 숫자들중 step의 간격에 해당하는 숫자들만 리턴

type 출력시 class 'range' 출력된다
숫자범위의 list나 tuple 쉽게 만들수 있다.
for문에도 활용
'''
