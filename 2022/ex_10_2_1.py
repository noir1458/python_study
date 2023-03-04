dict1 = {"a" : 1, "b" : 253, "c" : 356, "d" : 407} # 집합기호 => 순서는 상관x
dict2 = dict([("e", 654), ("f", 906)]) # tuple쌍을 list로 감싼 dict 형식도 가능하다

# method : dict_name.keys()
print(dict1.keys()) # Returns a list containing the dictionary’s keys(실제 리스트는 아니라서 슬라이싱 불가)
# method : dict_namee.values()
print(dict1.values()) # Returns a list of all the values in the dictionary
# method : dict_name.get(key_value)
print(dict1.get('a')) # 1 (키 'a' 의 value는 1, value는 가져와서 조작가능, key는 불가)
print(dict1.get(1)) # None (키 1은 없음, Returns the value of the specified key)
# method : dict_name.items()
print(dict1.items()) # Returns a list containing a tuple for each key value pair


# method: pop, popitem, copy
dict1.pop("a")
print(dict1)
dict1.popitem() #delete the last item
print(dict1)
dict3 = dict1.copy()
print(dict3)
dict4 = dict1
print(dict4)
dict2.clear()
print(dict2)

#update
d1 = { "a":1, "b":2 }
d2 = { "c":3 }
#d3 = d1 + d2 불가능, key 겹칠경우 우선순위를 알수가 없게되므로 update 사용
d3 = dict()
d3.update(d1)
d3.update(d2)
print(d3)


# list(enumerate(['A', 'B', 'C'])) 
# enumerate() 함수는 인자로 넘어온 목록을 기준으로 인덱스와 원소를 차례대로 접근하게 해주는 반복자(iterator) 객체를 반환해주는 함수
# >> [(0, 'A'), (1, 'B'), (2, 'C')]