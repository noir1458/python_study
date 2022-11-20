tmp_dict = {}
tmp = ""
fpath, fname, fmode = "./", "grade.csv", "r"
fhandle = open(fpath + fname, fmode)
while(True):
    line = fhandle.readline() # 한줄단위 읽기
    if len(line)==0:
        tmp = line
        break
    if (line[0] == "+" or line[0] == "|"): #(맨 위 3줄 헤더는 읽지 않도록)
        continue
    line_split1 = line.split(",") # 먼저 콤마로 쪼개고
    line_split2 = line_split1[-1].split(";") # 맨 뒤에걸 세미콜론으로 쪼개고
    del line_split1[-1] # 맨 뒤에건 지운뒤에 합치면 한 줄을 나눈 리스트가 된다
    line_split = line_split1 + line_split2
    
    name, score = "", ""
    for n in range(-5,0):
        score = score + line_split[n] #성적 부분을 score에 더하고
        del line_split[n] #리스트에서 지워서 이름만 남긴다
    for k in line_split:
        name = name + k
    tmp_dict.update({name:score[:-1]}) #이름과 성적 문자를 dictionary에 저장
print(tmp_dict)
# 왜 맨 마지막줄은 안읽어올까?

print("ThomasLee" in tmp_dict)
print(len(tmp_dict))