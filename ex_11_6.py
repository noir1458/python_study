

def findLocation(city_dict, city_name):
    location = ()
    #your code
    if city_name not in city_dict.keys():
        del location
        location = "Not in"
    else:
        location = city_dict[city_name]

    return location

def buildCityDict():
    city_dict = {}
    #your code
    #fpath ===

    fpath, fname, fmode = "./", "uscities.csv", "r"
    fhandle = open(fpath+fname,fmode)
    
    while(True):
        line = fhandle.readline()
        if(0==len(line)):
            break
        split_line = line.split(',')
        
        city = split_line[0][1:-1]
        if(city=="city"):
            continue
        lat = split_line[6][1:-1]
        lng = split_line[7][1:-1]
        city_dict.update({city:(lat,lng)})
        
    fhandle.close()
    return city_dict



def main():
    city_dict = buildCityDict()
    while(True):
        city_name = input("Enter the city name : ")
        if("stop"== city_name):
            break
        location = findLocation(city_dict,city_name)
        print(location)
    
    return None

if __name__=="__main__":
    main()