def buildUI():
    # your code
    print("+----------------------------- Menu ------------------------------+\n" +
"| 1. Give a file which lists all students whose GPA > x.xx        |\n" + 
"| 2. The number of students who gain an A in Arts                 |\n" +
"| 3. The list of student names who gain an A in 3 or more classes |\n" + 
"| 4. Give a file which lists all student in the bottom 1%         |\n" + 
"| 5. Exit                                                         |\n" +
"+-----------------------------------------------------------------+")
    return None

def findStudentsInBottom1Percent():
    # your code
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
    # 이름 중복시 잘 덮어씌워지는것 확인

    gpa_dict = {}
    for k,v in tmp_dict.items(): # value의 성적 문자를 gpa값으로 바꾸기
        tmp_gpa = 0
        for n in v:
            if n == "A":
                tmp_gpa = tmp_gpa + 4.5
            elif  n == "B":
                tmp_gpa = tmp_gpa + 3.5
            elif  n == "C":
                tmp_gpa = tmp_gpa + 2.5
            elif  n == "D":
                tmp_gpa = tmp_gpa + 1.5
            else:
                tmp_gpa = tmp_gpa + 0
        gpa_dict.update({k:tmp_gpa/5})
    #print(gpa_dict)

    #하위 1%에 속하는 이름과 성적을 파일에 저장하기


    #gpa_dict 안에서 그 성적대인 학생을 찾아서 저장하여 출력
    gpa_list = list(gpa_dict.values()) #성적만 가져와서 정렬
    gpa_list.sort()
    #print(gpa_list)
    #print(len(gpa_list),len(gpa_dict))

    gpa_list2 = [] #중복되지 않는 성적 리스트
    for k in gpa_list:
        if k not in gpa_list2:
            gpa_list2 = gpa_list2 + [k]
    #print(gpa_list2)
    
    num_1 = (len(gpa_list)+1)*0.01  #백분위수는 int(num)+1, 리스트에서 int(num)번째 찾으면 된다
    num_2 = int(num_1) #소수점 아래 버림
    b1p_score = gpa_list[num_2+10] # a가 하위 1%의 성적이 된다 = 0.8
    #print(gpa_list.count(0.8)) #0.8이 63개...이므로 1%는 0.8보다 작아야함.

    #평점의 오름차순, 성의 알파벳순 파일저장
    #성적이 gpa_list3 안에것에 해당하면
    b1p_name = []
    fpath2, fname2, fmode2 = "./", "202231469_HW3_1p.txt", "w"
    fhandle2 = open(fpath2 + fname2, fmode2)

    for k,v in gpa_dict.items():
        if v < b1p_score: 
            b1p_name = b1p_name + [k]
    b1p_name.sort() #성적 하위 1p의 성의 알파벳순 리스트 저장
    #먼저 성의 알파벳순으로 저장된 리스트에서, 평점의 오름차순으로 출력하면 된다.

    
    for tmp_gpa in gpa_list2:
        if tmp_gpa >= b1p_score: #중복 없이 성적이 저장된 리스트중 하위 1p만 해당되는것
            continue
        for tmp_name in b1p_name:
            if gpa_dict[tmp_name] == tmp_gpa:
                fhandle2.write("name : " + tmp_name + ", gpa : " + str(tmp_gpa) + "\n")

    fhandle2.close()
    fhandle.close()
    return None

def findStudentsAIn3OrMore():
    student_dict = {}
    # your code
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


    #tmp_dict에서 A개수를 센다
    #A가 3개 이상인경우 몇번째의 A인지 봐서, 그걸 과목명 tuple로 만들기(이름은 그대로 쓰면 된다)
    for k,v in tmp_dict.items():
        sub_list = []
        if v.count("A") >= 3:
            if v[0] == "A":
                sub_list = sub_list + ["Python"]
            if v[1] == "A":
                sub_list = sub_list + ["History"]
            if v[2] == "A":
                sub_list = sub_list + ["English"]
            if v[3] == "A":
                sub_list = sub_list + ["Music"]
            if v[4] == "A":
                sub_list = sub_list + ["Arts"]
            if len(sub_list) < 3:
                continue
            student_dict.update({k:tuple(sub_list)})


    fhandle.close()
    return student_dict

def findStudentsAInArts():
    num = 0
    # your code
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

    
    # value의 맨 마지막(arts)이 A인 학생수 count
    for v in tmp_dict.values():
        if v[-1] == "A":
            num = num + 1

    fhandle.close()
    return num

def findStudentsGpaBiggerThan(gpa):
    # your code
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


    gpa_dict = {}
    for k,v in tmp_dict.items(): # value의 성적 문자를 gpa값으로 바꾸기
        tmp_gpa = 0
        for n in v:
            if n == "A":
                tmp_gpa = tmp_gpa + 4.5
            elif  n == "B":
                tmp_gpa = tmp_gpa + 3.5
            elif  n == "C":
                tmp_gpa = tmp_gpa + 2.5
            elif  n == "D":
                tmp_gpa = tmp_gpa + 1.5
            else:
                tmp_gpa = tmp_gpa + 0
        gpa_dict.update({k:tmp_gpa/5})
    #print(gpa_dict)
    
    # 위에서 gpa 계산한것 그대로
    # gpa 변수와 크기 비교하여, 더 큰 학생과 gpa값 파일저장
    
    fpath2, fname2, fmode2 = "./", "202231469_HW3_gpa.txt", "w"
    fhandle2 = open(fpath2 + fname2, fmode2)
    for k,v in gpa_dict.items():
        if v > gpa:
            #print(k,v,gpa)
            gpa_formatter = "{:.2f}"
            v_write = gpa_formatter.format(v)
            fhandle2.write("name : " + k + ", gpa : " + v_write+ "\n")
            #print(k,v)
    
    #gpa값 소수점 아래 2자리까지 나오게 foramtting하기
    #정렬필요?

    fhandle2.close() 
    fhandle.close()
    return None

def selectMenu():
    while(True):
        onCommand = input("Your onCommand: ")
        if ("5" == onCommand):
            break
        elif ("4" == onCommand):
            findStudentsInBottom1Percent()
        elif ("3" == onCommand):
            student_dict = findStudentsAIn3OrMore()
            print("[Answer]")
            print(student_dict)
        elif ("2" == onCommand):
            num = findStudentsAInArts()
            print("[Answer]")
            print(num)
        elif ("1" == onCommand):
            gpa = input("What is the GPA?...")
            findStudentsGpaBiggerThan(float(gpa))
        else:
            print("An invalid onCommand...try again")
        return None

def main():
    buildUI()
    selectMenu()

if (__name__ == "__main__"):
    main()