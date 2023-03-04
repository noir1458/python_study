

def buildMenu():

    # my code
    Menu = {}

    while(True):
        input_key = input("메뉴명을 입력하세요, exit을 입력시 그만 입력받습니다 > ") #dish name
        if(input_key == "exit"):
            break
        input_value = input("가격을 입력하세요 > ") #price

        #Menu[input_key] = int(input_value) #메뉴에 입력합니다
        #add(name:price) to Menu, using Menu.update() method
        Menu.update({input_key : int(input_value)})
        #괄호하고 튜플로주거나, 콜론으로 하거나 딕셔너리로 줘야 함


        print(Menu)
    return Menu


def getOrder(Menu):
    tot_price = 0

    while(True):
        # menu_name = Menu.keys()

        input_order = input("Your Order, stop 입력시 그만 입력받습니다 > ")
        if(input_order == "stop"):
            break
        elif(input_order not in Menu.keys()): # not in, prompt
            print("메뉴에 없는것을 주문하셨습니다.")
        else: # input order in ... sum
            print(input_order, " = ", Menu[input_order])
            tot_price = tot_price + Menu[input_order]
    
    # my code

    return tot_price

def main():
    Menu = buildMenu()
    print(Menu)
    
    total_Price = getOrder(Menu)
    print("the total price = ", total_Price)
    return None

if (__name__ == "__main__"):
    main()


