# Comparison between homogeneous tuples
t1 = (1,2,3)
t2 = (1,2,4)

print(t1!=t2) #true
print(t1<t2) #true

t3 = (1,2,3,4)
t4 = (1,2,3,4,5,5)
print(t3>t4) #false
print(t3==t4) #false

# Built-in functions
print(min(t1),max(t1))
print(sum(t1))
print(len(t1))

# Tuple Methods
# tuple의 모든 요소는 변경불가 (move, delete, change)
# .sort(), .append(), .reverse() 사용불가
t2 = tuple(t4)
print(t2)
#print(dir(tuple)) #dir 내장함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드를 가지고 있는지 나열해줍니다.
print("t4 안에 5의 개수는 : ", t4.count(5)) # 2
print("t4 안에 4의 index는 : ", t4.index(4)) # 3
# find()는 리스트, 튜플, 딕셔너리 자료형에서 사용불가. 문자열에서만 가능

# sorted() built-in function 사용가능. 정렬한것을 반환한다(리스트로...)
t6 = (1,5,3,2)
t7 = sorted(t6) #sorted(object, key, reverse=False)
print(t7)
t8 = (1,5,3,2,1)
print(t8.pop())
print(t8.reverse())