"""
@file 202xxxxxx_Final_Exam.py
@description Final Exam Python template file
=> Rename by replacing 202xxxxxx by your own StudentID
"""
class _GBaio():
    #class variables
    ACGT_dict__ = {'A':0, 'C':0, 'G':0, 'T':0}
    # Ans) ACGT_dict - 염기서열 파일중 A,C,G,T 를 뜯어서 분석해야 함, 분석이 되기 전에는 일단 모두 0으로

    #constructors
    def __new__(cls,*args):
        #your code
        obj = super(_GBaio,cls).__new__(cls)
        return obj

    def __init__(self, ifpath = './', ifname = None , ofpath = './', ofname = None, spec = 'not classified'):
        #your code
        self._species_class = spec
        self._ifname = ifname
        self._ifhandle = open(ifpath + ifname, "r")
        self._ofhandle = open(ofpath + ofname, "w")
        return None
    
    #destructors
    def __del__(self):
        self._ifhandle.close()
        self._ofhandle.close()
        return None

    #user-defined methods
    def _count(self):
        nucleotides = _GBaio.ACGT_dict__
        #key = ACGT, value = 개수\
        #your code
        fhandle = self._ifhandle
        line_count = 0
        while(True):
            line = fhandle.readline()
            line_count += 1
            if len(line) == 0:
                break
            if line_count % 4 == 2: #4로 나눴을때 나머지가 2인 줄이면 acgt 체크해서 더한다.
                for tmp in line:
                    nucleotides[tmp] = nucleotides.get(tmp,0) + 1
        return nucleotides

    def _classify(self,nucleotides):
        total_GC, total_AT, total_ACGT = nucleotides['G']+nucleotides['C'], nucleotides['A']+nucleotides['T'], nucleotides['G']+nucleotides['C']+nucleotides['A']+nucleotides['T']
        delta_GC, delta_AT, ratio_ATGC = total_GC/total_ACGT*100, total_AT/total_ACGT*100, total_AT/total_GC

        if delta_GC > 55:
            self._species_class = 'Hobbit'
        elif 35 <= delta_GC and delta_GC <= 55:
            self._species_class = 'Muggle'
        else:
            #delta_GC <35
            self._species_class = 'Elf'
            
        #result.txt 쓰기
        fhandle = self._ofhandle
        str_a = 'Total number of GC = ' + str(total_GC) + '\n'
        str_b = 'Total number of AT = ' + str(total_AT) + '\n'
        str_c = 'Total number of Nucleotides = ' + str(total_ACGT) + '\n'
        str_d = 'GC-Content = ' + str(delta_GC) + '%\n'
        str_e = 'AT-Content = ' + str(delta_AT) + '%\n'
        str_f = 'AT/GC Ratio = ' + str(ratio_ATGC) + '\n'
        str_g = 'The classification result = ' + self._species_class
        fhandle.write(str_a + str_b + str_c + str_d + str_e + str_f + str_g)
        #your code
        return None

    # magic function
    def __str__(self):
        # your code
        str4 = 'Done! The GC-Content says that you are ' + self._species_class
        return str4

def main():       
    print("+++++++++ Final Exam +++++++++")
    # please modify ****** and xxxxxx
    print("My name is 서정민 and ID is 202231469")
    # input file and output file paths
    ifpath, ofpath = "./", "./"
    # in/output file names
    ifname = input("Enter the input file name: ")
    ofname = "result.txt"
    gbaio = _GBaio(ifpath, ifname, ofpath, ofname)
    # your code
    nucleotides = gbaio._count()
    gbaio._classify(nucleotides)

    print(gbaio)
    return None

if __name__=="__main__":
    main()
