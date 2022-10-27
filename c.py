i_tuple = (-30,10,77,450,1)
acc_dict={}

'''for idx in range(len(i_tuple)):
    if idx == 0:
        acc_dict[idx+1] = i_tuple[idx]
    else:
        k = acc_dict[idx]
        acc_dict[idx+1] = k + i_tuple[idx] '''


tmp_acc = 0
for idx in range(len(i_tuple)):
    tmp_acc = tmp_acc + i_tuple[idx]
    acc_dict[idx+1] = tmp_acc

print(acc_dict)