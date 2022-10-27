# 슬라이싱(slicing) or 슬라이스(slice)
# 연속적인 객체들에(예: 리스트, 튜플, 문자열) 범위를 지정해 선택해서 객체들을 가져오는 방법 및 표기법

a = ('a', 'b', 'c', 'd', 'e')
#a = 'abcde'
# a[start:end:step]
# a[start:end ]
print(a[1:])
print(a[-1:])
print(a[-3:])
print(a[3:0:-1]) #값을 거꾸로 가져온다

# 원본이 list면 list, tuple이면 tuple, 문자열이면 문자열 (원본 타입을 따라간다)