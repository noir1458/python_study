dict1 = {}
a = [1,2,1]

for k in a:
    dict1[k] = dict1.get(k,{})
    dict1[k][k] = dict1[k].get(dict1[k],0)+1

    print(dict1[k])

print(dict1)