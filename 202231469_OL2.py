def exp_(x):
    e = 2.718281828459045235360287471352
    return e**(x)

def predict_diabetes():
    fpath, fname, fmode = "./", "diabetes.csv", "r"
    fhandle = open(fpath + fname, fmode)
    likelihood = 0 # the number of expectations
    # your code
    # ...   
    while(True):
        line = fhandle.readline()
        if line == "":
            break
        if line[0] == "+" or line[0] == "|":
            continue
        split_line = line.split(",")
        #print(line)
        #print(split_line)
        age = int(split_line[0])
        sex = float(split_line[1])
        BMI = float(split_line[2])
        PT = float(split_line[3])
        RPG = float(split_line[4][:-1])
        #print(type(RPG))
        
        x = -10.0382 + 0.0331 * age + 0.0308 * RPG + 0.2500 * PT + 0.5620 * sex + 0.0346 * BMI
        predictive = exp_(x) / (exp_(x) - 1)
        if predictive > 0.20:
            likelihood = likelihood + 1

    fhandle.close()
    return likelihood

def main():
    n = predict_diabetes()
    print(n, "are at risk of diabetes")
    return None

if __name__ == "__main__":
    main()